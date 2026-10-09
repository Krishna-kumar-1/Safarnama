"""
Indian Railways Real Track Geometry Loader & Leg Slicer.

Loads the open Indian Railways GeoJSON dataset (data/raw/trains.json) once at startup.
For any train number and station pair (A -> B), slices the train's real track LineString
between the closest coordinate to A and closest coordinate to B, following every curve,
bend, bridge, and turnout.
"""

import json
import logging
import math
from pathlib import Path
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger("safarnama.train_geometry")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TRAINS_GEOJSON_PATH = DATA_DIR / "raw" / "trains.json"

# In-memory lookup: train_number -> list of [lon, lat]
_TRAIN_LINESTRINGS: Dict[str, List[List[float]]] = {}
_INITIALIZED = False


def load_train_geometries(path: Path = TRAINS_GEOJSON_PATH) -> Dict[str, List[List[float]]]:
    """
    Load trains.json once at startup into memory.
    Keys are train numbers (both raw e.g. '04601' and stripped e.g. '4601').
    Values are GeoJSON coordinates: [[lon, lat], [lon, lat], ...].
    """
    global _TRAIN_LINESTRINGS, _INITIALIZED
    if _INITIALIZED:
        return _TRAIN_LINESTRINGS

    data = None
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            logger.warning(f"Error reading trains.json from disk: {e}")
    else:
        try:
            from .vault import load_vault_files
            v = load_vault_files()
            if "raw/trains.json" in v:
                data = json.loads(v["raw/trains.json"])
        except Exception as e:
            logger.warning(f"Error reading trains.json from vault: {e}")

    if not data:
        _INITIALIZED = True
        return _TRAIN_LINESTRINGS

    try:
        features = data.get("features", [])
        for feat in features:
            props = feat.get("properties", {})
            geom = feat.get("geometry", {})
            if geom.get("type") != "LineString":
                continue
            coords = geom.get("coordinates", [])
            if not coords:
                continue

            num = str(props.get("number", "")).strip()
            if num:
                _TRAIN_LINESTRINGS[num] = coords
                stripped = num.lstrip("0")
                if stripped and stripped != num:
                    _TRAIN_LINESTRINGS[stripped] = coords

        _INITIALIZED = True
        logger.info(f"Loaded {len(_TRAIN_LINESTRINGS)} train track geometry mappings from {path}")
    except Exception as exc:
        logger.error(f"Failed to load train geometry from {path}: {exc}")
        _INITIALIZED = True

    return _TRAIN_LINESTRINGS


def _closest_coord_index(coords: List[List[float]], lat: float, lon: float) -> int:
    """Find the index of the coordinate in coords [[lon, lat], ...] closest to (lat, lon)."""
    cos_lat = math.cos(math.radians(lat))
    best_idx = 0
    min_dist_sq = float("inf")
    for i, pt in enumerate(coords):
        # pt is [lon, lat]
        dx = (pt[0] - lon) * cos_lat
        dy = pt[1] - lat
        d2 = dx * dx + dy * dy
        if d2 < min_dist_sq:
            min_dist_sq = d2
            best_idx = i
    return best_idx


STATION_CODE_ALIASES = {
    "MBDP": "PBH",  # Maa Belha Devi Dham Pratapgarh -> Pratapgarh Jn
    "AYC": "FD",    # Ayodhya Cantt -> Faizabad Jn
    "PRYJ": "ALD",  # Prayagraj Jn -> Allahabad Jn
    "DDU": "MGS",   # Pt Deen Dayal Upadhyaya -> Mughalsarai Jn
    "VGLJ": "JHS",  # Virangana Lakshmibai Jhansi -> Jhansi Jn
}


def _resolve_station_coords(code: str, stations_map: dict) -> Optional[Tuple[float, float]]:
    st = stations_map.get(code)
    if st and getattr(st, "has_coords", False):
        return (st.lat, st.lon)
    alt_code = STATION_CODE_ALIASES.get(code)
    if alt_code:
        alt_st = stations_map.get(alt_code)
        if alt_st and getattr(alt_st, "has_coords", False):
            return (alt_st.lat, alt_st.lon)
    return None


def get_train_leg_geometry(
    train_number: str,
    source_code: str,
    dest_code: str,
    stations_map: dict
) -> Tuple[List[List[float]], bool]:
    """
    Returns (coordinates, is_real_geometry) for a route leg.
    - coordinates is in Leaflet format: [[lat, lon], [lat, lon], ...]
    - is_real_geometry is True if sliced from trains.json LineString,
      or False if using fallback straight-line station platform coordinates.
    """
    if not _INITIALIZED:
        load_train_geometries()

    coordsA = _resolve_station_coords(source_code, stations_map)
    coordsB = _resolve_station_coords(dest_code, stations_map)

    if not coordsA or not coordsB:
        pts = []
        if coordsA:
            pts.append([coordsA[0], coordsA[1]])
        if coordsB:
            pts.append([coordsB[0], coordsB[1]])
        return pts, False

    latA, lonA = coordsA
    latB, lonB = coordsB

    t_key = str(train_number).strip() if train_number else ""
    coords = _TRAIN_LINESTRINGS.get(t_key) or _TRAIN_LINESTRINGS.get(t_key.lstrip("0"))

    if not coords or len(coords) < 2:
        # Fallback straight line between stations
        return [[latA, lonA], [latB, lonB]], False

    # Find closest indices in LineString
    idxA = _closest_coord_index(coords, latA, lonA)
    idxB = _closest_coord_index(coords, latB, lonB)

    if idxA == idxB:
        # Stations map to the same nearest track waypoint (very close stations)
        return [[latA, lonA], [latB, lonB]], True

    if idxA < idxB:
        sub = coords[idxA : idxB + 1]
    else:
        # Train traveling reverse direction of LineString
        sub = coords[idxB : idxA + 1][::-1]

    # Convert GeoJSON [lon, lat] to Leaflet [lat, lon]
    leaflet_pts = [[c[1], c[0]] for c in sub]

    # Snap exact start and end coordinates to the station platform positions
    leaflet_pts[0] = [latA, lonA]
    leaflet_pts[-1] = [latB, lonB]

    return leaflet_pts, True
