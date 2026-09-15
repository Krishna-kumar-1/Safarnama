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

_WORKING_MODEL = None

GEMINI_MODELS = [
    os.environ.get("GEMINI_MODEL", "gemini-3.6-flash"),
    "gemini-3.6-flash",
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash"
]

HINDI_MONTHS = {
    "जनवरी": 1, "फरवरी": 2, "फ़रवरी": 2, "मार्च": 3,
    "अप्रैल": 4, "अप्रेल": 4, "मई": 5, "जून": 6,
    "जुलाई": 7, "अगस्त": 8, "सितंबर": 9, "सितम्बर": 9,
    "अक्टूबर": 10, "अक्तूबर": 10, "नवंबर": 11, "नवम्बर": 11,
    "दिसंबर": 12, "दिसम्बर": 12
}

ENGLISH_MONTHS = {
    "january": 1, "jan": 1,
    "february": 2, "feb": 2,
    "march": 3, "mar": 3,
    "april": 4, "apr": 4,
    "may": 5,
    "june": 6, "jun": 6,
    "july": 7, "jul": 7,
    "august": 8, "aug": 8,
    "september": 9, "sep": 9, "sept": 9,
    "october": 10, "oct": 10,
    "november": 11, "nov": 11,
    "december": 12, "dec": 12
}

POPULAR_STATION_ALIASES = {
    # English aliases & city names
    "DELHI": "NDLS", "NEW DELHI": "NDLS", "OLD DELHI": "DLI", "NIZAMUDDIN": "NZM",
    "HAZRAT NIZAMUDDIN": "NZM", "ANAND VIHAR": "ANVT", "ANAND VIHAR TERMINAL": "ANVT",
    "DHANBAD": "DHN", "DHANBAD JN": "DHN",
    "GOVINDPURI": "GOY",
    "KANPUR": "CNB", "KANPUR CENTRAL": "CNB", "KANPUR ANWARGANJ": "CPA",
    "HOWRAH": "HWH", "KOLKATA": "KOAA", "SEALDAH": "SDAH",
    "PRAYAGRAJ": "PRYJ", "ALLAHABAD": "PRYJ", "PRAYAGRAJ JN": "PRYJ",
    "VARANASI": "BSB", "BANARAS": "BSBS", "MANDUADIH": "BSBS",
    "PATNA": "PNBE", "PATNA JN": "PNBE", "RAJENDRA NAGAR": "RJPB",
    "MUMBAI": "MMCT", "MUMBAI CENTRAL": "MMCT", "CSMT": "CSMT", "BOMBAY": "MMCT",
    "PUNE": "PUNE", "PUNE JN": "PUNE",
    "JAIPUR": "JP", "JAIPUR JN": "JP",
    "AHMEDABAD": "ADI", "AHMEDABAD JN": "ADI",
    "LUCKNOW": "LKO", "LUCKNOW CHARBAGH": "LKO", "LUCKNOW JN": "LJN", "LKO": "LKO",
    "GORAKHPUR": "GKP", "GORAKHPUR JN": "GKP",
    "CHENNAI": "MAS", "CHENNAI CENTRAL": "MAS", "MADRAS": "MAS",
    "BANGALORE": "SBC", "BENGALURU": "SBC", "KSR BENGALURU": "SBC",
    "HYDERABAD": "HYB", "SECUNDERABAD": "SC",
    "CHANDIGARH": "CDG", "AMRITSAR": "ASR",
    "GWALIOR": "GWL", "BHOPAL": "BPL", "HABIBGANJ": "RKMP", "RANI KAMLAPATI": "RKMP",
    "JABALPUR": "JBP", "INDORE": "INDB",
    "RANCHI": "RNC", "GAYA": "GAYA", "DEHRADUN": "DDN", "HARIDWAR": "HW",
    "AGRA": "AGC", "AGRA CANTT": "AGC", "AGRA FORT": "AF", "MATHURA": "MTJ",
    "SURAT": "ST", "VADODARA": "BRC", "KOTA": "KOTA", "JAMMU": "JAT",
    "AYODHYA": "AY", "AYODHYA DHAM": "AY", "AYODHYA CANTT": "AYC",
    "BAREILLY": "BE", "MORADABAD": "MB", "ALIGARH": "ALJN", "MEERUT": "MTC",
    
    # Hindi Devanagari aliases
    "धनबाद": "DHN", "गोविंदपुरी": "GOY",
    "कानपुर": "CNB", "कानपुर सेंट्रल": "CNB",
    "हावड़ा": "HWH", "दिल्ली": "NDLS", "नई दिल्ली": "NDLS", "पुरानी दिल्ली": "DLI",
    "निज़ामुद्दीन": "NZM", "निजामुद्दीन": "NZM", "आनंद विहार": "ANVT",
    "कोलकाता": "KOAA", "सियालदह": "SDAH",
    "प्रयागराज": "PRYJ", "इलाहाबाद": "PRYJ",
    "वाराणसी": "BSB", "बनारस": "BSBS",
    "पटना": "PNBE", "मुंबई": "MMCT", "पुणे": "PUNE",
    "जयपुर": "JP", "अहमदाबाद": "ADI",
    "लखनऊ": "LKO", "चारबाग": "LKO",
    "गोरखपुर": "GKP", "चेन्नई": "MAS",
    "बैंगलोर": "SBC", "बेंगलुरु": "SBC", "हैदराबाद": "HYB", "सिकंदराबाद": "SC",
    "चंडीगढ़": "CDG", "अमृतसर": "ASR",
    "ग्वालियर": "GWL", "भोपाल": "BPL", "रानी कमलापति": "RKMP",
    "जबलपुर": "JBP", "इंदौर": "INDB",
    "राँची": "RNC", "रांची": "RNC", "गया": "GAYA",
    "देहरादून": "DDN", "हरिद्वार": "HW",
    "आगरा": "AGC", "मथुरा": "MTJ", "सूरत": "ST", "वडोदरा": "BRC",
    "कोटा": "KOTA", "जम्मू": "JAT", "अयोध्या": "AY", "अयोध्या धाम": "AY",
    "बरेली": "BE", "मुरादाबाद": "MB", "अलीगढ़": "ALJN", "मेरठ": "MTC",
}


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


