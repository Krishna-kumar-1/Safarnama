"""Client for the RailRadar API (api.railradar.in).

Fills the two gaps the scraped timetable listings cannot:

  * intermediate halts -- the listing only publishes origin and destination,
    so the graph could only model whole trains. The API returns every halt,
    which lets a passenger board mid-route.
  * running days -- the listing shows these by highlighting letters, and
    copy-paste loses the highlighting, so they were never recorded.

Station coordinates come along for free: every station inside a train's route
carries lat/lng, which is what the imported stations were missing.

The key is read from the RAILRADAR_API_KEY environment variable and is never
written to disk or logged -- do not paste it into a file that gets committed.

    setx RAILRADAR_API_KEY "rg_..."        (Windows, new shell after)
    export RAILRADAR_API_KEY=rg_...        (bash)

Every response is cached under data/raw/railradar/, so re-running costs no
quota. The free tier is small; deleting the cache means paying for it again.
"""

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://api.railradar.in/v1"
API_KEY_ENV = "RAILRADAR_API_KEY"
CACHE = Path(__file__).resolve().parent.parent / "data" / "raw" / "railradar"

TIMEOUT_S = 30
# The API allows 10 requests/minute and 1000/month (it reports both in
# x-ratelimit-* headers). Spacing requests just over 6s keeps us inside the
# per-minute window without ever tripping a 429.
DELAY_S = 6.3
RETRIES = 3
COOLDOWN_S = 62        # a full minute plus slack, when a 429 does slip through

# Last seen values from x-ratelimit-remaining-*; None until a call is made.
remaining_minute: int | None = None
remaining_month: int | None = None


class RailRadarError(RuntimeError):
    """Any failure that should stop the caller cleanly, without a traceback."""


class MissingApiKey(RailRadarError):
    pass


class QuotaExhausted(RailRadarError):
    pass


def api_key() -> str:
    key = os.environ.get(API_KEY_ENV, "").strip()
    if not key:
        raise MissingApiKey(
            f"{API_KEY_ENV} is not set. Get a key at https://railradar.in/developers "
            f'then run:  setx {API_KEY_ENV} "rg_..."  and open a new terminal.'
        )
    return key


def _request(path: str) -> dict:
    request = urllib.request.Request(
        f"{BASE}{path}",
        headers={
            "Authorization": f"Bearer {api_key()}",
            "Accept": "application/json",
            "User-Agent": "safarnama-route-finder/1.0",
        },
    )
    global remaining_minute, remaining_month

    def note_limits(headers):
        global remaining_minute, remaining_month
        for name, target in (("x-ratelimit-remaining-min", "minute"),
                             ("x-ratelimit-remaining-month", "month")):
            value = headers.get(name)
            if value is None:
                continue
            try:
                parsed = int(value)
            except (TypeError, ValueError):
                continue
            if target == "minute":
                remaining_minute = parsed
            else:
                remaining_month = parsed

    last = None
    for attempt in range(1, RETRIES + 1):
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_S) as response:
                note_limits(response.headers)
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            note_limits(exc.headers or {})
            if exc.code == 401:
                raise RailRadarError("API key rejected (401). Check the key is current.")
            if exc.code == 404:
                return {"success": False, "error": {"code": "NOT_FOUND"}}
            if exc.code == 429:
                # Two very different situations share this status code.
                if remaining_month == 0:
                    raise QuotaExhausted(
                        "Monthly quota exhausted. Everything fetched so far is "
                        "cached and written; re-run next month to continue."
                    )
                # Per-minute burst limit: wait out the window and carry on.
                time.sleep(COOLDOWN_S)
                continue
            last = exc
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            last = exc
        time.sleep(DELAY_S * attempt)
    raise RailRadarError(f"{path} failed after {RETRIES} tries: {last}")


