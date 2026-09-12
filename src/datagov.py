"""Optional live data source: data.gov.in Open Government Data (OGD) API.

The bundled CSVs stay the source of truth. This module can refresh them from
the official Indian Railways datasets published on data.gov.in, which -- unlike
scraping a timetable site -- is an open-licensed API meant to be read by
machines.

Needs a free API key from https://data.gov.in/user/register (the shared demo
key is rate-limited to the point of being unusable). Supply it as:

    export DATA_GOV_IN_API_KEY=...        # or set it in the environment

Nothing here runs at import time and nothing here is required for the app to
work: with no key, `fetch_resource` raises `MissingApiKey` and callers fall
back to the CSVs.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

API_ROOT = "https://api.data.gov.in/resource"
API_KEY_ENV = "DATA_GOV_IN_API_KEY"
PAGE_SIZE = 500
TIMEOUT_S = 30


class DataGovError(RuntimeError):
    """Any failure talking to data.gov.in."""


class MissingApiKey(DataGovError):
    def __init__(self):
        super().__init__(
            f"No {API_KEY_ENV} set. Get a free key at "
            "https://data.gov.in/user/register and export it, or keep using "
            "the bundled CSVs."
        )


class RateLimited(DataGovError):
    pass


def api_key() -> str:
    key = os.environ.get(API_KEY_ENV, "").strip()
    if not key:
        raise MissingApiKey()
    return key


def _get(url: str) -> dict:
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_S) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            raise RateLimited(
                "data.gov.in rate limit hit. The shared demo key is heavily "
                f"throttled -- set your own {API_KEY_ENV}."
            ) from exc
        raise DataGovError(f"data.gov.in returned HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise DataGovError(f"Could not reach data.gov.in: {exc.reason}") from exc
    except TimeoutError as exc:
        # a socket read timeout is not a URLError, so it would otherwise
        # escape as a raw traceback
        raise DataGovError(
            f"data.gov.in timed out after {TIMEOUT_S}s. It throttles by "
            "stalling the connection, so this usually means the key is "
            "rate-limited rather than the resource being wrong."
        ) from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise DataGovError(f"Bad response from data.gov.in: {exc}") from exc


def fetch_resource(resource_id: str, limit: int | None = None) -> list[dict]:
    """Page through one OGD resource and return its records.

    `limit` caps the total pulled; None means "everything the resource has".
    """
    key = api_key()
    records: list[dict] = []
    offset = 0

    while True:
        want = PAGE_SIZE if limit is None else min(PAGE_SIZE, limit - len(records))
        if want <= 0:
            break
        query = urllib.parse.urlencode(
            {"api-key": key, "format": "json", "limit": want, "offset": offset}
        )
        payload = _get(f"{API_ROOT}/{resource_id}?{query}")
        page = payload.get("records") or []
        records.extend(page)
        if len(page) < want:
            break  # last page
        offset += len(page)

    return records


# --- field mapping -------------------------------------------------------
#
# OGD publishers are not consistent about column names across datasets, so we
# match on a set of known aliases rather than hard-coding one spelling. Unknown
# columns are ignored, and a record missing a required field is skipped by the
# caller rather than silently producing a half-built row.

STATION_ALIASES = {
    "code": ("station_code", "code", "stn_code", "station code"),
    "name": ("station_name", "name", "stn_name", "station name"),
    "state": ("state", "state_name", "state ut", "state/ut"),
    "lat": ("latitude", "lat", "y"),
    "lon": ("longitude", "lon", "long", "lng", "x"),
}

TRAIN_ALIASES = {
    "train_number": ("train_number", "train_no", "train no", "number"),
    "train_name": ("train_name", "name", "train name"),
    "source": ("source_station_code", "from_station_code", "source", "from"),
    "destination": ("destination_station_code", "to_station_code", "destination", "to"),
    "dep_time": ("departure_time", "dep_time", "departure", "std"),
    "arr_time": ("arrival_time", "arr_time", "arrival", "sta"),
    "distance": ("distance", "distance_km", "dist"),
}


def pick(record: dict, aliases: tuple[str, ...]):
    """First non-empty value in `record` whose key matches any alias.

    Keys are compared case-insensitively with spaces/underscores normalised,
    because OGD column names vary between "Station Code" and "station_code".
    """
    normalised = {
        str(k).strip().lower().replace(" ", "_"): v for k, v in record.items()
    }
    for alias in aliases:
        value = normalised.get(alias.replace(" ", "_"))
        if value not in (None, ""):
            return value
    return None


def normalise_stations(records: list[dict]) -> list[dict]:
    """OGD station records -> stations.csv rows. Skips unusable rows."""
    out = []
    for record in records:
        code = pick(record, STATION_ALIASES["code"])
        name = pick(record, STATION_ALIASES["name"])
        lat = pick(record, STATION_ALIASES["lat"])
        lon = pick(record, STATION_ALIASES["lon"])
        if not code or not name or lat is None or lon is None:
            continue
        try:
            lat_f, lon_f = float(lat), float(lon)
        except (TypeError, ValueError):
            continue
        # a station at 0,0 is a null island placeholder, not a real location
        if lat_f == 0 and lon_f == 0:
            continue
        out.append(
            {
                "code": str(code).strip().upper(),
                "name": str(name).strip(),
                "state": str(pick(record, STATION_ALIASES["state"]) or "").strip(),
                "lat": f"{lat_f:.4f}",
                "lon": f"{lon_f:.4f}",
            }
        )
    return out


def normalise_routes(records: list[dict], fare_per_km: float = 1.1) -> list[dict]:
    """OGD train records -> routes.csv rows. Skips unusable rows.

    Fares are still estimated from distance: the OGD train datasets publish
    schedules, not fares.
    """
    out = []
    for record in records:
        source = pick(record, TRAIN_ALIASES["source"])
        destination = pick(record, TRAIN_ALIASES["destination"])
        dep = pick(record, TRAIN_ALIASES["dep_time"])
        arr = pick(record, TRAIN_ALIASES["arr_time"])
        if not source or not destination or not dep or not arr:
            continue

        dep_hhmm, arr_hhmm = _hhmm(dep), _hhmm(arr)
        if not dep_hhmm or not arr_hhmm:
            continue

        duration = _duration_min(dep_hhmm, arr_hhmm)
        distance = pick(record, TRAIN_ALIASES["distance"])
        try:
            cost = round(float(distance) * fare_per_km, -1) if distance else 0.0
        except (TypeError, ValueError):
            cost = 0.0

        out.append(
            {
                "source": str(source).strip().upper(),
                "destination": str(destination).strip().upper(),
                "mode": "train",
                "duration_min": duration,
                "cost_inr": cost,
                "train_number": str(pick(record, TRAIN_ALIASES["train_number"]) or "").strip(),
                "train_name": str(pick(record, TRAIN_ALIASES["train_name"]) or "").strip(),
                "available": "true",
                "date": "",
                "dep_time": dep_hhmm,
                "arr_time": arr_hhmm,
                "valid_from": "",
                "valid_to": "",
            }
        )
    return out


def _hhmm(value) -> str:
    """Coerce OGD time spellings ('9:5', '09:05:00', '0905') to HH:MM."""
    text = str(value).strip()
    if not text or text.lower() in {"na", "n/a", "-", "--"}:
        return ""
    if ":" in text:
        parts = text.split(":")
        try:
            hour, minute = int(parts[0]), int(parts[1])
        except (ValueError, IndexError):
            return ""
    elif text.isdigit() and len(text) in (3, 4):
        hour, minute = int(text[:-2]), int(text[-2:])
    else:
        return ""
    if not (0 <= hour < 24 and 0 <= minute < 60):
        return ""
    return f"{hour:02d}:{minute:02d}"


def _duration_min(dep: str, arr: str) -> int:
    """Minutes from dep to arr, rolling past midnight when arr <= dep."""
    dep_h, dep_m = (int(x) for x in dep.split(":"))
    arr_h, arr_m = (int(x) for x in arr.split(":"))
    minutes = (arr_h * 60 + arr_m) - (dep_h * 60 + dep_m)
    if minutes <= 0:
        minutes += 24 * 60
    return minutes
