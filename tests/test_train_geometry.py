import unittest
from unittest.mock import patch
from pathlib import Path
from src.route_engine import RouteEngine
from src.train_geometry import (
    load_train_geometries,
    get_train_leg_geometry,
    _closest_coord_index,
    _resolve_station_coords,
    _TRAIN_LINESTRINGS,
)
from app import app


class TestTrainGeometry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = RouteEngine()
        cls.client = app.test_client()
        load_train_geometries()

    def test_load_train_geometries(self):
        # Must load thousands of train track LineStrings
        self.assertGreater(len(_TRAIN_LINESTRINGS), 1000)

    def test_closest_coord_index(self):
        coords = [[80.3510, 26.4542], [81.8600, 25.3931], [86.4289, 23.7909]]
        # Point right at Kanpur
        idx = _closest_coord_index(coords, 26.4542, 80.3510)
        self.assertEqual(idx, 0)
        # Point right at Dhanbad
        idx2 = _closest_coord_index(coords, 23.7909, 86.4289)
        self.assertEqual(idx2, 2)

    def test_resolve_station_coords_with_aliases(self):
        # MBDP should resolve via PBH alias
        coords = _resolve_station_coords("MBDP", self.engine.stations)
        self.assertIsNotNone(coords)
        self.assertAlmostEqual(coords[0], 25.91331, places=3)

        # Standard station CNB
        coords_cnb = _resolve_station_coords("CNB", self.engine.stations)
        self.assertIsNotNone(coords_cnb)
        self.assertAlmostEqual(coords_cnb[0], 26.45424, places=3)

    def test_slice_train_geometry_kanpur_to_dhanbad(self):
        # Train 12302 (Rajdhani Express) CNB -> DHN
        pts, is_real = get_train_leg_geometry("12302", "CNB", "DHN", self.engine.stations)
        self.assertTrue(is_real)
        # Real track path contains over 50 curving waypoints
        self.assertGreater(len(pts), 50)
        # Snapped precisely to Kanpur and Dhanbad platforms
        self.assertAlmostEqual(pts[0][0], self.engine.stations["CNB"].lat, places=4)
        self.assertAlmostEqual(pts[0][1], self.engine.stations["CNB"].lon, places=4)
        self.assertAlmostEqual(pts[-1][0], self.engine.stations["DHN"].lat, places=4)
        self.assertAlmostEqual(pts[-1][1], self.engine.stations["DHN"].lon, places=4)

    def test_slice_train_geometry_reverse_direction(self):
        # Train 12302 in reverse direction: DHN -> CNB
        pts, is_real = get_train_leg_geometry("12302", "DHN", "CNB", self.engine.stations)
        self.assertTrue(is_real)
        self.assertGreater(len(pts), 50)
        # First point must be DHN, last point CNB
        self.assertAlmostEqual(pts[0][0], self.engine.stations["DHN"].lat, places=4)
        self.assertAlmostEqual(pts[-1][0], self.engine.stations["CNB"].lat, places=4)

    def test_slice_train_geometry_jasidih_area(self):
        # Train 12304 (Poorva Express) JSME -> MDP
        pts, is_real = get_train_leg_geometry("12304", "JSME", "MDP", self.engine.stations)
        self.assertTrue(is_real)
        self.assertGreaterEqual(len(pts), 2)
        self.assertAlmostEqual(pts[0][0], self.engine.stations["JSME"].lat, places=4)
        self.assertAlmostEqual(pts[-1][0], self.engine.stations["MDP"].lat, places=4)

    def test_fallback_for_unknown_train(self):
        # Non-existent train number should return 2-point straight line with is_real=False
        pts, is_real = get_train_leg_geometry("9999999", "JSME", "MDP", self.engine.stations)
        self.assertFalse(is_real)
        self.assertEqual(len(pts), 2)
        self.assertAlmostEqual(pts[0][0], self.engine.stations["JSME"].lat, places=4)
        self.assertAlmostEqual(pts[-1][0], self.engine.stations["MDP"].lat, places=4)

    def test_api_route_includes_track_geometry(self):
        res = self.client.get("/api/route?source=CNB&destination=DHN")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        sim = data.get("simplest")
        self.assertIsNotNone(sim)
        leg = sim["legs"][0]
        self.assertIn("track_geometry", leg)
        self.assertIn("is_real_geometry", leg)
        self.assertTrue(leg["is_real_geometry"])
        self.assertGreater(len(leg["track_geometry"]), 50)


if __name__ == "__main__":
    unittest.main()