def fetch_train(number: str, refresh: bool = False) -> dict | None:
    """Full train record, or None if the API does not know this number.

    Cached on disk; a cached train never costs quota again.
    """
    number = str(number).strip()
    CACHE.mkdir(parents=True, exist_ok=True)
    cached = CACHE / f"train_{number}.json"

    if cached.exists() and not refresh:
        try:
            payload = json.loads(cached.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            cached.unlink()          # truncated write from an interrupted run
        else:
            return payload.get("data")

    if remaining_minute == 0:
        time.sleep(COOLDOWN_S)          # per-minute window is spent
    payload = _request(f"/trains/{number}")
    if not payload.get("success"):
        # Remember the miss too, so a bad number is not retried every run.
        cached.write_text(json.dumps(payload), encoding="utf-8")
        return None

    cached.write_text(json.dumps(payload), encoding="utf-8")
    time.sleep(DELAY_S)
    return payload.get("data")


def budget() -> str:
    """Human-readable view of what the key has left, for progress output."""
    month = "?" if remaining_month is None else remaining_month
    return f"{month} requests left this month"


# --------------------------------------------------------------- normalising

DAY_ORDER = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def run_days(train: dict) -> str:
    """['mon','wed'] -> 'mon,wed'. Empty string means unknown, not 'never'."""
    days = train.get("runDays") or []
    keep = [d for d in DAY_ORDER if d in {str(x).lower()[:3] for x in days}]
    return ",".join(keep)


def _minutes(hhmm: str | None) -> int | None:
    if not hhmm or ":" not in str(hhmm):
        return None
    hours, _, mins = str(hhmm).partition(":")
    try:
        return int(hours) * 60 + int(mins)
    except ValueError:
        return None


def halts(record: dict) -> list[dict]:
    """Commercial stops only.

    A route contains every point the train passes -- 237 of them for the Mumbai
    Rajdhani -- but only the 8 with isHalt set are places a passenger can
    actually board. Treating passing points as boardable would invent stops.
    """
    out = []
    for point in record.get("route") or []:
        if not point.get("isHalt"):
            continue
        station = point.get("station") or {}
        code = (station.get("code") or "").strip().upper()
        if not code:
            continue
        out.append({
            "code": code,
            "name": (station.get("name") or "").strip().title(),
            "lat": station.get("lat"),
            "lon": station.get("lng"),
            "departure": point.get("departure"),
            "arrival": point.get("arrival"),
            "distance_km": point.get("distance"),
        })
    return out


def segments(record: dict, premium_rate: float = 2.4, base_rate: float = 1.1) -> list[dict]:
    """Consecutive halt-to-halt legs, so mid-route boarding becomes possible.

    Eight halts give seven legs. Dijkstra chains them back together, so a
    passenger can join or leave anywhere the train actually stops.
    """
    train = record.get("train") or {}
    stops = halts(record)
    if len(stops) < 2:
        return []

    category = str(train.get("category") or "")
    kind = str(train.get("type") or "")
    premium = "Premium" in category or any(
        w in kind for w in ("Rajdhani", "Shatabdi", "Vande", "Tejas", "Duronto")
    )
    rate = premium_rate if premium else base_rate
    days = run_days(train)

    legs = []
    for first, second in zip(stops, stops[1:]):
        depart = _minutes(first["departure"])
        arrive = _minutes(second["arrival"] or second["departure"])
        if depart is None or arrive is None:
            continue
        duration = arrive - depart
        if duration <= 0:
            duration += 24 * 60          # crossed midnight
        km = None
        if first["distance_km"] is not None and second["distance_km"] is not None:
            km = max(0.0, float(second["distance_km"]) - float(first["distance_km"]))
        legs.append({
            "source": first["code"],
            "destination": second["code"],
            "mode": "train",
            "duration_min": duration,
            "cost_inr": round(km * rate) if km else round(duration * 0.9),
            "train_number": str(train.get("number") or "").strip(),
            "train_name": (train.get("name") or "").strip(),
            "available": "true",
            "date": "",
            "dep_time": first["departure"] or "",
            "arr_time": second["arrival"] or second["departure"] or "",
            "valid_from": "",
            "valid_to": "",
            "run_days": days,
        })
    return legs
