from math import asin, cos, radians, sin, sqrt

from .models import RouteLeg

EARTH_RADIUS_KM = 6371.0

WALK_MAX_KM = 2
CAB_MAX_KM = 15

WALK_SPEED_KMPH = 4.5
CAB_SPEED_KMPH = 30
BUS_SPEED_KMPH = 22

CAB_BASE_FARE = 40
CAB_PER_KM = 15
BUS_PER_KM = 2.5


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    lat1, lon1, lat2, lon2 = map(radians, (lat1, lon1, lat2, lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * EARTH_RADIUS_KM * asin(sqrt(a))


def nearest_station(stations: dict, lat: float, lon: float):
    """Return (station, distance_km) for the closest station to a raw lat/lon."""
    best_station, best_dist = None, float("inf")
    for station in stations.values():
        # Imported stations have no published coordinates; they cannot be
        # snapped to, so skip them rather than treating them as (0, 0).
        if not station.has_coords:
            continue
        dist = haversine_km(lat, lon, station.lat, station.lon)
        if dist < best_dist:
            best_station, best_dist = station, dist
    return best_station, best_dist


def last_mile_leg(from_code: str, to_label: str, distance_km: float) -> RouteLeg:
    """Pick walk/cab/bus by distance threshold and estimate time+cost."""
    if distance_km <= WALK_MAX_KM:
        mode = "walk"
        duration_min = round(distance_km / WALK_SPEED_KMPH * 60)
        cost = 0.0
    elif distance_km <= CAB_MAX_KM:
        mode = "cab"
        duration_min = round(distance_km / CAB_SPEED_KMPH * 60)
        cost = round(CAB_BASE_FARE + distance_km * CAB_PER_KM, -1)
    else:
        mode = "bus"
        duration_min = round(distance_km / BUS_SPEED_KMPH * 60)
        cost = round(distance_km * BUS_PER_KM, -1)

    return RouteLeg(
        source=from_code,
        destination=to_label,
        mode=mode,
        duration_min=max(duration_min, 1),
        cost_inr=cost,
        available=True,
    )
