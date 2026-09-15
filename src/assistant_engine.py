# -*- coding: utf-8 -*-
"""
Safarnama AI Voice & Chatbot Engine (Powered by Google Gemini 3.6 Flash)
Provides conversational Hinglish route finding, slot filling, voice queries, PNR, and live train tracking.
"""

import os
import re
import json
import urllib.request
import urllib.error
import ssl
from datetime import date as date_cls, datetime, timedelta

_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode = ssl.CERT_NONE

GEMINI_MODELS = [
    os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"),
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-flash-latest"
]


def _get_gemini_api_key():
    key = os.environ.get("GEMINI_API_KEY", "")
    if key:
        return key.strip()
    
    # Read from local .env
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("GEMINI_API_KEY="):
                        return line.split("=", 1)[1].strip().strip('"').strip("'")
        except Exception:
            pass
    return ""


def call_gemini(prompt: str, system_instruction: str = None, temperature: float = 0.4):
    """Executes a request to Google Gemini with automatic model fallback."""
    api_key = _get_gemini_api_key()
    if not api_key:
        return None, "Gemini API key is not configured in .env."

    for model in GEMINI_MODELS:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": 1024,
            }
        }
        
        if system_instruction:
            payload["systemInstruction"] = {
                "parts": [{"text": system_instruction}]
            }

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        
        try:
            with urllib.request.urlopen(req, timeout=12, context=_ssl_ctx) as res:
                if res.status == 200:
                    resp_json = json.loads(res.read().decode("utf-8"))
                    candidates = resp_json.get("candidates", [])
                    if candidates:
                        content = candidates[0].get("content", {})
                        parts = content.get("parts", [])
                        if parts:
                            return parts[0].get("text", "").strip(), None
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")
            # If model unavailable, try next model in list
            if e.code in (404, 503, 400):
                continue
            return None, f"Gemini API Error (HTTP {e.code}): {err_body}"
        except Exception as e:
            continue

    return None, "Unable to reach Gemini API. Please check your internet connection or API key."


