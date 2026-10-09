import json
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from src.last_mile import haversine_km
from src.route_engine import RouteEngine, estimate_class_fares
from src.ntes_engine import (
    get_train_ntes_details,
    get_trains_between_stations,
    get_train_exceptions,
)
from src.railkit_client import (
    check_pnr_status,
    track_train,
    check_seat_availability,
    get_live_station,
)
from src.assistant_engine import SafarnamaAssistant
from src.track_geometry import get_exact_track_geometry
from src.train_geometry import get_train_leg_geometry, load_train_geometries

app = Flask(__name__, static_folder="static")
CORS(app)
engine = RouteEngine()
assistant = SafarnamaAssistant(engine)
load_train_geometries()

DATA_DIR = Path(__file__).resolve().parent / "data"
META_FILE = DATA_DIR / "train_metadata.json"
TRAIN_METADATA = {}
if META_FILE.exists():
    try:
        with open(META_FILE, "r", encoding="utf-8") as f:
            TRAIN_METADATA = json.load(f)
    except Exception as e:
        print("Warning: failed to load train metadata:", e)
else:
    try:
        from src.vault import load_vault_files
        _vf = load_vault_files()
        if "train_metadata.json" in _vf:
            TRAIN_METADATA = json.loads(_vf["train_metadata.json"])
    except Exception as e:
        print("Warning: failed to load train metadata from vault:", e)


def get_station_distance_km(source_code, dest_code):
    s1 = engine.stations.get(source_code)
    s2 = engine.stations.get(dest_code)
    if s1 and s2 and s1.has_coords and s2.has_coords:
        return round(haversine_km(s1.lat, s1.lon, s2.lat, s2.lon), 1)
    return None


def get_path_details(source_code, dest_code, train_number=""):
    path_codes = engine.get_leg_path_stations(source_code, dest_code, train_number)
    path_stations = []
    path_coordinates = []
    for code in path_codes:
        st = engine.stations.get(code)
        if st:
            path_stations.append({
                "code": st.code,
                "name": st.name,
                "state": st.state,
                "lat": st.lat,
                "lon": st.lon,
            })
            if st.has_coords:
                path_coordinates.append([st.lat, st.lon])
    return path_stations, path_coordinates


def leg_to_dict(leg):
    dist = get_station_distance_km(leg.source, leg.destination)
    path_stations, path_coords = get_path_details(leg.source, leg.destination, leg.train_number)
    track_geom, is_real = get_train_leg_geometry(leg.train_number, leg.source, leg.destination, engine.stations)
    if not is_real and len(path_coords) >= 2:
        track_geom = path_coords
    t_meta = TRAIN_METADATA.get(leg.train_number, {}) if leg.train_number else {}
    dist_val = dist or t_meta.get("distance_km")
    return {
        "source": leg.source,
        "source_name": engine.stations.get(leg.source).name if leg.source in engine.stations else leg.source,
        "destination": leg.destination,
        "destination_name": engine.stations.get(leg.destination).name if leg.destination in engine.stations else leg.destination,
        "mode": leg.mode,
        "duration_min": leg.duration_min,
        "cost_inr": leg.cost_inr,
        "distance_km": dist_val,
        "class_fares": estimate_class_fares(dist_val, leg.cost_inr),
        "train_number": leg.train_number,
        "train_name": leg.train_name,
        "available": leg.available,
        "date": leg.date,
        "dep_time": leg.dep_time or "",
        "arr_time": leg.arr_time or "",
        "valid_from": leg.valid_from,
        "valid_to": leg.valid_to,
        "train_type": t_meta.get("type", ""),
        "zone": t_meta.get("zone", ""),
        "classes": t_meta.get("classes", ""),
        "halts": t_meta.get("halts", 0),
        "speed_kmh": t_meta.get("speed_kmh", 0),
        "tags": t_meta.get("tags", []),
        "return_train": t_meta.get("return_train", ""),
        "path_stations": path_stations,
        "path_coordinates": path_coords,
        "track_geometry": track_geom,
        "is_real_geometry": is_real,
    }


def itinerary_to_dict(itinerary):
    if itinerary is None:
        return None
    legs = [leg_to_dict(leg) for leg in itinerary.legs]
    total_dist = sum(l["distance_km"] for l in legs if l["distance_km"] is not None)
    return {
        "legs": legs,
        "total_duration_min": itinerary.total_duration_min,
        "total_cost_inr": itinerary.total_cost_inr,
        "total_distance_km": round(total_dist, 1) if total_dist > 0 else None,
        "total_class_fares": estimate_class_fares(total_dist, itinerary.total_cost_inr),
        "num_legs": itinerary.num_legs,
        "has_sold_out_leg": itinerary.has_sold_out_leg,
    }


def station_name(code):
    return engine.stations.get(code).name if code in engine.stations else code


