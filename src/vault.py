"""
Safarnama Encrypted Railway Data Vault
Secures and protects raw railway timetable Excel/CSV and GeoJSON files with AES-256-GCM.
Allows seamless in-memory loading without exposing plaintext datasets on GitHub.
"""

import io
import json
import logging
import os
import zipfile
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger("safarnama.vault")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
VAULT_FILE = DATA_DIR / "rail_data.vault"

# Default Derivation Secret - Can be overridden via SAFARNAMA_DATA_KEY in .env
DEFAULT_VAULT_KEY = "Safarnama_Rail_Master_Vault_Key_2026_Secure"

_IN_MEMORY_VAULT: Optional[Dict[str, str]] = None


def _get_vault_password() -> str:
    """Retrieve vault password from environment variable or .env file."""
    key = os.getenv("SAFARNAMA_DATA_KEY", "").strip()
    if key:
        return key

    # Try loading from .env
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if env_file.exists():
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("SAFARNAMA_DATA_KEY="):
                        val = line.split("=", 1)[1].strip().strip('"').strip("'")
                        if val:
                            return val
        except Exception:
            pass

    return DEFAULT_VAULT_KEY


def _derive_aes_key(password: str, salt: bytes) -> bytes:
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode("utf-8"))


def create_vault(password: Optional[str] = None, vault_path: Optional[Path] = None, source_dir: Optional[Path] = None) -> Path:
    """
    Compresses and encrypts all raw CSV, JSON, and GeoJSON files in data/ into a secure AES-256 vault.
    """
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    pwd = password or _get_vault_password()
    v_path = vault_path or VAULT_FILE
    s_dir = source_dir or DATA_DIR

    files_to_pack = []
    # 1. All root CSVs
    for f in s_dir.glob("*.csv"):
        files_to_pack.append((f, f.name))

    # 2. train_metadata.json
    meta_json = s_dir / "train_metadata.json"
    if meta_json.exists():
        files_to_pack.append((meta_json, "train_metadata.json"))

    # 3. raw/trains.json
    raw_trains = s_dir / "raw" / "trains.json"
    if raw_trains.exists():
        files_to_pack.append((raw_trains, "raw/trains.json"))

    # 4. Rail raw all datasets (user raw excel/csv collection)
    for raw_folder in [s_dir / "Rail raw all datasets", DATA_DIR / "Rail raw all datasets"]:
        if raw_folder.exists():
            for f in raw_folder.glob("*.csv"):
                arc = f"Rail raw all datasets/{f.name}"
                if not any(x[1] == arc for x in files_to_pack):
                    files_to_pack.append((f, arc))

    if not files_to_pack:
        raise ValueError(f"No CSV, JSON, or GeoJSON files found in {s_dir} to encrypt!")

    # Compress into in-memory zip
    zip_buf = io.BytesIO()
    with zipfile.ZipFile(zip_buf, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for file_path, arcname in sorted(files_to_pack, key=lambda x: x[1]):
            zf.write(file_path, arcname=arcname)
    plaintext = zip_buf.getvalue()

    # Encrypt with AES-256-GCM
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = _derive_aes_key(pwd, salt)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    # Write vault: [16 bytes salt] + [12 bytes nonce] + [ciphertext]
    v_path.parent.mkdir(parents=True, exist_ok=True)
    with open(v_path, "wb") as f:
        f.write(salt + nonce + ciphertext)

    logger.info(f"Encrypted {len(files_to_pack)} files into {v_path} ({len(salt + nonce + ciphertext)} bytes)")
    return v_path


def load_vault_files(password: Optional[str] = None, vault_path: Optional[Path] = None) -> Dict[str, str]:
    """
    Decrypts the vault in memory and returns a dictionary of { filename: content_string }.
    Does NOT write plaintext files to disk.
    """
    global _IN_MEMORY_VAULT
    if _IN_MEMORY_VAULT is not None:
        return _IN_MEMORY_VAULT

    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    v_path = vault_path or VAULT_FILE
    if not v_path.exists():
        return {}

    pwd = password or _get_vault_password()

    with open(v_path, "rb") as f:
        vault_data = f.read()

    if len(vault_data) < 28:
        raise ValueError(f"Vault file {v_path} is corrupt or invalid.")

    salt = vault_data[:16]
    nonce = vault_data[16:28]
    ciphertext = vault_data[28:]

    key = _derive_aes_key(pwd, salt)
    aesgcm = AESGCM(key)

    try:
        decrypted_zip = aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        if pwd != DEFAULT_VAULT_KEY:
            try:
                fallback_key = _derive_aes_key(DEFAULT_VAULT_KEY, salt)
                decrypted_zip = AESGCM(fallback_key).decrypt(nonce, ciphertext, None)
            except Exception:
                raise ValueError("Incorrect Safarnama vault password or corrupted data file!") from e
        else:
            raise ValueError("Incorrect Safarnama vault password or corrupted data file!") from e

    # Extract into memory string dict
    file_map = {}
    with zipfile.ZipFile(io.BytesIO(decrypted_zip), "r") as zf:
        for name in zf.namelist():
            file_map[name] = zf.read(name).decode("utf-8")

    _IN_MEMORY_VAULT = file_map
    return file_map


def extract_vault(password: Optional[str] = None, vault_path: Optional[Path] = None, target_dir: Optional[Path] = None) -> List[str]:
    """
    Decrypts the vault and restores all original CSV/JSON files to disk.
    Used by the repository owner to view, edit, or manage raw spreadsheets.
    """
    t_dir = target_dir or DATA_DIR
    t_dir.mkdir(parents=True, exist_ok=True)

    file_map = load_vault_files(password, vault_path)
    extracted = []
    for arcname, content in file_map.items():
        dest = t_dir / arcname
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(content)
        extracted.append(arcname)

    return extracted
