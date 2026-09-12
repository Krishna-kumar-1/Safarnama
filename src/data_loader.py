import csv
from pathlib import Path

from .models import RouteLeg, Station

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


# Companion CSVs merged on top of the base network, in order. Later files win
# on a duplicate station code, so hand-curated rows keep their coordinates.
#   specials -- seasonal special-fare trains, kept separate so the year-round
#               base network stays readable and separately editable
#   iri      -- bulk timetable import (import_iri.py)
#   rr       -- RailRadar API: halt-to-halt legs, run days, real coordinates
EXTRA_SUFFIXES = ("rr", "iri", "specials", "extra")


def _extra_file(path: Path, suffix: str) -> Path | None:
    """Companion '<name>_<suffix>.csv' beside the given file, if it exists."""
    candidate = path.with_name(f"{path.stem}_{suffix}{path.suffix}")
    return candidate if candidate.exists() else None


def _sources(path: Path, extras=EXTRA_SUFFIXES):
    yield path
    for suffix in extras:
        extra = _extra_file(path, suffix)
        if extra is not None:
            yield extra


def _coord(value: str) -> float | None:
    """Blank cell -> None. Imported stations have no published coordinates."""
    value = (value or "").strip()
    return float(value) if value else None


# Comprehensive State Mapping for Indian Railway Stations
STATION_STATE_MAP = {
    # Uttar Pradesh
    "LKO": "Uttar Pradesh", "LJN": "Uttar Pradesh", "CNB": "Uttar Pradesh", "GOY": "Uttar Pradesh",
    "PRYJ": "Uttar Pradesh", "ALD": "Uttar Pradesh", "BSB": "Uttar Pradesh", "BNRS": "Uttar Pradesh",
    "GKP": "Uttar Pradesh", "AY": "Uttar Pradesh", "AYC": "Uttar Pradesh", "AGC": "Uttar Pradesh",
    "AF": "Uttar Pradesh", "MTJ": "Uttar Pradesh", "MTC": "Uttar Pradesh", "SRE": "Uttar Pradesh",
    "GZB": "Uttar Pradesh", "MB": "Uttar Pradesh", "BE": "Uttar Pradesh", "ALJN": "Uttar Pradesh",
    "TDL": "Uttar Pradesh", "ETW": "Uttar Pradesh", "FBD": "Uttar Pradesh", "JHS": "Uttar Pradesh",
    "VGLJ": "Uttar Pradesh", "BUI": "Uttar Pradesh", "MAU": "Uttar Pradesh", "ARJ": "Uttar Pradesh",
    "SPN": "Uttar Pradesh", "HRI": "Uttar Pradesh", "BLP": "Uttar Pradesh", "GD": "Uttar Pradesh",
    "BST": "Uttar Pradesh", "DEOS": "Uttar Pradesh", "MZP": "Uttar Pradesh", "DDU": "Uttar Pradesh",
    "MGS": "Uttar Pradesh", "GTNR": "Uttar Pradesh", "ASH": "Uttar Pradesh", "BNZ": "Uttar Pradesh",
    "BLM": "Uttar Pradesh", "SAN": "Uttar Pradesh", "KLD": "Uttar Pradesh", "JNU": "Uttar Pradesh",
    "SLN": "Uttar Pradesh", "RBL": "Uttar Pradesh", "UCR": "Uttar Pradesh", "AME": "Uttar Pradesh",
    "PBH": "Uttar Pradesh", "FD": "Uttar Pradesh", "BBK": "Uttar Pradesh", "ABP": "Uttar Pradesh",
    
    # Bihar
    "PNBE": "Bihar", "PPTA": "Bihar", "DNR": "Bihar", "RJPB": "Bihar", "GAYA": "Bihar",
    "MKA": "Bihar", "BKP": "Bihar", "KIUL": "Bihar", "JAJ": "Bihar", "JMP": "Bihar",
    "BGP": "Bihar", "KGG": "Bihar", "MNE": "Bihar", "NNA": "Bihar", "KIR": "Bihar",
    "KNE": "Bihar", "SHC": "Bihar", "DBG": "Bihar", "SPJ": "Bihar", "MFP": "Bihar",
    "HJP": "Bihar", "SEE": "Bihar", "BJU": "Bihar", "SMI": "Bihar", "RXL": "Bihar",
    "NKE": "Bihar", "BUG": "Bihar", "JYG": "Bihar", "THE": "Bihar", "JBN": "Bihar",
    "SV": "Bihar", "CPR": "Bihar", "ARA": "Bihar", "BXR": "Bihar", "DLN": "Bihar",
    
    # Jharkhand
    "DHN": "Jharkhand", "GMO": "Jharkhand", "PNME": "Jharkhand", "KQR": "Jharkhand",
    "HZD": "Jharkhand", "JSME": "Jharkhand", "MDP": "Jharkhand", "CRJ": "Jharkhand",
    "TATA": "Jharkhand", "CKP": "Jharkhand", "RNC": "Jharkhand", "HTE": "Jharkhand",
    "MURI": "Jharkhand", "BKSC": "Jharkhand", "CRP": "Jharkhand", "BRKA": "Jharkhand",
    "DTO": "Jharkhand", "GHD": "Jharkhand", "DGHR": "Jharkhand", "KNDN": "Jharkhand",
    "BNDM": "Odisha", "ROU": "Odisha", "JSG": "Odisha",
    
    # West Bengal
    "HWH": "West Bengal", "SDAH": "West Bengal", "KOAA": "West Bengal", "SHM": "West Bengal",
    "SRC": "West Bengal", "KGP": "West Bengal", "BWN": "West Bengal", "DGR": "West Bengal",
    "ASN": "West Bengal", "RNG": "West Bengal", "UDL": "West Bengal", "STN": "West Bengal",
    "MLDT": "West Bengal", "NFK": "West Bengal", "NJP": "West Bengal", "SGUJ": "West Bengal",
    "APDJ": "West Bengal", "NOQ": "West Bengal", "BOE": "Bihar",
    
    # Delhi & NCR
    "NDLS": "Delhi", "DLI": "Delhi", "NZM": "Delhi", "ANVT": "Delhi", "DEC": "Delhi",
    "DEE": "Delhi", "DSA": "Delhi", "SSB": "Delhi", "FDB": "Haryana", "GGN": "Haryana",
    
    # Maharashtra
    "CSMT": "Maharashtra", "MMCT": "Maharashtra", "LTT": "Maharashtra", "BDTS": "Maharashtra",
    "BCT": "Maharashtra", "DR": "Maharashtra", "TNA": "Maharashtra", "KYN": "Maharashtra",
    "KJT": "Maharashtra", "LNL": "Maharashtra", "PUNE": "Maharashtra", "DD": "Maharashtra",
    "SUR": "Maharashtra", "KWV": "Maharashtra", "PVR": "Maharashtra", "MRJ": "Maharashtra",
    "KOP": "Maharashtra", "IGP": "Maharashtra", "NK": "Maharashtra", "MMR": "Maharashtra",
    "CSN": "Maharashtra", "JL": "Maharashtra", "BSL": "Maharashtra", "MKU": "Maharashtra",
    "SEG": "Maharashtra", "AK": "Maharashtra", "MZR": "Maharashtra", "BD": "Maharashtra",
    "DMN": "Maharashtra", "WR": "Maharashtra", "NGP": "Maharashtra", "AJNI": "Maharashtra",
    "NITR": "Maharashtra", "BPQ": "Maharashtra", "CD": "Maharashtra", "WRR": "Maharashtra",
    "SEGM": "Maharashtra", "NED": "Maharashtra", "PAU": "Maharashtra", "PBN": "Maharashtra",
    "J": "Maharashtra", "AWB": "Maharashtra", "SNSI": "Maharashtra",
    
    # Gujarat
    "ADI": "Gujarat", "SBIB": "Gujarat", "ASV": "Gujarat", "GNC": "Gujarat", "BRC": "Gujarat",
    "ANND": "Gujarat", "ND": "Gujarat", "ST": "Gujarat", "UDN": "Gujarat", "NVS": "Gujarat",
    "BL": "Gujarat", "VAPI": "Gujarat", "BH": "Gujarat", "MYG": "Gujarat", "RJT": "Gujarat",
    "HAPA": "Gujarat", "JAM": "Gujarat", "OKHA": "Gujarat", "DWK": "Gujarat", "SUNR": "Gujarat",
    "VG": "Gujarat", "GIMB": "Gujarat", "BHUJ": "Gujarat", "BVC": "Gujarat", "VRL": "Gujarat",
    "PBR": "Gujarat", "PNU": "Gujarat", "MSH": "Gujarat",
    
    # Rajasthan
    "JP": "Rajasthan", "GADJ": "Rajasthan", "DPA": "Rajasthan", "FL": "Rajasthan",
    "AII": "Rajasthan", "MDJN": "Rajasthan", "BER": "Rajasthan", "MJ": "Rajasthan",
    "FA": "Rajasthan", "ABR": "Rajasthan", "JU": "Rajasthan", "BME": "Rajasthan",
    "JSM": "Rajasthan", "BKN": "Rajasthan", "LGH": "Rajasthan", "NOK": "Rajasthan",
    "NGO": "Rajasthan", "DNA": "Rajasthan", "MTD": "Rajasthan", "KOTA": "Rajasthan",
    "SWM": "Rajasthan", "BTE": "Rajasthan", "BXN": "Rajasthan", "HAN": "Rajasthan",
    "GGC": "Rajasthan", "COR": "Rajasthan", "UDZ": "Rajasthan", "CNA": "Rajasthan",
    "BHL": "Rajasthan", "ALW": "Rajasthan", "RE": "Haryana", "AWR": "Rajasthan",
    
    # Madhya Pradesh
    "BPL": "Madhya Pradesh", "RKMP": "Madhya Pradesh", "HBJ": "Madhya Pradesh", "ET": "Madhya Pradesh",
    "HBD": "Madhya Pradesh", "INDB": "Madhya Pradesh", "DWX": "Madhya Pradesh", "UJN": "Madhya Pradesh",
    "NAD": "Madhya Pradesh", "RTM": "Madhya Pradesh", "MDS": "Madhya Pradesh", "NMH": "Madhya Pradesh",
    "GWL": "Madhya Pradesh", "MRA": "Madhya Pradesh", "DBA": "Madhya Pradesh", "JBP": "Madhya Pradesh",
    "MML": "Madhya Pradesh", "NU": "Madhya Pradesh", "GAR": "Madhya Pradesh", "PPI": "Madhya Pradesh",
    "KTE": "Madhya Pradesh", "MYR": "Madhya Pradesh", "STA": "Madhya Pradesh", "REWA": "Madhya Pradesh",
    "SGO": "Madhya Pradesh", "DMO": "Madhya Pradesh", "KMZ": "Madhya Pradesh", "BINA": "Madhya Pradesh",
    "LAR": "Madhya Pradesh", "BAQ": "Madhya Pradesh", "KURJ": "Madhya Pradesh", "MCSC": "Madhya Pradesh",
    "SHR": "Madhya Pradesh", "APR": "Madhya Pradesh", "SDL": "Madhya Pradesh", "UMR": "Madhya Pradesh",
    
    # Punjab & Haryana & Chandigarh & HP & J&K
    "ASR": "Punjab", "BEAS": "Punjab", "JUC": "Punjab", "PGW": "Punjab", "LDH": "Punjab",
    "KNN": "Punjab", "SIR": "Punjab", "RPJ": "Punjab", "UMB": "Haryana", "CDG": "Chandigarh",
    "KLK": "Haryana", "SML": "Himachal Pradesh", "AADR": "Himachal Pradesh", "UHL": "Himachal Pradesh",
    "FZR": "Punjab", "BTI": "Punjab", "ABS": "Punjab", "KKP": "Punjab", "FDK": "Punjab",
    "PTA": "Punjab", "DUI": "Punjab", "SAG": "Punjab", "JHL": "Haryana", "ROK": "Haryana",
    "BNW": "Haryana", "HSR": "Haryana", "SSA": "Haryana", "JIND": "Haryana", "PNP": "Haryana",
    "KUN": "Haryana", "KKDE": "Haryana", "JAT": "Jammu and Kashmir", "SVDK": "Jammu and Kashmir",
    "UHP": "Jammu and Kashmir", "MCTM": "Jammu and Kashmir", "SINA": "Jammu and Kashmir",
    "PTKC": "Punjab", "PTK": "Punjab",
    
    # Uttarakhand
    "DDN": "Uttarakhand", "HW": "Uttarakhand", "RK": "Uttarakhand", "KGM": "Uttarakhand",
    "HDW": "Uttarakhand", "LKU": "Uttarakhand", "RMR": "Uttarakhand", "TPU": "Uttarakhand",
    "YNRK": "Uttarakhand",
    
    # Telangana & Andhra Pradesh
    "SC": "Telangana", "HYB": "Telangana", "KCG": "Telangana", "LPI": "Telangana",
    "KZJ": "Telangana", "WL": "Telangana", "MABD": "Telangana", "KMT": "Telangana",
    "BZA": "Andhra Pradesh", "GNT": "Andhra Pradesh", "EE": "Andhra Pradesh", "TDD": "Andhra Pradesh",
    "RJY": "Andhra Pradesh", "SLO": "Andhra Pradesh", "ANV": "Andhra Pradesh", "TUNI": "Andhra Pradesh",
    "AKP": "Andhra Pradesh", "DVD": "Andhra Pradesh", "VSKP": "Andhra Pradesh", "VZM": "Andhra Pradesh",
    "CHE": "Andhra Pradesh", "PSA": "Andhra Pradesh", "TEL": "Andhra Pradesh", "CLX": "Andhra Pradesh",
    "OGL": "Andhra Pradesh", "NLR": "Andhra Pradesh", "GDR": "Andhra Pradesh", "RU": "Andhra Pradesh",
    "TPTY": "Andhra Pradesh", "PAK": "Andhra Pradesh", "CTO": "Andhra Pradesh", "KPD": "Tamil Nadu",
    "GY": "Andhra Pradesh", "GTL": "Andhra Pradesh", "AD": "Andhra Pradesh", "MALM": "Andhra Pradesh",
    "DHNE": "Andhra Pradesh", "KRNT": "Andhra Pradesh", "ATP": "Andhra Pradesh", "DMM": "Andhra Pradesh",
    "SSPN": "Andhra Pradesh", "HUP": "Andhra Pradesh", "NDL": "Andhra Pradesh", "MRK": "Andhra Pradesh",
    
    # Karnataka
    "SBC": "Karnataka", "SMVB": "Karnataka", "YPR": "Karnataka", "BNC": "Karnataka",
    "BAND": "Karnataka", "KJM": "Karnataka", "WFD": "Karnataka", "MYS": "Karnataka",
    "MYA": "Karnataka", "CPT": "Karnataka", "RMGM": "Karnataka", "BID": "Karnataka",
    "HAS": "Karnataka", "ASK": "Karnataka", "DRU": "Karnataka", "TTR": "Karnataka",
    "TK": "Karnataka", "DVG": "Karnataka", "HRR": "Karnataka", "RNR": "Karnataka",
    "HVR": "Karnataka", "UBL": "Karnataka", "DWR": "Karnataka", "LWR": "Karnataka",
    "BGM": "Karnataka", "GPB": "Karnataka", "BGK": "Karnataka", "BJP": "Karnataka",
    "IDR": "Karnataka", "GR": "Karnataka", "KLBG": "Karnataka", "WADI": "Karnataka",
    "YG": "Karnataka", "RC": "Karnataka", "BAY": "Karnataka", "HPT": "Karnataka",
    "KBL": "Karnataka", "GDG": "Karnataka", "BDM": "Karnataka", "MAQ": "Karnataka",
    "MAJN": "Karnataka", "UD": "Karnataka", "KUDA": "Karnataka", "BYNR": "Karnataka",
    "BTJL": "Karnataka", "MRDW": "Karnataka", "KT": "Karnataka", "GOK": "Karnataka",
    "ANKL": "Karnataka", "KAWR": "Karnataka",
    
    # Tamil Nadu
    "MAS": "Tamil Nadu", "MS": "Tamil Nadu", "TBM": "Tamil Nadu", "CGL": "Tamil Nadu",
    "AJJ": "Tamil Nadu", "TRT": "Tamil Nadu", "GYM": "Tamil Nadu", "VN": "Tamil Nadu",
    "AB": "Tamil Nadu", "JTJ": "Tamil Nadu", "TPT": "Tamil Nadu", "SA": "Tamil Nadu",
    "ED": "Tamil Nadu", "TUP": "Tamil Nadu", "CBE": "Tamil Nadu", "CBF": "Tamil Nadu",
    "PTJ": "Tamil Nadu", "TPJ": "Tamil Nadu", "DG": "Tamil Nadu", "MDU": "Tamil Nadu",
    "VPT": "Tamil Nadu", "SRT": "Tamil Nadu", "CVP": "Tamil Nadu", "TEN": "Tamil Nadu",
    "VLY": "Tamil Nadu", "NCJ": "Tamil Nadu", "CAPE": "Tamil Nadu", "RMD": "Tamil Nadu",
    "RMM": "Tamil Nadu", "MNM": "Tamil Nadu", "KKDI": "Tamil Nadu", "PDKT": "Tamil Nadu",
    "TJ": "Tamil Nadu", "KMU": "Tamil Nadu", "MV": "Tamil Nadu", "CDM": "Tamil Nadu",
    "CUD": "Tamil Nadu", "VM": "Tamil Nadu", "TMV": "Tamil Nadu",
    
    # Kerala
    "PGT": "Kerala", "OTP": "Kerala", "SRR": "Kerala", "TIR": "Kerala", "CLT": "Kerala",
    "BDJ": "Kerala", "TLY": "Kerala", "CAN": "Kerala", "PAY": "Kerala", "NLE": "Kerala",
    "KZE": "Kerala", "KGQ": "Kerala", "TVC": "Kerala", "TVP": "Kerala", "KCVL": "Kerala",
    "QLN": "Kerala", "KYJ": "Kerala", "HAD": "Kerala", "MVLK": "Kerala", "CNGR": "Kerala",
    "TRVL": "Kerala", "CGY": "Kerala", "KTYM": "Kerala", "ERN": "Kerala", "ERS": "Kerala",
    "AWY": "Kerala", "AFK": "Kerala", "CKI": "Kerala", "IJK": "Kerala", "TCR": "Kerala",
    "PNQ": "Kerala", "ALLP": "Kerala", "SRTL": "Kerala", "TUVR": "Kerala", "NIL": "Kerala",
    
    # Odisha
    "BBS": "Odisha", "BBSN": "Odisha", "CTC": "Odisha", "JKR": "Odisha", "BHC": "Odisha",
    "BLS": "Odisha", "JER": "Odisha", "PURI": "Odisha", "KUR": "Odisha", "BALU": "Odisha",
    "CAP": "Odisha", "BAM": "Odisha", "SBP": "Odisha", "SBPY": "Odisha", "BRGA": "Odisha",
    "BLGR": "Odisha", "TIG": "Odisha", "KSNG": "Odisha", "MNGD": "Odisha", "RGDA": "Odisha",
    "KRPU": "Odisha",
    
    # Chhattisgarh
    "R": "Chhattisgarh", "DURG": "Chhattisgarh", "BPHB": "Chhattisgarh", "BYT": "Chhattisgarh",
    "BSP": "Chhattisgarh", "CPH": "Chhattisgarh", "KRBA": "Chhattisgarh", "RIG": "Chhattisgarh",
    "RJN": "Chhattisgarh", "DGG": "Chhattisgarh", "PND": "Chhattisgarh", "ABKP": "Chhattisgarh",
    "BRH": "Chhattisgarh", "JDB": "Chhattisgarh",
    
    # Assam & North East
    "GHY": "Assam", "KYQ": "Assam", "RNY": "Assam", "BPRD": "Assam", "NBQ": "Assam",
    "KOJ": "Assam", "GLPT": "Assam", "CPK": "Assam", "HJI": "Assam", "LMG": "Assam",
    "DPU": "Assam", "DMV": "Nagaland", "FKG": "Assam", "MXN": "Assam", "SLGR": "Assam",
    "SRTN": "Assam", "DBRG": "Assam", "NTSK": "Assam", "TSK": "Assam", "LED": "Assam",
    "DCA": "Assam", "SCL": "Assam", "BPB": "Assam", "AGTL": "Tripura", "DMR": "Tripura",
    "NHL": "Arunachal Pradesh", "MZS": "Mizoram", "BHRB": "Mizoram"
}


