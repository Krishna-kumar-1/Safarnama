import io
import unittest
from pathlib import Path
from src.vault import create_vault, load_vault_files, extract_vault, VAULT_FILE, DATA_DIR


class TestVault(unittest.TestCase):
    def test_vault_file_exists_and_decrypts(self):
        # Vault file must exist
        self.assertTrue(VAULT_FILE.exists(), "rail_data.vault must exist in data/")
        self.assertGreater(VAULT_FILE.stat().st_size, 1000000, "Vault must be over 1MB")

        # In-memory decrypt
        files = load_vault_files()
        self.assertIn("stations.csv", files)
        self.assertIn("routes.csv", files)
        self.assertIn("train_metadata.json", files)
        self.assertIn("raw/trains.json", files)

        # Content must be valid CSV and JSON
        self.assertTrue(files["stations.csv"].startswith("code,name"))
        self.assertTrue(files["routes.csv"].startswith("source,destination"))
        self.assertTrue(files["train_metadata.json"].startswith("{"))

    def test_stations_load_from_vault_when_csv_absent(self):
        from src.data_loader import load_stations, load_routes
        # Even without physical CSV on disk, load_stations and load_routes work
        stations = load_stations(DATA_DIR / "non_existent_stations.csv")
        self.assertGreater(len(stations), 1000)

        routes = load_routes(DATA_DIR / "non_existent_routes.csv")
        self.assertGreater(len(routes), 5000)


if __name__ == "__main__":
    unittest.main()