def detect_language(text: str) -> str:
    """
    Detects whether the text is Hindi (Devanagari script), Hinglish (Roman Hindi), or English.
    """
    if not text:
        return "hinglish"
    # Devanagari script detection
    if re.search(r"[\u0900-\u097F]", text):
        return "hindi"

    low = text.lower()
    hinglish_markers = {
        "kahan", "kaha", "jana", "jaana", "chahiye", "batao", "bataiye", "batayein",
        "tareekh", "taarikh", "tarikh", "mahina", "mahine", "kaunsa", "konsa",
        "se", "tak", "liye", "subah", "sham", "shaam", "raat", "dopahar",
        "aaj", "kal", "parso", "parson", "bhejo", "hoga", "hai", "hain", "hoon",
        "kaise", "milegi", "milega", "kardo", "kar do", "dikhao", "karo", "bhi",
        "mujhe", "humko", "aap", "tum", "mera", "meri", "gaadi", "gadi",
        "batana", "dhundo", "dhoondo", "agle", "agla", "pichle", "wali", "wale"
    }
    words = set(re.findall(r"\b[a-z]+\b", low))
    if words & hinglish_markers:
        return "hinglish"

    if re.search(r"\b(se|tak|ke\s+liye|ki|ko|mein|me)\b", low):
        return "hinglish"

    return "english"


