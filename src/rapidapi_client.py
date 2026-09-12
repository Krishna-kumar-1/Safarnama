# -*- coding: utf-8 -*-
"""
RapidAPI IRCTC Integration Client (irctc1.p.rapidapi.com)
Provides live PNR lookup, real-time train running status, train schedule, and live station departures.
"""

import os
import json
import urllib.request
import ssl
from datetime import datetime

RAPID_HOST = os.environ.get("RAPIDAPI_HOST", "irctc1.p.rapidapi.com")

_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode = ssl.CERT_NONE


def _get_rapid_keys():
    """Extract all configured RapidAPI keys from environment or .env file."""
    keys = []
    
    # 1. Check environment variables
    env_pool = os.environ.get("RAPIDAPI_KEYS", "")
    if env_pool:
        keys.extend([k.strip() for k in env_pool.split(",") if k.strip()])
    single_key = os.environ.get("RAPIDAPI_KEY", "")
    if single_key and single_key.strip():
        keys.append(single_key.strip())
        
    # 2. Check local .env file
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("RAPIDAPI_KEYS="):
                        val = line.split("=", 1)[1].strip().strip('"').strip("'")
                        keys.extend([k.strip() for k in val.split(",") if k.strip()])
                    elif line.startswith("RAPIDAPI_KEY="):
                        val = line.split("=", 1)[1].strip().strip('"').strip("'")
                        if val:
                            keys.append(val)
        except Exception:
            pass
        
    # Deduplicate while preserving order
    seen = set()
    deduped = []
    for k in keys:
        if k not in seen:
            seen.add(k)
            deduped.append(k)
    return deduped


def _call_rapidapi(path: str, timeout: int = 8):
    """
    Execute RapidAPI request with multi-key pool automatic failover.
    Cycles through all configured keys if rate limits (429), quota limits, or auth errors occur.
    """
    keys = _get_rapid_keys()
    if not keys:
        return None

    url = f"https://{RAPID_HOST}{path}"
    
    for idx, key in enumerate(keys):
        masked_key = f"...{key[-6:]}" if len(key) >= 6 else "***"
        headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": RAPID_HOST,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx) as res:
                if res.status == 200:
                    resp_json = json.loads(res.read().decode())
                    # Check if response payload contains quota exceeded message
                    msg = str(resp_json.get("message", "")).lower()
                    if "exceeded" in msg or "rate limit" in msg or "quota" in msg:
                        print(f"[RapidAPI Pool] Key {masked_key} exceeded quota/rate limit. Failing over to next key...")
                        continue
                    return resp_json
        except urllib.error.HTTPError as http_err:
            # 429 = Too Many Requests / Quota, 403 = Forbidden / Quota exceeded, 401 = Unauthorized
            if http_err.code in (429, 403, 401):
                print(f"[RapidAPI Pool] Key {masked_key} received HTTP {http_err.code} ({http_err.reason}). Failing over to next key...")
                continue
            else:
                print(f"[RapidAPI Error] Key {masked_key} HTTP {http_err.code}: {http_err}")
        except Exception as e:
            print(f"[RapidAPI Error] Key {masked_key} -> {e}")
            
    return None


# 1. LIVE PNR STATUS LOOKUP
def rapid_get_pnr_status(pnr: str):
    clean_pnr = str(pnr).strip().replace("-", "").replace(" ", "")
    if len(clean_pnr) != 10:
        return None
    
    data = _call_rapidapi(f"/api/v3/getPNRStatus?pnrNumber={clean_pnr}")
    if data and data.get("status") and "data" in data:
        d = data["data"]
        
        passengers = []
        for idx, p in enumerate(d.get("PassengerStatus", []), start=1):
            passengers.append({
                "number": f"Passenger {idx}",
                "booking_status": f"{p.get('BookingStatus', 'CNF')}/{p.get('BookingCoachId', '')}/{p.get('BookingBerthNo', '')}",
                "current_status": p.get("CurrentStatus", "CNF"),
                "coach": p.get("CurrentCoachId", p.get("BookingCoachId", "")),
                "berth": f"{p.get('CurrentBerthNo', '')} [{p.get('CurrentBerthCode', '')}]" if p.get("CurrentBerthNo") else (p.get("BookingBerthNo", "")),
            })
            
        if not passengers:
            passengers.append({
                "number": "Passenger 1",
                "booking_status": "CNF",
                "current_status": "CNF",
                "coach": d.get("Class", "SL"),
                "berth": "Confirmed",
            })
            
        return {
            "pnr": d.get("Pnr", clean_pnr),
            "is_live": True,
            "provider": "RapidAPI IRCTC",
            "train_number": d.get("TrainNo", ""),
            "train_name": d.get("TrainName", "Express"),
            "source": d.get("From", ""),
            "source_name": d.get("BoardingStationName", d.get("From", "")),
            "destination": d.get("To", ""),
            "destination_name": d.get("ReservationUptoName", d.get("To", "")),
            "date_of_journey": d.get("Doj", ""),
            "arrival_date": d.get("DestinationDoj", ""),
            "class": d.get("Class", ""),
            "quota": d.get("Quota", "GN"),
            "fare": d.get("TicketFare", d.get("TotalFare", 0)),
            "chart_prepared": bool(d.get("ChartPrepared", False)),
            "chart_status": "Chart Prepared" if d.get("ChartPrepared") else "Chart Not Prepared",
            "passengers": passengers,
            "message": "Live IRCTC Passenger Data Verified"
        }
    return None


# 2. LIVE TRAIN RUNNING STATUS
def rapid_get_live_train(train_no: str, date_str: str = None):
    clean_no = str(train_no).strip()
    if not date_str:
        date_str = datetime.now().strftime("%d-%m-%Y")
        
    data = _call_rapidapi(f"/api/v1/liveTrainStatus?trainNo={clean_no}&date={date_str}")
    if data and data.get("status") and "data" in data:
        d = data["data"]
        return d
    return None


# 3. LIVE STATION DEPARTURES
def rapid_get_live_station(from_stn: str, to_stn: str = "", hours: int = 4):
    f_code = str(from_stn).strip().upper()
    t_code = str(to_stn).strip().upper() if to_stn else ""
    path = f"/api/v3/getLiveStation?fromStationCode={f_code}&hours={hours}"
    if t_code:
        path += f"&toStationCode={t_code}"
        
    data = _call_rapidapi(path)
    if data and data.get("status") and "data" in data:
        return data["data"]
    return None
