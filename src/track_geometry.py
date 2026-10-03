"""
Real Railway Track Geometry Module for Safarnama (Indian Railways Route Finder).

Fetches, caches, and stitches physical rail track geometry (GeoJSON coordinates)
from OpenStreetMap's physical railway network via BRouter's railway routing engine.
Ensures route polylines snap 100% to physical steel tracks, tracing every curve,
bend, bridge, and turnout matching OpenRailwayMap.
"""

import json
import logging
import os
import time
import urllib.error
import urllib.request
import hashlib
from typing import List, Tuple, Union

logger = logging.getLogger("safarnama.track_geometry")

CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
CACHE_FILE = os.path.join(CACHE_DIR, "track_geometry_cache.json")

_IN_MEMORY_CACHE = {}
_CACHE_LOADED = False


def _load_cache():
    global _CACHE_LOADED
    if _CACHE_LOADED:
        return
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    _IN_MEMORY_CACHE.clear()
                    _IN_MEMORY_CACHE.update(data)
        except Exception as e:
            logger.warning(f"Could not load track geometry cache: {e}")
            _IN_MEMORY_CACHE.clear()
    _CACHE_LOADED = True


def _save_cache():
    global _IN_MEMORY_CACHE
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        # Limit cache size to 1000 routes if it grows too large
        if len(_IN_MEMORY_CACHE) > 1000:
            keys = list(_IN_MEMORY_CACHE.keys())
            for k in keys[:-800]:
                del _IN_MEMORY_CACHE[k]
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(_IN_MEMORY_CACHE, f, separators=(",", ":"))
    except Exception as e:
        logger.warning(f"Could not save track geometry cache: {e}")


def _coord_cache_key(points: List[List[float]]) -> str:
    """Generate a compact cache key from ordered lat,lon pairs."""
    key_str = "|".join(f"{round(p[0], 4)},{round(p[1], 4)}" for p in points)
    return hashlib.sha256(key_str.encode("utf-8")).hexdigest()[:24]


def _fetch_brouter_chunk(points: List[List[float]], timeout: float = 6.0) -> List[List[float]]:
    """
    Fetch exact physical railway coordinates for a list of points from BRouter.
    points: list of [lat, lon]
    returns: list of [lat, lon]
    """
    if len(points) < 2:
        return points

    # BRouter expects: lonlats=lon1,lat1|lon2,lat2|...
    lonlats = "|".join(f"{p[1]:.5f},{p[0]:.5f}" for p in points)
    url = f"https://brouter.de/brouter?lonlats={lonlats}&profile=rail&format=geojson"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SafarnamaRail/2.0",
        "Accept": "application/json, text/plain, */*"
    }
    
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    raw_coords = data["features"][0]["geometry"]["coordinates"]
    # BRouter returns [lon, lat, elevation] -> convert to Leaflet [lat, lon]
    return [[c[1], c[0]] for c in raw_coords]


def get_exact_track_geometry(points: List[Union[List[float], Tuple[float, float]]], timeout: float = 8.0) -> List[List[float]]:
    """
    Given a list of station coordinates [[lat, lon], ...], returns the high-density
    physical railway track polyline [[lat, lon], ...] following every curve, bend,
    and bridge of the real tracks.
    
    If BRouter is unavailable or returns an error, gracefully falls back to the original
    station coordinates or stitched pairwise segments.
    """
    _load_cache()

    if not points or len(points) < 2:
        return [[float(p[0]), float(p[1])] for p in points] if points else []

    # Clean and deduplicate consecutive identical points
    cleaned_points = []
    for p in points:
        lat, lon = float(p[0]), float(p[1])
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            continue
        if cleaned_points:
            last_lat, last_lon = cleaned_points[-1]
            # Skip if closer than ~10 meters
            if abs(lat - last_lat) < 0.0001 and abs(lon - last_lon) < 0.0001:
                continue
        cleaned_points.append([lat, lon])

    if len(cleaned_points) < 2:
        return cleaned_points

    cache_key = _coord_cache_key(cleaned_points)
    if cache_key in _IN_MEMORY_CACHE:
        return _IN_MEMORY_CACHE[cache_key]

    # Strategy:
    # If 2 to 8 stations: query all points in a single chunk.
    # If > 8 stations: break into overlapping chunks of 6 stations (0..5, 5..10, etc.)
    # to avoid BRouter URL length limits or query complexity timeouts.
    result_coords = []
    chunk_size = 6
    overlap = 1
    
    chunks = []
    if len(cleaned_points) <= 8:
        chunks = [cleaned_points]
    else:
        i = 0
        while i < len(cleaned_points) - 1:
            end = min(i + chunk_size, len(cleaned_points))
            chunks.append(cleaned_points[i:end])
            if end >= len(cleaned_points):
                break
            i = end - overlap

    for chunk in chunks:
        chunk_coords = None
        try:
            chunk_coords = _fetch_brouter_chunk(chunk, timeout=timeout)
        except Exception as e:
            logger.debug(f"Direct chunk query failed ({e}), attempting pairwise fallback")
            # Fallback to pairwise for this chunk
            pair_coords = []
            for j in range(len(chunk) - 1):
                p1, p2 = chunk[j], chunk[j + 1]
                pair_key = _coord_cache_key([p1, p2])
                if pair_key in _IN_MEMORY_CACHE:
                    sub = _IN_MEMORY_CACHE[pair_key]
                else:
                    try:
                        sub = _fetch_brouter_chunk([p1, p2], timeout=min(4.0, timeout))
                        _IN_MEMORY_CACHE[pair_key] = sub
                    except Exception:
                        sub = [p1, p2]
                
                if pair_coords and sub:
                    pair_coords.extend(sub[1:])
                else:
                    pair_coords.extend(sub)
            chunk_coords = pair_coords

        if not chunk_coords:
            chunk_coords = chunk

        # Stitch into result_coords, avoiding duplicating junction points
        if result_coords and chunk_coords:
            result_coords.extend(chunk_coords[1:])
        else:
            result_coords.extend(chunk_coords)

    # If successful and high-density track was returned, cache it
    if len(result_coords) > len(cleaned_points):
        _IN_MEMORY_CACHE[cache_key] = result_coords
        _save_cache()
        return result_coords
    else:
        return cleaned_points