def load_stations(path: Path = DATA_DIR / "stations.csv") -> dict[str, Station]:
    stations = {}
    for source in _sources(path):
        with open(source, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                code = row["code"].strip()
                st_state = row.get("state", "").strip() or STATION_STATE_MAP.get(code, "")
                station = Station(
                    code=code,
                    name=row["name"],
                    state=st_state,
                    lat=_coord(row.get("lat")),
                    lon=_coord(row.get("lon")),
                )
                # Never let a coordinate-less import overwrite a curated row
                # that already carries a position.
                existing = stations.get(code)
                if existing is not None and existing.has_coords and not station.has_coords:
                    continue
                # Same protection, applied to state: a bulk import with no
                # state field must not blank out one we already know.
                if existing is not None and existing.state and not station.state:
                    station.state = existing.state
                
                # If still blank, check fallback map
                if not station.state and code in STATION_STATE_MAP:
                    station.state = STATION_STATE_MAP[code]
                    
                stations[code] = station
    return stations


def load_routes(path: Path = DATA_DIR / "routes.csv",
                extras=EXTRA_SUFFIXES) -> list[RouteLeg]:
    legs = []
    seen = set()
    for source in _sources(path, extras):
        before = len(legs)
        _read_route_rows(source, legs)
        # A train can appear in more than one listing; keep the first copy.
        deduped = []
        for leg in legs[before:]:
            key = (leg.train_number, leg.source, leg.destination)
            if leg.train_number and key in seen:
                continue
            seen.add(key)
            deduped.append(leg)
        legs[before:] = deduped
    return legs


def _read_route_rows(path: Path, legs: list[RouteLeg]) -> None:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            legs.append(
                RouteLeg(
                    source=row["source"],
                    destination=row["destination"],
                    mode=row["mode"],
                    duration_min=int(row["duration_min"]),
                    cost_inr=float(row["cost_inr"]),
                    train_number=row.get("train_number", "") or "",
                    train_name=row.get("train_name", "") or "",
                    available=row["available"].strip().lower() == "true",
                    date=row.get("date", "") or "",
                    dep_time=row.get("dep_time", "") or "",
                    arr_time=row.get("arr_time", "") or "",
                    valid_from=row.get("valid_from", "") or "",
                    valid_to=row.get("valid_to", "") or "",
                    run_days=row.get("run_days", "") or "",
                )
            )
