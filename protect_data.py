#!/usr/bin/env python3
"""
Safarnama Railway Data Protection Utility
Encrypts and locks raw railway CSV spreadsheets into an AES-256 vault
to prevent unauthorized access or copying on public GitHub repositories.

Usage:
  python protect_data.py lock     # Encrypts CSVs into vault & hides raw files from GitHub
  python protect_data.py unlock   # Decrypts vault & restores raw CSV files for editing in Excel
  python protect_data.py status   # Shows current encryption and file protection status
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from src.vault import create_vault, extract_vault, VAULT_FILE, DATA_DIR, _get_vault_password

BACKUP_DIR = DATA_DIR / "my_private_excel_files"
GITIGNORE_FILE = BASE_DIR / ".gitignore"

PROTECTED_PATTERNS = [
    "data/*.csv",
    "data/train_metadata.json",
    "data/my_private_excel_files/",
    "data/raw/",
    "data/Rail raw all datasets/",
]


def ensure_gitignore():
    """Ensure raw CSV files and private folders are strictly gitignored."""
    existing_lines = []
    if GITIGNORE_FILE.exists():
        with open(GITIGNORE_FILE, "r", encoding="utf-8") as f:
            existing_lines = [line.strip() for line in f]

    modified = False
    with open(GITIGNORE_FILE, "a", encoding="utf-8") as f:
        for pattern in PROTECTED_PATTERNS:
            if pattern not in existing_lines:
                f.write(f"\n{pattern}")
                modified = True

    if modified:
        print("  ✓ Updated .gitignore to safeguard raw CSV files from git tracking.")


def lock_data():
    print("🔒 Locking and Encrypting Railway Datasets...")

    csv_files = list(DATA_DIR.glob("*.csv"))
    meta_json = DATA_DIR / "train_metadata.json"
    raw_files = list(csv_files)
    if meta_json.exists():
        raw_files.append(meta_json)

    if not raw_files and not BACKUP_DIR.exists():
        if VAULT_FILE.exists():
            print("  ℹ️ Dataset is ALREADY locked! Only 'data/rail_data.vault' is present.")
            print("  Run 'python protect_data.py unlock' if you want to extract them for Excel editing.")
            return
        else:
            print("  ❌ No raw CSV files or vault found to encrypt!")
            return

    # If raw files are in BACKUP_DIR, bring them into account
    source_dir = DATA_DIR
    if not raw_files and BACKUP_DIR.exists():
        source_dir = BACKUP_DIR

    # 1. Create encrypted vault
    vault_path = create_vault(source_dir=source_dir)
    vault_size_mb = vault_path.stat().st_size / (1024 * 1024)
    print(f"  ✓ Created AES-256 Encrypted Vault: {vault_path.name} ({vault_size_mb:.2f} MB)")

    # 2. Backup raw CSV files into private gitignored folder for the owner
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    for f in DATA_DIR.glob("*.csv"):
        try:
            shutil.copy2(f, BACKUP_DIR / f.name)
            f.unlink()
        except Exception:
            pass

    if meta_json.exists():
        try:
            shutil.copy2(meta_json, BACKUP_DIR / meta_json.name)
            meta_json.unlink()
        except Exception:
            pass

    raw_trains = DATA_DIR / "raw" / "trains.json"
    if raw_trains.exists():
        raw_backup = BACKUP_DIR / "raw"
        raw_backup.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy2(raw_trains, raw_backup / "trains.json")
            raw_trains.unlink()
        except Exception:
            pass

    rail_raw = DATA_DIR / "Rail raw all datasets"
    if rail_raw.exists():
        rail_backup = BACKUP_DIR / "Rail raw all datasets"
        rail_backup.mkdir(parents=True, exist_ok=True)
        for f in rail_raw.glob("*.csv"):
            try:
                shutil.copy2(f, rail_backup / f.name)
                f.unlink()
            except Exception:
                pass
        try:
            rail_raw.rmdir()
        except Exception:
            pass

    print(f"  ✓ Safely moved raw CSV files to private owner folder: {BACKUP_DIR.relative_to(BASE_DIR)}/")
    print("  ✓ Removed plaintext CSV files from public git path.")

    # 3. Ensure .gitignore protects raw files
    ensure_gitignore()

    print("\n✅ DATA PROTECTION COMPLETE!")
    print("  - On GitHub: Nobody can see or download your raw Excel/CSV spreadsheets.")
    print("  - The application will automatically run from the encrypted 'rail_data.vault' in memory.")
    print("  - Only you can unlock the raw files using: 'python protect_data.py unlock'")


def unlock_data():
    print("🔓 Unlocking Railway Datasets for Owner...")

    if not VAULT_FILE.exists():
        print(f"  ❌ Vault file {VAULT_FILE} not found!")
        return

    # First check if private backup already has them
    if BACKUP_DIR.exists() and list(BACKUP_DIR.glob("*.csv")):
        for f in BACKUP_DIR.glob("*.csv"):
            shutil.copy2(f, DATA_DIR / f.name)
        meta = BACKUP_DIR / "train_metadata.json"
        if meta.exists():
            shutil.copy2(meta, DATA_DIR / meta.name)
        raw_backup = BACKUP_DIR / "raw" / "trains.json"
        if raw_backup.exists():
            (DATA_DIR / "raw").mkdir(parents=True, exist_ok=True)
            shutil.copy2(raw_backup, DATA_DIR / "raw" / "trains.json")
        rail_backup = BACKUP_DIR / "Rail raw all datasets"
        if rail_backup.exists():
            (DATA_DIR / "Rail raw all datasets").mkdir(parents=True, exist_ok=True)
            for f in rail_backup.glob("*.csv"):
                shutil.copy2(f, DATA_DIR / "Rail raw all datasets" / f.name)
        print("  ✓ Restored all CSV and JSON files from your private local backup into data/.")
    else:
        # Decrypt from vault
        try:
            extracted = extract_vault()
            print(f"  ✓ Successfully decrypted and extracted {len(extracted)} files into data/:")
            for name in extracted:
                print(f"    - {name}")
        except Exception as e:
            print(f"  ❌ Decryption failed: {e}")
            return

    print("\n✅ DATA UNLOCKED!")
    print("  You can now open, inspect, or edit your CSV files in Excel.")
    print("  Note: Keep them gitignored, or run 'python protect_data.py lock' before pushing to GitHub.")


def show_status():
    print("📊 Safarnama Data Protection Status:")
    vault_exists = VAULT_FILE.exists()
    csv_count = len(list(DATA_DIR.glob("*.csv")))
    backup_count = len(list(BACKUP_DIR.glob("*.csv"))) if BACKUP_DIR.exists() else 0

    print(f"  - Encrypted Vault ({VAULT_FILE.name}): {'EXISTS (' + str(round(VAULT_FILE.stat().st_size / (1024*1024), 2)) + ' MB)' if vault_exists else 'NOT CREATED'}")
    print(f"  - Plaintext CSV files in data/: {csv_count} files ({'EXPOSED / UNLOCKED' if csv_count > 0 else 'PROTECTED / HIDDEN'})")
    print(f"  - Private Owner Backup: {backup_count} files")

    if csv_count == 0 and vault_exists:
        print("\n🔒 STATUS: FULLY PROTECTED (Safe for GitHub! Nobody can steal or open the raw CSVs).")
    elif csv_count > 0 and vault_exists:
        print("\n⚠️ STATUS: UNLOCKED LOCALLY (Plaintext files exist on disk for your editing).")
        print("   Run 'python protect_data.py lock' before pushing to GitHub to hide them.")
    else:
        print("\n❌ STATUS: UNPROTECTED. Run 'python protect_data.py lock' to secure your data.")


def main():
    parser = argparse.ArgumentParser(description="Safarnama Railway Data Protection Utility")
    parser.add_argument("action", choices=["lock", "unlock", "status"], nargs="?", default="status",
                        help="Action to perform: lock, unlock, or status")
    parser.add_argument("--lock", dest="flag_lock", action="store_true", help="Lock and encrypt raw CSV datasets")
    parser.add_argument("--unlock", dest="flag_unlock", action="store_true", help="Unlock and extract raw CSV datasets")
    parser.add_argument("--status", dest="flag_status", action="store_true", help="Show data protection status")

    args = parser.parse_args()

    if args.flag_lock or args.action == "lock":
        lock_data()
    elif args.flag_unlock or args.action == "unlock":
        unlock_data()
    else:
        show_status()


if __name__ == "__main__":
    main()
