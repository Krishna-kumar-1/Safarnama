import unittest
from unittest.mock import patch, MagicMock
from app import app
from src.track_geometry import get_exact_track_geometry, _coord_cache_key, _IN_MEMORY_CACHE


class TestTrackGeometry(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        from src.track_geometry import _load_cache
        _load_cache()

    def test_empty_and_single_point(self):
        self.assertEqual(get_exact_track_geometry([]), [])
        self.assertEqual(get_exact_track_geometry([[26.45, 80.35]]), [[26.45, 80.35]])

    def test_deduplication_of_adjacent_points(self):
        pts = [[26.4538, 80.3513], [26.4538, 80.3513]]
        # Points are identical (<10m apart), should collapse to 1 point and return safely
        res = get_exact_track_geometry(pts)
        self.assertEqual(len(res), 1)

    def test_cache_retrieval(self):
        test_pts = [[10.1111, 20.2222], [10.3333, 20.4444]]
        cache_key = _coord_cache_key(test_pts)
        mock_snapped = [[10.1111, 20.2222], [10.2222, 20.3333], [10.3333, 20.4444]]
        _IN_MEMORY_CACHE[cache_key] = mock_snapped

        result = get_exact_track_geometry(test_pts)
        self.assertEqual(result, mock_snapped)

    @patch("urllib.request.urlopen")
    def test_brouter_fetch_success(self, mock_urlopen):
        import io, json
        sample_geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [80.3513, 26.4538, 120.0],
                        [80.3600, 26.4600, 121.0],
                        [80.8252, 25.9284, 115.0]
                    ]
                }
            }]
        }
        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps(sample_geojson).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_resp

        pts = [[26.4538, 80.3513], [25.9284, 80.8252]]
        # Invalidate any cache for test
        cache_key = _coord_cache_key(pts)
        if cache_key in _IN_MEMORY_CACHE:
            del _IN_MEMORY_CACHE[cache_key]

        res = get_exact_track_geometry(pts)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], [26.4538, 80.3513])
        self.assertEqual(res[1], [26.4600, 80.3600])
        self.assertEqual(res[2], [25.9284, 80.8252])

    @patch("urllib.request.urlopen", side_effect=Exception("Network error"))
    def test_fallback_on_network_error(self, mock_urlopen):
        pts = [[26.4538, 80.3513], [25.4484, 81.8333]]
        # Invalidate cache for test
        cache_key = _coord_cache_key(pts)
        if cache_key in _IN_MEMORY_CACHE:
            del _IN_MEMORY_CACHE[cache_key]

        res = get_exact_track_geometry(pts)
        # Should gracefully return the original stations
        self.assertEqual(len(res), 2)
        self.assertAlmostEqual(res[0][0], 26.4538, places=4)
        self.assertAlmostEqual(res[1][0], 25.4484, places=4)

    def test_api_endpoint_track_geometry(self):
        # Empty points
        res = self.client.post("/api/track/geometry", json={"points": []})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "ok")
        self.assertFalse(data["snapped"])

        # Valid cached or queried route
        test_pts = [[11.1111, 22.2222], [11.3333, 22.4444]]
        cache_key = _coord_cache_key(test_pts)
        _IN_MEMORY_CACHE[cache_key] = [[11.1111, 22.2222], [11.2, 22.3], [11.3333, 22.4444]]

        res = self.client.post("/api/track/geometry", json={"points": test_pts})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "ok")
        self.assertTrue(data["snapped"])
        self.assertEqual(data["count"], 3)


if __name__ == "__main__":
    unittest.main()
