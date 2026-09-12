import os
import unittest
from unittest import mock

from src.datagov import (
    MissingApiKey,
    _duration_min,
    _hhmm,
    api_key,
    normalise_routes,
    normalise_stations,
    pick,
)


class TestFieldMatching(unittest.TestCase):
    def test_pick_is_case_and_separator_insensitive(self):
        # OGD publishers spell the same column several ways
        self.assertEqual(pick({"Station Code": "DHN"}, ("station_code",)), "DHN")
        self.assertEqual(pick({"STATION_CODE": "DHN"}, ("station_code",)), "DHN")
        self.assertEqual(pick({"station code": "DHN"}, ("station_code",)), "DHN")

    def test_pick_falls_through_to_later_aliases(self):
        self.assertEqual(pick({"stn_code": "RNC"}, ("station_code", "code", "stn_code")), "RNC")

    def test_pick_skips_empty_values(self):
        self.assertIsNone(pick({"code": ""}, ("code",)))
        self.assertIsNone(pick({}, ("code",)))


class TestTimeParsing(unittest.TestCase):
    def test_hhmm_normalises_spellings(self):
        self.assertEqual(_hhmm("9:5"), "09:05")
        self.assertEqual(_hhmm("09:05:00"), "09:05")
        self.assertEqual(_hhmm("0905"), "09:05")
        self.assertEqual(_hhmm("905"), "09:05")

    def test_hhmm_rejects_junk(self):
        for junk in ("", "NA", "n/a", "-", "--", "banana", "25:00", "09:75"):
            self.assertEqual(_hhmm(junk), "", f"should reject {junk!r}")

    def test_duration_rolls_past_midnight(self):
        self.assertEqual(_duration_min("09:00", "17:30"), 510)
        self.assertEqual(_duration_min("23:00", "01:30"), 150)  # next day
        self.assertEqual(_duration_min("10:00", "10:00"), 1440)  # full 24h, not 0


class TestNormaliseStations(unittest.TestCase):
    def test_maps_a_well_formed_record(self):
        rows = normalise_stations([
            {"station_code": "dhn", "station_name": " Dhanbad Jn ",
             "state": "Jharkhand", "latitude": "23.7957", "longitude": "86.4304"}
        ])
        self.assertEqual(rows, [{
            "code": "DHN", "name": "Dhanbad Jn", "state": "Jharkhand",
            "lat": "23.7957", "lon": "86.4304",
        }])

    def test_skips_records_missing_required_fields(self):
        self.assertEqual(normalise_stations([{"station_code": "DHN"}]), [])
        self.assertEqual(normalise_stations([{"station_name": "Dhanbad"}]), [])

    def test_skips_null_island_placeholders(self):
        rows = normalise_stations([
            {"station_code": "X", "station_name": "Nowhere", "latitude": "0", "longitude": "0"}
        ])
        self.assertEqual(rows, [])

    def test_skips_non_numeric_coordinates(self):
        rows = normalise_stations([
            {"station_code": "X", "station_name": "Bad", "latitude": "abc", "longitude": "1"}
        ])
        self.assertEqual(rows, [])


class TestNormaliseRoutes(unittest.TestCase):
    def test_maps_a_well_formed_record(self):
        rows = normalise_routes([{
            "train_no": "12301", "train_name": "Rajdhani Express",
            "source_station_code": "hwh", "destination_station_code": "ndls",
            "departure_time": "16:50", "arrival_time": "10:05", "distance": "1451",
        }])
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["source"], "HWH")
        self.assertEqual(row["destination"], "NDLS")
        self.assertEqual(row["dep_time"], "16:50")
        self.assertEqual(row["arr_time"], "10:05")
        self.assertEqual(row["duration_min"], 1035)  # rolls past midnight
        self.assertEqual(row["cost_inr"], 1600.0)    # 1451km * 1.1, rounded to 10
        self.assertEqual(row["mode"], "train")
        self.assertEqual(row["available"], "true")

    def test_skips_records_missing_endpoints_or_times(self):
        self.assertEqual(normalise_routes([{"source": "A", "destination": "B"}]), [])
        self.assertEqual(
            normalise_routes([{"source": "A", "departure_time": "10:00", "arrival_time": "11:00"}]),
            [],
        )

    def test_missing_distance_yields_zero_fare_not_a_crash(self):
        rows = normalise_routes([{
            "source": "A", "destination": "B",
            "departure_time": "10:00", "arrival_time": "11:00",
        }])
        self.assertEqual(rows[0]["cost_inr"], 0.0)

    def test_emitted_columns_match_the_csv_schema(self):
        from refresh_data import ROUTE_COLUMNS
        rows = normalise_routes([{
            "source": "A", "destination": "B",
            "departure_time": "10:00", "arrival_time": "11:00",
        }])
        self.assertEqual(sorted(rows[0].keys()), sorted(ROUTE_COLUMNS))

    def test_emitted_station_columns_match_the_csv_schema(self):
        from refresh_data import STATION_COLUMNS
        rows = normalise_stations([{
            "station_code": "A", "station_name": "A", "state": "S",
            "latitude": "1.0", "longitude": "2.0",
        }])
        self.assertEqual(sorted(rows[0].keys()), sorted(STATION_COLUMNS))


class TestApiKey(unittest.TestCase):
    def test_missing_key_raises_with_actionable_message(self):
        with mock.patch.dict(os.environ, {"DATA_GOV_IN_API_KEY": ""}, clear=False):
            with self.assertRaises(MissingApiKey) as ctx:
                api_key()
        self.assertIn("data.gov.in/user/register", str(ctx.exception))

    def test_key_is_read_and_stripped(self):
        with mock.patch.dict(os.environ, {"DATA_GOV_IN_API_KEY": "  abc123  "}, clear=False):
            self.assertEqual(api_key(), "abc123")


if __name__ == "__main__":
    unittest.main()