class SafarnamaAssistant:
    def __init__(self, route_engine=None):
        self.engine = route_engine
        self.stations_map = {}
        if self.engine and hasattr(self.engine, "stations"):
            self.stations_map = self.engine.stations

    def resolve_station(self, text: str):
        """Fuzzy and alias resolver for Indian Railway stations."""
        if not text:
            return None, None
            
        cleaned = text.strip().upper()
        
        # 1. Direct code lookup
        if cleaned in self.stations_map:
            st = self.stations_map[cleaned]
            return st.code, st.name
            
        # Common aliases & popular city names
        aliases = {
            "DELHI": "NDLS",
            "NEW DELHI": "NDLS",
            "OLD DELHI": "DLI",
            "NIZAMUDDIN": "NZM",
            "HAZRAT NIZAMUDDIN": "NZM",
            "ANAND VIHAR": "ANVT",
            "DHANBAD": "DHN",
            "GOVINDPURI": "GOY",
            "KANPUR": "CNB",
            "KANPUR CENTRAL": "CNB",
            "HOWRAH": "HWH",
            "KOLKATA": "KOAA",
            "SEALDAH": "SDAH",
            "PRAYAGRAJ": "PRYJ",
            "ALLAHABAD": "PRYJ",
            "VARANASI": "BSB",
            "BANARAS": "BSBS",
            "PATNA": "PNBE",
            "MUMBAI": "MMCT",
            "MUMBAI CENTRAL": "MMCT",
            "CSMT": "CSMT",
            "PUNE": "PUNE",
            "JAIPUR": "JP",
            "AHMEDABAD": "ADI",
            "LUCKNOW": "LKO",
            "GORAKHPUR": "GKP",
            "CHENNAI": "MAS",
            "BANGALORE": "SBC",
            "BENGALURU": "SBC",
            "HYDERABAD": "HYB",
            "SECUNDERABAD": "SC",
            "CHANDIGARH": "CDG",
            "AMRITSAR": "ASR",
            "GWALIOR": "GWL",
            "BHOPAL": "BPL",
            "JABALPUR": "JBP",
            "RANCHI": "RNC",
            "GAYA": "GAYA",
            "DEHRADUN": "DDN",
            "AGRA": "AGC",
            "MATHURA": "MTJ",
            "धनबाद": "DHN",
            "गोविंदपुरी": "GOY",
            "कानपुर": "CNB",
            "हावड़ा": "HWH",
            "दिल्ली": "NDLS",
            "नई दिल्ली": "NDLS",
            "कोलकाता": "KOAA",
            "सियालदह": "SDAH",
            "प्रयागराज": "PRYJ",
            "इलाहाबाद": "PRYJ",
            "वाराणसी": "BSB",
            "बनारस": "BSBS",
            "पटना": "PNBE",
            "मुंबई": "MMCT",
            "पुणे": "PUNE",
            "जयपुर": "JP",
            "अहमदाबाद": "ADI",
            "लखनऊ": "LKO",
            "गोरखपुर": "GKP",
            "चेन्नई": "MAS",
            "बैंगलोर": "SBC",
            "बेंगलुरु": "SBC",
            "हैदराबाद": "HYB",
            "चंडीगढ़": "CDG",
            "अमृतसर": "ASR",
            "ग्वालियर": "GWL",
            "भोपाल": "BPL",
            "जबलपुर": "JBP",
            "राँची": "RNC",
            "रांची": "RNC",
            "गया": "GAYA",
            "देहरादून": "DDN",
            "आगरा": "AGC",
            "मथुरा": "MTJ",
        }
        
        for k, code in aliases.items():
            if k in cleaned or cleaned in k:
                if code in self.stations_map:
                    return code, self.stations_map[code].name
                return code, k.title()
                
        # Substring search in stations database
        low_t = text.lower().strip()
        for code, st in self.stations_map.items():
            if low_t == st.name.lower():
                return code, st.name
            if len(low_t) >= 4 and (low_t in st.name.lower() or st.name.lower() in low_t):
                return code, st.name
                
        return None, None

    def parse_date(self, text: str):
        """Converts natural Hinglish/English/Hindi dates and ISO dates into YYYY-MM-DD."""
        if not text:
            return None

        today = datetime.now()
        low = text.lower().strip()

        # Relative keywords (English, Hinglish & Hindi)
        if "aaj" in low or "today" in low or "आज" in text:
            return today.strftime("%Y-%m-%d")
        if "kal" in low or "tomorrow" in low or "next day" in low or "कल" in text:
            return (today + timedelta(days=1)).strftime("%Y-%m-%d")
        if "parso" in low or "day after" in low or "+2" in low or "परसों" in text:
            return (today + timedelta(days=2)).strftime("%Y-%m-%d")

        # 1. ISO format: YYYY-MM-DD or YYYY/MM/DD (e.g. 2026-09-16) - MUST BE CHECKED FIRST!
        iso_match = re.search(r"\b(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})\b", text)
        if iso_match:
            y, mth, d = int(iso_match.group(1)), int(iso_match.group(2)), int(iso_match.group(3))
            try:
                dt = datetime(y, mth, d)
                return dt.strftime("%Y-%m-%d")
            except Exception:
                pass

        # 2. DD-MM-YYYY or DD/MM/YYYY (e.g. 16-09-2026 or 16/09/2026)
        dmy_match = re.search(r"\b(\d{1,2})[-/.](\d{1,2})[-/.](20\d{2})\b", text)
        if dmy_match:
            d, mth, y = int(dmy_match.group(1)), int(dmy_match.group(2)), int(dmy_match.group(3))
            try:
                dt = datetime(y, mth, d)
                return dt.strftime("%Y-%m-%d")
            except Exception:
                pass

        # 3. DD-MM-YY or DD/MM/YY (e.g. 16-09-26 or 16/09/26)
        dmy_short = re.search(r"\b(\d{1,2})[-/.](\d{1,2})[-/.](\d{2})\b", text)
        if dmy_short:
            d, mth, y_short = int(dmy_short.group(1)), int(dmy_short.group(2)), int(dmy_short.group(3))
            y = 2000 + y_short
            try:
                dt = datetime(y, mth, d)
                return dt.strftime("%Y-%m-%d")
            except Exception:
                pass

        # 4. Named month: e.g. "16 sept", "16 september 2026", "sept 16"
        months = {
            "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
            "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
        }
        for m_name, m_num in months.items():
            if m_name in low:
                yr_match = re.search(r"\b(20\d{2})\b", text)
                year_num = int(yr_match.group(1)) if yr_match else today.year
                days = [int(x) for x in re.findall(r"\b(\d{1,2})\b", text) if 1 <= int(x) <= 31]
                if days:
                    day_num = days[0]
                    try:
                        dt = datetime(year_num, m_num, day_num)
                        if not yr_match and (today - dt).days > 30:
                            dt = datetime(year_num + 1, m_num, day_num)
                        return dt.strftime("%Y-%m-%d")
                    except Exception:
                        pass

        return None

    def process_message(self, user_message: str, history=None):
        """
        Main Conversational AI agent pipeline with slot-filling and route lookup.
        """
        user_message = user_message.strip()
        if not user_message:
            return {
                "reply": "Namaste ji! Main Safarnama AI Assistant hoon. Aap mujhe kisi bhi train, route, PNR ya station ke baare mein bol kar ya likh kar pooch sakte hain!",
                "action": None
            }

        # Check for 10-digit PNR query
        pnr_match = re.search(r"\b(\d{10})\b", user_message)
        if pnr_match and ("pnr" in user_message.lower() or "status" in user_message.lower() or "ticket" in user_message.lower()):
            pnr_no = pnr_match.group(1)
            return {
                "reply": f"Main aapka PNR **{pnr_no}** check kar raha hoon... Aap Live PNR tab mein bhi iska real-time coach aur berth status dekh sakte hain.",
                "action": {
                    "type": "pnr_lookup",
                    "pnr": pnr_no
                }
            }

        # Check for Train Spotting / Tracking query
        train_match = re.search(r"\b(\d{5})\b", user_message)
        if train_match and ("kahan" in user_message.lower() or "live" in user_message.lower() or "spot" in user_message.lower() or "track" in user_message.lower()):
            t_no = train_match.group(1)
            return {
                "reply": f"Train **{t_no}** ka live running status aur GPS position check kar raha hoon. Aap ise NTES Spot Your Train portal par track kar sakte hain!",
                "action": {
                    "type": "spot_train",
                    "train_number": t_no
                }
            }

        system_instruction = """
You are Safarnama AI, a very helpful, friendly, and knowledgeable Indian Railways journey assistant.
You converse naturally in warm, conversational Hinglish (Hindi + English) with Indian politeness (e.g. "Namaste ji!", "Aapka safar shubh ho!", "Zaroor ji").

Your task is to understand user travel requests and extract route details:
- Source Station / City (e.g. Dhanbad, New Delhi, Govindpuri, Kanpur)
- Destination Station / City
- Travel Date (e.g. 31-08-2026, kal, parso, aaj)
- Travel Time / Preference (e.g. subah 11 bje, evening, fastest, cheapest)

SLOT-FILLING RULES:
1. If the user gives a complete route request (Source, Destination, and Date), extract them clearly and reply with enthusiasm in Hinglish.
2. If ANY required detail is missing:
   - If Destination is missing: Ask politely where they want to travel.
   - If Source is missing: Ask which boarding station they want to start from.
   - If Date is missing: Ask politely for the travel date (e.g. "Kripya travel ki date batayein jaise 'kal', 'parso' ya koi specific date?").
3. Always include a structured JSON block at the very end of your response inside ```json ... ```:
{
  "is_complete": true/false,
  "missing_slots": ["date", "source", "destination"],
  "source_raw": "Dhanbad",
  "dest_raw": "Govindpuri",
  "date_raw": "31-08-2026",
  "time_raw": "11:00 AM",
  "action": "search_route" / "ask_clarification"
}
"""

        # Formulate prompt
        prompt = f"""
Current Date: {datetime.now().strftime('%Y-%m-%d')}
User Message: "{user_message}"

Analyze the user's intent, extract slots, and provide a helpful Hinglish reply with the structured JSON block at the end.
"""

        gemini_reply, err = call_gemini(prompt, system_instruction=system_instruction, temperature=0.3)
        
        if err or not gemini_reply:
            # Fallback heuristic parser
            return self._heuristic_fallback(user_message)

        # Parse JSON block from Gemini reply
        json_data = {}
        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", gemini_reply, re.DOTALL)
        if json_match:
            try:
                json_data = json.loads(json_match.group(1))
            except Exception:
                pass

        # Clean conversational reply for user (hide the raw JSON block)
        clean_reply = re.sub(r"```(?:json)?\s*\{.*?\}\s*```", "", gemini_reply, flags=re.DOTALL).strip()

        # If complete, resolve station codes and prepare auto-search action
        src_raw = json_data.get("source_raw")
        dst_raw = json_data.get("dest_raw")
        date_raw = json_data.get("date_raw")
        time_raw = json_data.get("time_raw", "00:00")

        src_code, src_name = self.resolve_station(src_raw) if src_raw else (None, None)
        dst_code, dst_name = self.resolve_station(dst_raw) if dst_raw else (None, None)
        parsed_dt = self.parse_date(date_raw) if date_raw else None

        action = None
        if src_code and dst_code:
            final_dt = parsed_dt or (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            
            # Execute actual routing query if engine available
            route_info = ""
            if self.engine:
                try:
                    plan = self.engine.plan_journey(src_code, dst_code, final_dt, time_raw or "00:00")
                    if plan and plan.get("best"):
                        best_it = plan["best"]["itinerary"]
                        sched = plan["best"]["schedule"]
                        train_names = [leg.train_name for leg in best_it.legs if leg.train_name]
                        route_info = f"\n\n🚆 **Best Option**: {', '.join(train_names)} | Duration: {best_it.total_duration_display} | Fare: ₹{best_it.total_fare}"
                except Exception:
                    pass

            action = {
                "type": "fill_and_search",
                "source": src_code,
                "source_name": src_name or src_code,
                "destination": dst_code,
                "destination_name": dst_name or dst_code,
                "date": final_dt,
                "time": time_raw or "00:00"
            }
            if route_info:
                clean_reply += route_info

        return {
            "reply": clean_reply,
            "action": action,
            "extracted": {
                "source": src_code or src_raw,
                "destination": dst_code or dst_raw,
                "date": parsed_dt or date_raw,
            }
        }

    def _heuristic_fallback(self, msg: str):
        """Deterministic NLP fallback when Gemini API is unreachable."""
        m_low = msg.lower()
        
        # Try to find "X se Y" (supports English & Devanagari Hindi)
        se_match = re.search(r"([a-zA-Z\u0900-\u097F]+)\s+(?:se|से)\s+([a-zA-Z\u0900-\u097F]+)", msg, re.IGNORECASE)
        to_match = re.search(r"([a-zA-Z\u0900-\u097F]+)\s+(?:to|tak|तक)\s+([a-zA-Z\u0900-\u097F]+)", msg, re.IGNORECASE)
        
        src_cand, dst_cand = None, None
        if se_match:
            src_cand, dst_cand = se_match.group(1), se_match.group(2)
        elif to_match:
            src_cand, dst_cand = to_match.group(1), to_match.group(2)
            
        src_code, src_name = self.resolve_station(src_cand) if src_cand else (None, None)
        dst_code, dst_name = self.resolve_station(dst_cand) if dst_cand else (None, None)
        dt = self.parse_date(msg)
        
        if src_code and dst_code:
            target_dt = dt or (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            return {
                "reply": f"Namaste ji! Maine aapke liye **{src_name} ({src_code})** se **{dst_name} ({dst_code})** ke trains search kar diye hain date **{target_dt}** ke liye.",
                "action": {
                    "type": "fill_and_search",
                    "source": src_code,
                    "source_name": src_name,
                    "destination": dst_code,
                    "destination_name": dst_name,
                    "date": target_dt
                }
            }
            
        return {
            "reply": "Namaste ji! Kripya batayein aap kaunse station se kaunse station tak travel karna chahte hain aur kis date par? (Jaise: *'Dhanbad se Govindpuri kal subah'*).",
            "action": None
        }