def extract_day(text: str):
    """Extracts day of month (1-31) from natural text."""
    if not text:
        return None
    # 1. Day with explicit date/ordinal suffix or keyword
    m = re.search(r'\b([1-9]|[12]\d|3[01])\s*(?:st|nd|rd|th|वीं|vi|taarikh|tareekh|tarikh|तारीख|ko|को)\b', text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # 2. Prefix keyword e.g. "tareekh 25", "taarikh 25", "तारीख 25", "date 25"
    m2 = re.search(r'(?:taarikh|tareekh|tarikh|तारीख|date)\s*([1-9]|[12]\d|3[01])\b', text, re.IGNORECASE)
    if m2:
        return int(m2.group(1))
    # 3. e.g. "25 ke liye" or "25 के लिए"
    m3 = re.search(r'\b([1-9]|[12]\d|3[01])\s+(?:ke\s+liye|के\s+लिए)', text, re.IGNORECASE)
    if m3:
        return int(m3.group(1))
    # 4. Standalone number when user enters just the day e.g. "25"
    m4 = re.fullmatch(r'\s*([1-9]|[12]\d|3[01])\s*', text)
    if m4:
        return int(m4.group(1))
    return None


def extract_month(text: str):
    """Extracts month number (1-12) and name from English, Hindi, or relative references."""
    if not text:
        return None, None
    low = text.lower().strip()

    # 1. Hindi Devanagari months
    for m_hi, m_num in HINDI_MONTHS.items():
        if m_hi in text:
            return m_num, m_hi

    # 2. English months
    for m_en, m_num in ENGLISH_MONTHS.items():
        if re.search(rf'\b{m_en}\b', low):
            return m_num, m_en.title()

    # 3. Relative month
    if re.search(r'\b(next\s+month|agle\s+mahine?|अगले\s+महीने|अगला\s+महीना)\b', low):
        today = datetime.now()
        nm = today.month + 1 if today.month < 12 else 1
        return nm, "next month"

    if re.search(r'\b(this\s+month|is\s+mahine?|इसी\s+महीने|इस\s+महीने)\b', low):
        today = datetime.now()
        return today.month, "this month"

    return None, None


def call_gemini(prompt: str, system_instruction: str = None, temperature: float = 0.3):
    """Executes a fast request to Google Gemini with verified working model caching and 3.5s timeout."""
    global _WORKING_MODEL
    api_key = _get_gemini_api_key()
    if not api_key:
        return None, "Gemini API key is not configured in .env."

    models_to_try = [_WORKING_MODEL] if _WORKING_MODEL else []
    for m in GEMINI_MODELS:
        if m not in models_to_try:
            models_to_try.append(m)

    for model in models_to_try:
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
                "maxOutputTokens": 350,
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
            with urllib.request.urlopen(req, timeout=3.5, context=_ssl_ctx) as res:
                if res.status == 200:
                    resp_json = json.loads(res.read().decode("utf-8"))
                    candidates = resp_json.get("candidates", [])
                    if candidates:
                        content = candidates[0].get("content", {})
                        parts = content.get("parts", [])
                        if parts:
                            _WORKING_MODEL = model
                            return parts[0].get("text", "").strip(), None
        except Exception:
            continue

    return None, "Unable to reach Gemini API. Please check your internet connection or API key."


class SafarnamaAssistant:
    def __init__(self, route_engine=None):
        self.engine = route_engine
        self.stations_map = {}
        if self.engine and hasattr(self.engine, "stations"):
            self.stations_map = self.engine.stations

    def resolve_station(self, text: str):
        """Fuzzy and alias resolver for Indian Railway stations (English & Hindi)."""
        if not text:
            return None, None
            
        cleaned = text.strip().upper()
        cleaned_raw = text.strip()
        
        # 1. Direct code lookup
        if cleaned in self.stations_map:
            st = self.stations_map[cleaned]
            return st.code, st.name

        # 2. Exact alias match
        if cleaned in POPULAR_STATION_ALIASES:
            code = POPULAR_STATION_ALIASES[cleaned]
            name = self.stations_map[code].name if code in self.stations_map else cleaned.title()
            return code, name
            
        if cleaned_raw in POPULAR_STATION_ALIASES:
            code = POPULAR_STATION_ALIASES[cleaned_raw]
            name = self.stations_map[code].name if code in self.stations_map else cleaned_raw
            return code, name

        # Word boundary or substring alias match
        for k, code in POPULAR_STATION_ALIASES.items():
            if len(cleaned) >= 4 and (k == cleaned or k in cleaned or (len(k) >= 4 and cleaned in k)):
                if code in self.stations_map:
                    return code, self.stations_map[code].name
                return code, k.title()
                
        # 3. Match against loaded station database
        low_t = text.lower().strip()
        for code, st in self.stations_map.items():
            st_name_low = st.name.lower()
            if low_t == st_name_low:
                return code, st.name
            if len(low_t) >= 4 and (low_t in st_name_low or st_name_low in low_t):
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

        # 4. Month name + Day (e.g. "25 October", "25th Oct 2026", "25 अक्टूबर", "अक्टूबर 25")
        m_num, m_name = extract_month(text)
        if m_num:
            day_num = extract_day(text)
            if not day_num:
                days = [int(x) for x in re.findall(r"\b(\d{1,2})\b", text) if 1 <= int(x) <= 31]
                if days:
                    day_num = days[0]
            if day_num:
                yr_match = re.search(r"\b(20\d{2})\b", text)
                year_num = int(yr_match.group(1)) if yr_match else today.year
                try:
                    dt = datetime(year_num, m_num, day_num)
                    if not yr_match and (today - dt).days > 30:
                        dt = datetime(year_num + 1, m_num, day_num)
                    return dt.strftime("%Y-%m-%d")
                except Exception:
                    pass

        return None

    def extract_slots_from_history(self, history):
        """Reconstructs previously extracted slots from multi-turn history."""
        slots = {
            "source": None,
            "source_name": None,
            "destination": None,
            "destination_name": None,
            "date": None,
            "day": None,
            "month": None,
            "language": None
        }
        if not history or not isinstance(history, list):
            return slots

        for item in history:
            if not isinstance(item, dict):
                continue
            # Check attached extracted metadata
            ext = item.get("extracted")
            if isinstance(ext, dict):
                for k in ("source", "source_name", "destination", "destination_name", "date", "day", "month", "language"):
                    if ext.get(k):
                        slots[k] = ext[k]
            
            # If user message, update language
            if item.get("role") == "user":
                u_content = item.get("content", "")
                if u_content:
                    u_lang = detect_language(u_content)
                    if u_lang:
                        slots["language"] = u_lang

        return slots

    def extract_slots(self, text: str, prev_slots=None):
        """
        Fast local deterministic slot-extractor (< 2ms) for Indian Railways queries.
        Handles source, destination, day, month, date, and multi-turn merges.
        """
        prev = prev_slots or {}
        slots = {
            "source": prev.get("source"),
            "source_name": prev.get("source_name"),
            "destination": prev.get("destination"),
            "destination_name": prev.get("destination_name"),
            "date": prev.get("date"),
            "day": prev.get("day"),
            "month": prev.get("month"),
            "language": prev.get("language")
        }

        # Check full date first
        full_dt = self.parse_date(text)
        if full_dt:
            slots["date"] = full_dt

        # Check day and month
        d = extract_day(text)
        if d:
            slots["day"] = d
            
        m_num, m_name = extract_month(text)
        if m_num:
            slots["month"] = m_num

        # If we have both day and month but no date yet, combine them
        if slots.get("day") and slots.get("month") and not slots.get("date"):
            today = datetime.now()
            yr_match = re.search(r"\b(20\d{2})\b", text)
            year_num = int(yr_match.group(1)) if yr_match else today.year
            try:
                dt = datetime(year_num, slots["month"], slots["day"])
                if not yr_match and (today - dt).days > 30:
                    dt = datetime(year_num + 1, slots["month"], slots["day"])
                slots["date"] = dt.strftime("%Y-%m-%d")
            except Exception:
                pass

        # Stop words that should not be parsed as stations
        stop_words = {"where", "kahan", "kaha", "ticket", "train", "gaadi", "gadi", "booking", "seat", "date", "tarikh", "taarikh"}

        # 1. Look for explicit pairs: "X se Y" or "X to Y"
        se_match = re.search(r"([a-zA-Z\u0900-\u097F]+)\s+(?:se|से)\s+([a-zA-Z\u0900-\u097F]+)", text, re.IGNORECASE)
        to_match = re.search(r"([a-zA-Z\u0900-\u097F]+)\s+(?:to|tak|तक)\s+([a-zA-Z\u0900-\u097F]+)", text, re.IGNORECASE)

        if se_match:
            c1, c2 = se_match.group(1).strip(), se_match.group(2).strip()
            if c1.lower() not in stop_words:
                s_code, s_name = self.resolve_station(c1)
                if s_code:
                    slots["source"] = s_code
                    slots["source_name"] = s_name
            if c2.lower() not in stop_words:
                d_code, d_name = self.resolve_station(c2)
                if d_code:
                    slots["destination"] = d_code
                    slots["destination_name"] = d_name

        elif to_match:
            c1, c2 = to_match.group(1).strip(), to_match.group(2).strip()
            if c1.lower() not in stop_words:
                s_code, s_name = self.resolve_station(c1)
                if s_code:
                    slots["source"] = s_code
                    slots["source_name"] = s_name
            if c2.lower() not in stop_words:
                d_code, d_name = self.resolve_station(c2)
                if d_code:
                    slots["destination"] = d_code
                    slots["destination_name"] = d_name

        # 2. Look for isolated source: "X se" or "from X"
        if not slots.get("source"):
            from_match = re.search(r"(?:from)\s+([a-zA-Z\u0900-\u097F]+)", text, re.IGNORECASE)
            se_single = re.search(r"([a-zA-Z\u0900-\u097F]+)\s+(?:se|से)\b", text, re.IGNORECASE)
            src_cand = from_match.group(1) if from_match else (se_single.group(1) if se_single else None)
            if src_cand and src_cand.lower() not in stop_words:
                s_code, s_name = self.resolve_station(src_cand)
                if s_code:
                    slots["source"] = s_code
                    slots["source_name"] = s_name

        # 3. Look for isolated destination: "to Y", "Y ke liye", "Y tak"
        if not slots.get("destination"):
            to_single = re.search(r"(?:to|tak|तक)\s+([a-zA-Z\u0900-\u097F]+)", text, re.IGNORECASE)
            liye_single = re.search(r"([a-zA-Z\u0900-\u097F]+)\s+(?:ke\s+liye|के\s+लिए|jana\s+hai|जाना\s+है)", text, re.IGNORECASE)
            dst_cand = to_single.group(1) if to_single else (liye_single.group(1) if liye_single else None)
            if dst_cand and dst_cand.lower() not in stop_words:
                d_code, d_name = self.resolve_station(dst_cand)
                if d_code:
                    slots["destination"] = d_code
                    slots["destination_name"] = d_name

        # 4. Multi-turn single station input (e.g. user just replies "Kanpur" or "कानपुर")
        tokens = re.findall(r"[a-zA-Z\u0900-\u097F]+", text)
        for token in tokens:
            t_low = token.lower()
            if t_low in stop_words or t_low in {"train", "chahiye", "batao", "please", "yes", "ha", "haan", "bhejo"}:
                continue
            st_code, st_name = self.resolve_station(token)
            if st_code:
                if not slots.get("source"):
                    slots["source"] = st_code
                    slots["source_name"] = st_name
                elif not slots.get("destination") and st_code != slots.get("source"):
                    slots["destination"] = st_code
                    slots["destination_name"] = st_name
                break

        return slots

    def process_message(self, user_message: str, history=None):
        """
        Main Conversational AI agent pipeline with zero-latency local slot-filling,
        multi-turn context memory, Hindi/Hinglish/English language matching, and Gemini fallback.
        """
        user_message = user_message.strip()
        lang = detect_language(user_message)

        if not user_message:
            if lang == "hindi":
                reply = "नमस्ते! मैं सफ़रनामा एआई सहायक हूँ। आप मुझसे किसी भी ट्रेन, रूट, पीएनआर या स्टेशन के बारे में पूछ सकते हैं!"
            elif lang == "english":
                reply = "Hello! I am the Safarnama AI Assistant. Ask me anything about trains, routes, PNR, or live status!"
            else:
                reply = "Namaste ji! Main Safarnama AI Assistant hoon. Aap mujhe kisi bhi train, route, PNR ya station ke baare mein bol kar ya likh kar pooch sakte hain!"
            return {"reply": reply, "action": None}

        # Check for 10-digit PNR query
        pnr_match = re.search(r"\b(\d{10})\b", user_message)
        if pnr_match and any(w in user_message.lower() for w in ("pnr", "status", "ticket", "टिकट", "पीएनआर")):
            pnr_no = pnr_match.group(1)
            if lang == "hindi":
                reply = f"मैं आपका पीएनआर **{pnr_no}** चेक कर रहा हूँ... आप लाइव पीएनआर टैब में भी इसका रियल-टाइम स्टेटस देख सकते हैं।"
            elif lang == "english":
                reply = f"Checking real-time status for PNR **{pnr_no}**... You can view the berth and coach details in the Live PNR tab."
            else:
                reply = f"Main aapka PNR **{pnr_no}** check kar raha hoon... Aap Live PNR tab mein bhi iska real-time coach aur berth status dekh sakte hain."
            return {
                "reply": reply,
                "action": {"type": "pnr_lookup", "pnr": pnr_no}
            }

        # Check for Train Spotting / Tracking query
        train_match = re.search(r"\b(\d{5})\b", user_message)
        if train_match and any(w in user_message.lower() for w in ("kahan", "live", "spot", "track", "कहाँ", "लाइव", "ट्रैक")):
            t_no = train_match.group(1)
            if lang == "hindi":
                reply = f"ट्रेन **{t_no}** की लाइव रनिंग स्थिति और जीपीएस लोकेशन ट्रैक की जा रही है। आप इसे लाइव स्पॉट टैब पर देख सकते हैं।"
            elif lang == "english":
                reply = f"Tracking live running status and GPS position for train **{t_no}**. Opening Spot Your Train view."
            else:
                reply = f"Train **{t_no}** ka live running status aur GPS position check kar raha hoon. Aap ise NTES Spot Your Train portal par track kar sakte hain!"
            return {
                "reply": reply,
                "action": {"type": "spot_train", "train_number": t_no}
            }

        # Multi-turn slot resolution
        prev_slots = self.extract_slots_from_history(history)
        slots = self.extract_slots(user_message, prev_slots)
        
        # If user explicitly used Hindi or Hinglish, respect that; otherwise preserve previous turn language
        effective_lang = lang if (lang != "english" or not prev_slots.get("language")) else prev_slots.get("language", "english")
        slots["language"] = effective_lang

        # Detect travel intent
        travel_keywords = {
            "train", "ticket", "route", "se", "to", "tak", "jana", "jaana", "chahiye",
            "batao", "chalegi", "booking", "seat", "गाड़ी", "ट्रेन", "सफ़र", "सफर",
            "जाना", "टिकट", "बताओ", "चाहिए"
        }
        msg_words = set(re.findall(r"[a-zA-Z\u0900-\u097F]+", user_message.lower()))
        has_travel_intent = bool(
            slots.get("source") or slots.get("destination") or slots.get("day") or
            (msg_words & travel_keywords)
        )

        if has_travel_intent:
            src = slots.get("source")
            src_name = slots.get("source_name") or src
            dst = slots.get("destination")
            dst_name = slots.get("destination_name") or dst
            dt = slots.get("date")
            day = slots.get("day")
            month = slots.get("month")

            # CASE 1: Route is 100% complete! (Source, Destination, and valid Date)
            if src and dst and dt:
                if effective_lang == "hindi":
                    reply = f"मैंने आपके लिए **{src_name} ({src})** से **{dst_name} ({dst})** के लिए दिनांक **{dt}** की सभी ट्रेनें खोज ली हैं!"
                elif effective_lang == "english":
                    reply = f"I have found train routes from **{src_name} ({src})** to **{dst_name} ({dst})** on **{dt}**!"
                else:
                    reply = f"Maine aapke liye **{src_name} ({src})** se **{dst_name} ({dst})** ke liye date **{dt}** ki trains search kar li hain!"

                action = {
                    "type": "fill_and_search",
                    "source": src,
                    "source_name": src_name,
                    "destination": dst,
                    "destination_name": dst_name,
                    "date": dt,
                    "time": "00:00"
                }
                return {
                    "reply": reply,
                    "action": action,
                    "extracted": slots
                }

            # CASE 2: Source known, Destination missing, AND Month is missing (e.g. "25 taarikh ke liye lucknow se train")
            if src and not dst and day and not month:
                if effective_lang == "hindi":
                    reply = f"आप **{src_name}** से कहाँ जाना चाहते हैं? और कौन से महीने की {day} तारीख को यात्रा करना चाहते हैं (जैसे सितंबर या अक्टूबर)?"
                elif effective_lang == "english":
                    reply = f"Where would you like to travel to from **{src_name}**? And which month's {day}th would you like to travel on (for example, September or October)?"
                else:
                    reply = f"Aap **{src_name}** se kahan jaana chahte hain? Aur kaunse mahine ki {day} tareekh ko travel karna chahte hain (jaise September ya October)?"
                return {
                    "reply": reply,
                    "action": None,
                    "extracted": slots
                }

            # CASE 3: Source known, Destination missing (e.g. "Dhanbad se train" / "from Dhanbad to where")
            if src and not dst:
                if effective_lang == "hindi":
                    reply = f"आप **{src_name}** से कहाँ जाना चाहते हैं और किस तारीख को?"
                elif effective_lang == "english":
                    reply = f"Where would you like to travel to from **{src_name}**, and on which date?"
                else:
                    reply = f"Aap **{src_name}** se kahan jaana chahte hain aur kis date ko travel karna chahte hain?"
                return {
                    "reply": reply,
                    "action": None,
                    "extracted": slots
                }

            # CASE 4: Destination known, Source missing (e.g. "train to Kanpur tomorrow")
            if dst and not src:
                if effective_lang == "hindi":
                    reply = f"आप **{dst_name}** जाने के लिए किस स्टेशन से ट्रेन पकड़ना चाहते हैं?"
                elif effective_lang == "english":
                    reply = f"Which station will you be boarding from to travel to **{dst_name}**?"
                else:
                    reply = f"Aap **{dst_name}** jaane ke liye kaunse station se board karna chahte hain?"
                return {
                    "reply": reply,
                    "action": None,
                    "extracted": slots
                }

            # CASE 5: Source and Destination known, but Month is missing (Day is known)
            if src and dst and day and not month and not dt:
                if effective_lang == "hindi":
                    reply = f"आप **{src_name}** से **{dst_name}** के लिए कौन से महीने की {day} तारीख को यात्रा करना चाहते हैं (जैसे सितंबर या अक्टूबर)?"
                elif effective_lang == "english":
                    reply = f"Which month's {day}th would you like to travel from **{src_name}** to **{dst_name}** (e.g. September or October)?"
                else:
                    reply = f"Aap **{src_name}** se **{dst_name}** ke liye kaunse mahine ki {day} tareekh ko travel karna chahte hain (jaise September ya October)?"
                return {
                    "reply": reply,
                    "action": None,
                    "extracted": slots
                }

            # CASE 6: Source and Destination known, but Date is completely missing
            if src and dst and not dt:
                if effective_lang == "hindi":
                    reply = f"आप **{src_name}** से **{dst_name}** के लिए किस तारीख को यात्रा करना चाहते हैं? (जैसे 'आज', 'कल' या कोई विशेष तारीख)"
                elif effective_lang == "english":
                    reply = f"On which date would you like to travel from **{src_name}** to **{dst_name}**? (e.g. 'today', 'tomorrow', or a specific date)"
                else:
                    reply = f"Aap **{src_name}** se **{dst_name}** ke liye kis date par travel karna chahte hain? (Jaise 'aaj', 'kal' ya koi specific date)"
                return {
                    "reply": reply,
                    "action": None,
                    "extracted": slots
                }

        # If conversational chit-chat or general question, query Gemini with 3.5s timeout
        system_instruction = f"""
You are Safarnama AI, a very helpful, friendly, and knowledgeable Indian Railways journey assistant.
Language rule: If user writes in Hindi (Devanagari), reply purely in polite Hindi.
If user writes in English, reply purely in polite English.
If user writes in Hinglish, reply in warm, polite conversational Hinglish.
Keep responses concise, polite, and under 3 sentences.
"""
        prompt = f"""User message: "{user_message}"\nProvide a direct, helpful, and polite answer."""
        gemini_reply, err = call_gemini(prompt, system_instruction=system_instruction, temperature=0.3)

        if gemini_reply and not err:
            return {
                "reply": gemini_reply.strip(),
                "action": None,
                "extracted": slots
            }

        # Graceful fast fallback if Gemini is offline
        return self._heuristic_fallback(user_message, slots, effective_lang)

    def _heuristic_fallback(self, msg: str, slots=None, lang="hinglish"):
        """Instant polite fallback when Gemini is unreachable."""
        if lang == "hindi":
            return {
                "reply": "नमस्ते! कृपया बताएं आप किस स्टेशन से कहाँ तक और किस तारीख को यात्रा करना चाहते हैं? (जैसे: 'लखनऊ से कानपुर कल सुबह')",
                "action": None,
                "extracted": slots or {}
            }
        elif lang == "english":
            return {
                "reply": "Hello! Please tell me your boarding station, destination, and travel date (e.g., 'Lucknow to Kanpur tomorrow morning').",
                "action": None,
                "extracted": slots or {}
            }
        else:
            return {
                "reply": "Namaste ji! Kripya batayein aap kaunse station se kahan tak aur kis date par travel karna chahte hain? (Jaise: *'Lucknow se Kanpur kal subah'*).",
                "action": None,
                "extracted": slots or {}
            }