def schedule_leg_to_dict(leg):
    dist = get_station_distance_km(leg["source"], leg["destination"])
    path_stations, path_coords = get_path_details(leg["source"], leg["destination"], leg.get("train_number", ""))
    tno = leg.get("train_number", "")
    track_geom, is_real = get_train_leg_geometry(tno, leg["source"], leg["destination"], engine.stations)
    if not is_real and len(path_coords) >= 2:
        track_geom = path_coords
    t_meta = TRAIN_METADATA.get(tno, {}) if tno else {}
    dist_val = dist or t_meta.get("distance_km")
    return {
        **leg,
        "source_name": station_name(leg["source"]),
        "destination_name": station_name(leg["destination"]),
        "distance_km": dist_val,
        "class_fares": estimate_class_fares(dist_val, leg.get("cost_inr", 0)),
        "train_type": t_meta.get("type", ""),
        "zone": t_meta.get("zone", ""),
        "classes": t_meta.get("classes", ""),
        "halts": t_meta.get("halts", 0),
        "speed_kmh": t_meta.get("speed_kmh", 0),
        "tags": t_meta.get("tags", []),
        "return_train": t_meta.get("return_train", ""),
        "path_stations": path_stations,
        "path_coordinates": path_coords,
        "track_geometry": track_geom,
        "is_real_geometry": is_real,
    }


def plan_candidate_to_dict(candidate):
    schedule = candidate["schedule"]
    legs = [schedule_leg_to_dict(leg) for leg in schedule["legs"]]
    total_dist = sum(l["distance_km"] for l in legs if l["distance_km"] is not None)
    return {
        "legs": legs,
        "num_legs": candidate["itinerary"].num_legs,
        "total_cost_inr": candidate["itinerary"].total_cost_inr,
        "total_distance_km": round(total_dist, 1) if total_dist > 0 else None,
        "total_class_fares": estimate_class_fares(total_dist, candidate["itinerary"].total_cost_inr),
        "start_date": schedule["start_date"],
        "start_time": schedule["start_time"],
        "arrival_date": schedule["arrival_date"],
        "arrival_time": schedule["arrival_time"],
        "total_elapsed_min": schedule["total_elapsed_min"],
        "total_duration_min": schedule["total_elapsed_min"],
        "total_wait_min": schedule["total_wait_min"],
        "total_days": schedule["total_days"],
        "all_legs_run_on_date": schedule["all_legs_run_on_date"],
    }


def schedule_or_itinerary_to_dict(itinerary, date=None, time_str="00:00"):
    if itinerary is None:
        return None
    if date:
        try:
            sched = engine.schedule_itinerary(itinerary, date, time_str)
            return plan_candidate_to_dict({"itinerary": itinerary, "schedule": sched})
        except Exception:
            pass
    return itinerary_to_dict(itinerary)


def planned_to_dict(planned):
    if planned is None:
        return None
    return {
        "best": plan_candidate_to_dict(planned["best"]),
        "alternatives": [plan_candidate_to_dict(c) for c in planned["alternatives"]],
    }


def flexible_option_to_dict(opt):
    return {
        "date": opt["date"],
        "offset_days": opt["offset_days"],
        "is_direct": opt["is_direct"],
        "num_legs": opt["num_legs"],
        "advantage": opt["advantage"],
        "plan": plan_candidate_to_dict(opt["candidate"]),
    }


@app.get("/")
def index():
    return send_from_directory("static", "index.html")


@app.get("/journey")
def journey():
    return send_from_directory("static", "journey.html")


@app.get("/live")
def live_portal():
    return send_from_directory("static", "live.html")


@app.get("/api/stations")
def stations():
    return jsonify(
        [{"code": s.code, "name": s.name, "state": s.state, "lat": s.lat, "lon": s.lon} for s in engine.stations.values()]
    )


@app.get("/api/route")
def route():
    source = request.args.get("source")
    destination = request.args.get("destination")
    date = request.args.get("date") or None
    time_str = request.args.get("time") or "00:00"
    flexible = request.args.get("flexible") in ("true", "1", "yes")
    try:
        days_range = max(1, min(5, int(request.args.get("days") or 3)))
    except (ValueError, TypeError):
        days_range = 3

    if not source or not destination:
        return jsonify({"error": "source and destination are required"}), 400
    if source == destination:
        return jsonify({"error": "source and destination must differ"}), 400

    try:
        result = engine.find_routes(source, destination, date=date)
        flexible_options = []
        if date:
            if flexible:
                flex_res = engine.plan_journey_flexible(source, destination, date, time_str, days_range=days_range)
                planned = flex_res["exact_plan"]
                flexible_options = [flexible_option_to_dict(o) for o in flex_res["flexible_options"]]
            else:
                planned = engine.plan_journey(source, destination, date, time_str)
        else:
            planned = None
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    # Schedule each route result so every single option has full transfer layovers and dates/times
    fastest_dict = schedule_or_itinerary_to_dict(result["fastest"], date, time_str)
    cheapest_dict = schedule_or_itinerary_to_dict(result["cheapest"], date, time_str)
    recommended_dict = schedule_or_itinerary_to_dict(result["recommended"], date, time_str)
    simplest_dict = schedule_or_itinerary_to_dict(result["simplest"], date, time_str)
    alternatives_dict = [schedule_or_itinerary_to_dict(a, date, time_str) for a in result["alternatives"]]

    return jsonify(
        {
            "fastest": fastest_dict,
            "cheapest": cheapest_dict,
            "recommended": recommended_dict,
            "simplest": simplest_dict,
            "alternatives": alternatives_dict,
            "warnings": result["warnings"],
            "planned": planned_to_dict(planned),
            "flexible_options": flexible_options,
        }
    )


