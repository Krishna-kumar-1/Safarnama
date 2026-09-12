"""Refresh stations.csv / routes.csv from data.gov.in.

The bundled CSVs are the source of truth; this only overwrites them when a
fetch actually succeeds, and writes to a .new file first so a partial or
empty response can never clobber working data.

Usage:
    export DATA_GOV_IN_API_KEY=...
    python refresh_data.py --stations <resource-id>
    python refresh_data.py --trains   <resource-id>
    python refresh_data.py --stations <id> --trains <id> --apply

Without --apply it does a dry run: fetches, normalises, reports counts, and
writes nothing.
"""

import argparse
import csv
import sys
from pathlib import Path

from src.datagov import (
    DataGovError,
    MissingApiKey,
    fetch_resource,
    normalise_routes,
    normalise_stations,
)

DATA_DIR = Path(__file__).resolve().parent / "data"

STATION_COLUMNS = ["code", "name", "state", "lat", "lon"]
ROUTE_COLUMNS = [
    "source", "destination", "mode", "duration_min", "cost_inr",
    "train_number", "train_name", "available", "date",
    "dep_time", "arr_time", "valid_from", "valid_to",
]


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    staging = path.with_suffix(path.suffix + ".new")
    with open(staging, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    staging.replace(path)


def pull(label: str, resource_id: str, normalise, limit):
    print(f"fetching {label} from resource {resource_id} ...")
    raw = fetch_resource(resource_id, limit=limit)
    rows = normalise(raw)
    print(f"  {len(raw)} records fetched, {len(rows)} usable after normalising")
    if raw and not rows:
        print(f"  !! nothing usable -- the resource's columns may not match the")
        print(f"     aliases in src/datagov.py. First record's keys:")
        print(f"     {sorted(raw[0].keys())}")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stations", metavar="RESOURCE_ID", help="OGD station resource id")
    parser.add_argument("--trains", metavar="RESOURCE_ID", help="OGD train schedule resource id")
    parser.add_argument("--limit", type=int, default=None, help="cap records pulled (for testing)")
    parser.add_argument("--apply", action="store_true", help="actually overwrite the CSVs")
    args = parser.parse_args()

    if not args.stations and not args.trains:
        parser.error("give --stations and/or --trains with a resource id")

    try:
        station_rows = pull("stations", args.stations, normalise_stations, args.limit) if args.stations else None
        route_rows = pull("trains", args.trains, normalise_routes, args.limit) if args.trains else None
    except MissingApiKey as exc:
        print(f"\n{exc}\n", file=sys.stderr)
        print("Nothing changed -- the app keeps using the bundled CSVs.", file=sys.stderr)
        return 2
    except DataGovError as exc:
        print(f"\ndata.gov.in error: {exc}\n", file=sys.stderr)
        print("Nothing changed -- the app keeps using the bundled CSVs.", file=sys.stderr)
        return 1

    if not args.apply:
        print("\ndry run -- nothing written. Re-run with --apply to overwrite the CSVs.")
        return 0

    if station_rows:
        write_csv(DATA_DIR / "stations.csv", STATION_COLUMNS, station_rows)
        print(f"wrote data/stations.csv ({len(station_rows)} rows)")
    if route_rows:
        write_csv(DATA_DIR / "routes.csv", ROUTE_COLUMNS, route_rows)
        print(f"wrote data/routes.csv ({len(route_rows)} rows)")

    print("\nRun the tests -- they check the network is still fully connected:")
    print("  python -m unittest discover -s tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