# =========================================================================
# RailKit API Proxy Endpoints (Live PNR, Seat Availability & GPS Tracking)
# =========================================================================
@app.get("/api/railkit/pnr/<pnr>")
def api_railkit_pnr(pnr):
    return jsonify(check_pnr_status(pnr))


@app.get("/api/railkit/seats")
def api_railkit_seats():
    train_no = request.args.get("train", "")
    src = request.args.get("from", "")
    dst = request.args.get("to", "")
    date = request.args.get("date", "")
    class_code = request.args.get("class", "ALL")
    quota = request.args.get("quota", "GN")
    return jsonify(check_seat_availability(train_no, src, dst, date, class_code, quota))


@app.get("/api/railkit/track")
def api_railkit_track():
    train_no = request.args.get("train", "")
    date = request.args.get("date", None)
    return jsonify(track_train(train_no, date))


@app.get("/api/railkit/live-station/<station_code>")
def api_railkit_station(station_code):
    try:
        hours = int(request.args.get("hours") or 4)
    except (ValueError, TypeError):
        hours = 4
    return jsonify(get_live_station(station_code, hours))


# =========================================================================
# NTES Authentic Train Running Status & Ladder Route Engine
# =========================================================================
@app.get("/api/ntes/track/<train_no>")
def api_ntes_track(train_no):
    date = request.args.get("date", None)
    return jsonify(get_train_ntes_details(engine, train_no, date))


@app.get("/api/ntes/trains-between")
def api_ntes_trains_between():
    src = request.args.get("source", "")
    dst = request.args.get("destination", "")
    return jsonify(get_trains_between_stations(engine, src, dst))


@app.get("/api/ntes/exceptions")
def api_ntes_exceptions():
    return jsonify(get_train_exceptions())


# =========================================================================
# Safarnama AI Assistant & Hinglish/Voice Route Planner (Powered by Gemini)
# =========================================================================
@app.post("/api/assistant/chat")
def api_assistant_chat():
    data = request.get_json(force=True, silent=True) or {}
    message = data.get("message", "")
    history = data.get("history", [])
    res = assistant.process_message(message, history=history)
    return jsonify(res)


# =========================================================================
# Physical Railway Track Geometry API (100% Real Rails Snapping)
# =========================================================================
@app.post("/api/track/geometry")
def api_track_geometry():
    data = request.get_json(force=True, silent=True) or {}
    points = data.get("points") or []
    if not points or len(points) < 2:
        return jsonify({
            "status": "ok",
            "coordinates": points,
            "count": len(points),
            "snapped": False
        })
    try:
        coords = get_exact_track_geometry(points)
        snapped = len(coords) > len(points)
        return jsonify({
            "status": "ok",
            "coordinates": coords,
            "count": len(coords),
            "snapped": snapped
        })
    except Exception as exc:
        return jsonify({
            "status": "ok",
            "coordinates": points,
            "count": len(points),
            "snapped": False,
            "fallback_reason": str(exc)
        })


# =========================================================================
# API Key Configuration & Health Status (Safe public introspection)
# =========================================================================
@app.get("/api/config/status")
def api_config_status():
    from src.assistant_engine import _get_gemini_api_key
    from src.rapidapi_client import _get_rapid_keys
    from src.railkit_client import get_pool_status

    gemini_key = _get_gemini_api_key()
    rapid_keys = _get_rapid_keys()
    railkit_status = get_pool_status()
    rail_cnt = railkit_status.get("count", 0) if isinstance(railkit_status, dict) else 0

    import os
    gmaps_key = os.getenv("GOOGLE_MAPS_API_KEY", "").strip()
    if not gmaps_key:
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("GOOGLE_MAPS_API_KEY="):
                            gmaps_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                            if gmaps_key:
                                break
            except Exception:
                pass

    return jsonify({
        "gemini": {
            "configured": bool(gemini_key),
            "model": "gemini-2.5-flash",
            "masked": f"...{gemini_key[-4:]}" if len(gemini_key) >= 4 else None,
        },
        "railkit": {
            "configured": rail_cnt > 0,
            "count": rail_cnt,
        },
        "rapidapi": {
            "configured": len(rapid_keys) > 0,
            "count": len(rapid_keys),
        },
        "google_maps": {
            "configured": bool(gmaps_key),
            "masked": f"...{gmaps_key[-4:]}" if len(gmaps_key) >= 4 else None,
            "key": gmaps_key if gmaps_key else None,
        },
        "offline_database": {
            "status": "online",
            "routes_count": len(engine.legs),
            "stations_count": len(engine.stations)
        }
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)

