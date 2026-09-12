import csv
import glob
import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
RAW_DIR = DATA_DIR / 'Rail raw all datasets'

EXTRA_STATION_COORDS = {
    'AP': {'name': 'Ashokapuram (Mysuru)', 'state': 'Karnataka', 'lat': 12.2789, 'lon': 76.6433},
    'APR': {'name': 'Anuppur Junction', 'state': 'Madhya Pradesh', 'lat': 23.1114, 'lon': 81.6917},
    'BGY': {'name': 'Bagewadi', 'state': 'Karnataka', 'lat': 16.5744, 'lon': 75.9811},
    'BIB': {'name': 'Birur Junction', 'state': 'Karnataka', 'lat': 13.6214, 'lon': 75.9722},
    'BMPR': {'name': 'Badampahar', 'state': 'Odisha', 'lat': 22.0833, 'lon': 86.1167},
    'BRML': {'name': 'Baramulla', 'state': 'Jammu & Kashmir', 'lat': 34.2094, 'lon': 74.3431},
    'CIA': {'name': 'Chharodi', 'state': 'Gujarat', 'lat': 23.0833, 'lon': 72.3333},
    'CKU': {'name': 'Chakulia', 'state': 'Jharkhand', 'lat': 22.4786, 'lon': 86.7167},
    'DEEG': {'name': 'Deeg', 'state': 'Rajasthan', 'lat': 27.4714, 'lon': 77.3244},
    'DSPL': {'name': 'Daspalla', 'state': 'Odisha', 'lat': 20.3500, 'lon': 84.8500},
    'EKNR': {'name': 'Ekta Nagar (Kevadiya)', 'state': 'Gujarat', 'lat': 21.8319, 'lon': 73.6847},
    'GUA': {'name': 'Gua', 'state': 'Jharkhand', 'lat': 22.2167, 'lon': 85.3833},
    'HAS': {'name': 'Hassan Junction', 'state': 'Karnataka', 'lat': 13.0072, 'lon': 76.1044},
    'JRBI': {'name': 'Jorbira', 'state': 'Odisha', 'lat': 22.1333, 'lon': 85.8000},
    'KQZ': {'name': 'Kolar', 'state': 'Karnataka', 'lat': 13.1367, 'lon': 78.1292},
    'KRMR': {'name': 'Karimnagar', 'state': 'Telangana', 'lat': 18.4239, 'lon': 79.1417},
    'KTRD': {'name': 'Kavathe Mahankal', 'state': 'Maharashtra', 'lat': 16.9833, 'lon': 74.8833},
    'MASS': {'name': 'MGR Chennai Central Suburban', 'state': 'Tamil Nadu', 'lat': 13.0827, 'lon': 80.2755},
    'MSAE': {'name': 'Masagram', 'state': 'West Bengal', 'lat': 23.1833, 'lon': 88.0833},
    'ROP': {'name': 'Rupsa Junction', 'state': 'Odisha', 'lat': 21.6036, 'lon': 87.0167},
    'RPHR': {'name': 'Raipur Haryana', 'state': 'Haryana', 'lat': 29.8667, 'lon': 76.8167},
    'SGDN': {'name': 'Shravanabelagola', 'state': 'Karnataka', 'lat': 12.8583, 'lon': 76.4889},
    'UBR': {'name': 'Umargam Road', 'state': 'Gujarat', 'lat': 20.1833, 'lon': 72.7500},
    'VTA': {'name': 'Vatva', 'state': 'Gujarat', 'lat': 22.9667, 'lon': 72.6333},
    'VTDI': {'name': 'Vadtal Swaminarayan', 'state': 'Gujarat', 'lat': 22.5833, 'lon': 72.8667},
    'VZR': {'name': 'Valivade', 'state': 'Maharashtra', 'lat': 16.7167, 'lon': 74.2833},
    'CLA': {'name': 'Kurla Junction (Mumbai)', 'state': 'Maharashtra', 'lat': 19.0688, 'lon': 72.8887},
    'KSRA': {'name': 'Kasara', 'state': 'Maharashtra', 'lat': 19.3242, 'lon': 73.4844},
    'SIPT': {'name': 'Shahabad Mohamadpur', 'state': 'Delhi', 'lat': 28.5667, 'lon': 77.0667},
    'KHPI': {'name': 'Khopoli', 'state': 'Maharashtra', 'lat': 18.7844, 'lon': 73.3444},
    'BUD': {'name': 'Badlapur', 'state': 'Maharashtra', 'lat': 19.1667, 'lon': 73.2333},
    'ABH': {'name': 'Ambarnath', 'state': 'Maharashtra', 'lat': 19.2000, 'lon': 73.1833},
    'VAA': {'name': 'Bhaga Junction', 'state': 'Jharkhand', 'lat': 23.7333, 'lon': 86.4167},
    'JI': {'name': 'Jhajjar', 'state': 'Haryana', 'lat': 28.6083, 'lon': 76.6583},
    'CBY': {'name': 'Khambhat', 'state': 'Gujarat', 'lat': 22.3167, 'lon': 72.6167},
    'SONA': {'name': 'Sonada', 'state': 'West Bengal', 'lat': 26.9667, 'lon': 88.2667},
    'DK': {'name': 'Dhoraji', 'state': 'Gujarat', 'lat': 21.7333, 'lon': 70.4500},
    'CPT': {'name': 'Channapatna', 'state': 'Karnataka', 'lat': 12.6500, 'lon': 77.2000},
    'DIT': {'name': 'Dohrighat', 'state': 'Uttar Pradesh', 'lat': 26.0333, 'lon': 83.5167},
    'GPNB': {'name': 'Gopanapalli', 'state': 'Telangana', 'lat': 17.3833, 'lon': 78.3333},
    'KNF': {'name': 'Kankavali', 'state': 'Maharashtra', 'lat': 16.2667, 'lon': 73.7167},
}

CATEGORY_TAG_MAP = {
    'Hi-speed Vande Bharat Trains': 'Vande Bharat',
    'VB Sleeper Trainsnew': 'VB Sleeper',
    'Namo Bharat Rapid Rail': 'Namo Bharat',
    'Modern LHB Trains': 'LHB Coach',
    'Trains providing Bedroll': 'Bedroll',
    'Fastest Trains': 'High Speed',
    'Special Fare Trains': 'Special Fare',
    'Seasonal&Festival Special Trains': 'Festival Special',
    'Summer Special Trains': 'Summer Special',
    'Longest Train Routes': 'Long Route',
    'Speeded Up': 'Speeded Up',
}

def parse_duration_min(dur_str: str) -> int:
    if not dur_str:
        return 0
    h_m = re.findall(r'(\d+)\s*h', dur_str)
    m_m = re.findall(r'(\d+)\s*m', dur_str)
    h = int(h_m[0]) if h_m else 0
    m = int(m_m[0]) if m_m else 0
    return h * 60 + m

def parse_distance_km(dist_str: str) -> float:
    if not dist_str:
        return 0.0
    m = re.search(r'([\d\.]+)', dist_str)
    return float(m.group(1)) if m else 0.0

def parse_speed_kmh(speed_str: str) -> float:
    if not speed_str:
        return 0.0
    m = re.search(r'([\d\.]+)', speed_str)
    return float(m.group(1)) if m else 0.0

def parse_halts_count(halts_str: str) -> int:
    if not halts_str:
        return 0
    m = re.search(r'(\d+)', halts_str)
    return int(m.group(1)) if m else 0

def parse_dep_days(dep_days_str: str) -> str:
    if not dep_days_str:
        return ''
    s = dep_days_str.strip()
    if s.lower() == 'daily' or s == 'S M T W T F S':
        return 'sun,mon,tue,wed,thu,fri,sat'
    tokens = s.split()
    if not tokens:
        return ''
    day_names = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    day_letters = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
    result = []
    t_idx = 0
    for slot_idx, expected_letter in enumerate(day_letters):
        if t_idx < len(tokens) and tokens[t_idx] == expected_letter:
            result.append(day_names[slot_idx])
            t_idx += 1
    if result and t_idx == len(tokens):
        return ','.join(result)
    if len(tokens) == 1:
        tok = tokens[0].upper()
        if tok == 'M': return 'mon'
        if tok == 'T': return 'tue,thu'
        if tok == 'W': return 'wed'
        if tok == 'F': return 'fri'
        if tok == 'S': return 'sat,sun'
    return ','.join(result) if result else s.lower()

def parse_date_mm_dd(date_str: str) -> str:
    if not date_str or not date_str.strip():
        return ''
    months = {
        'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04',
        'may': '05', 'jun': '06', 'jul': '07', 'aug': '08',
        'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
    }
    m = re.search(r'(\d+)\s*-\s*([a-zA-Z]+)', date_str.strip())
    if m:
        day = int(m.group(1))
        mon_str = m.group(2).lower()[:3]
        if mon_str in months:
            return f'{months[mon_str]}-{day:02d}'
    return ''

def calculate_estimated_cost_inr(distance_km: float, train_type: str, classes: str) -> float:
    d = max(10.0, distance_km)
    t = train_type.upper()
    if 'VB' in t or 'VANDE' in t:
        cost = d * 1.35 + 160
    elif 'RAJ' in t or 'SHAT' in t or 'DRNT' in t:
        cost = d * 1.20 + 140
    elif 'SF' in t:
        cost = d * 0.52 + 75
    elif 'EXP' in t or 'MAIL' in t:
        cost = d * 0.46 + 55
    elif 'PASS' in t or 'MEMU' in t or 'EMU' in t:
        cost = d * 0.25 + 25
    else:
        cost = d * 0.48 + 50
    return round(max(35.0, cost), 1)

def process_all_datasets():
    print(f'Reading raw IndiaRailInfo CSV files from: {RAW_DIR}')
    csv_files = glob.glob(str(RAW_DIR / '*.csv'))
    print(f'Found {len(csv_files)} datasets.')
    trains_dict = {}
    stations_used = set()

    for fpath in csv_files:
        cat_name = Path(fpath).stem
        tag = CATEGORY_TAG_MAP.get(cat_name, '')
        with open(fpath, mode='r', encoding='utf-8-sig', errors='ignore') as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                train_no = row.get('Train No', '').strip()
                name = row.get('Name', '').strip()
                src = row.get('From', '').strip().upper()
                dst = row.get('To', '').strip().upper()
                if not train_no or not src or not dst:
                    continue
                stations_used.add(src)
                stations_used.add(dst)
                dur_min = parse_duration_min(row.get('Duration', ''))
                dist_km = parse_distance_km(row.get('Distance', ''))
                speed_kmh = parse_speed_kmh(row.get('Speed', ''))
                halts = parse_halts_count(row.get('Halts', ''))
                run_days = parse_dep_days(row.get('Dep Days', ''))
                valid_from = parse_date_mm_dd(row.get('Date From', ''))
                valid_to = parse_date_mm_dd(row.get('Date To', ''))
                train_type = row.get('Type', '').strip()
                zone = row.get('Zone', '').strip()
                classes = row.get('Classes', '').strip()
                dep_time = row.get('Dep', '').strip()
                arr_time = row.get('Arr', '').strip()
                return_train = row.get('Return', '').strip()

                if dep_time and ':' in dep_time:
                    p = dep_time.split(':')
                    dep_time = f'{int(p[0]):02d}:{int(p[1]):02d}'
                if arr_time and ':' in arr_time:
                    p = arr_time.split(':')
                    arr_time = f'{int(p[0]):02d}:{int(p[1]):02d}'

                cost_inr = calculate_estimated_cost_inr(dist_km, train_type, classes)

                if train_no not in trains_dict:
                    trains_dict[train_no] = {
                        'train_number': train_no,
                        'train_name': name,
                        'source': src,
                        'destination': dst,
                        'train_type': train_type,
                        'zone': zone,
                        'dep_time': dep_time,
                        'arr_time': arr_time,
                        'duration_min': dur_min,
                        'distance_km': dist_km,
                        'speed_kmh': speed_kmh,
                        'halts': halts,
                        'run_days': run_days,
                        'valid_from': valid_from,
                        'valid_to': valid_to,
                        'classes': classes,
                        'cost_inr': cost_inr,
                        'return_train': return_train,
                        'tags': set(),
                    }

                if tag:
                    trains_dict[train_no]['tags'].add(tag)
                if 'Vande Bharat' in name or train_type in ('VB', 'VBS'):
                    trains_dict[train_no]['tags'].add('Vande Bharat')
                if 'Namo Bharat' in name or train_type == 'NB':
                    trains_dict[train_no]['tags'].add('Namo Bharat')
                if 'Special' in name and 'Special' not in trains_dict[train_no]['tags']:
                    trains_dict[train_no]['tags'].add('Special')

                rec = trains_dict[train_no]
                if not rec['dep_time'] and dep_time: rec['dep_time'] = dep_time
                if not rec['arr_time'] and arr_time: rec['arr_time'] = arr_time
                if rec['duration_min'] <= 0 and dur_min > 0: rec['duration_min'] = dur_min
                if rec['distance_km'] <= 0 and dist_km > 0: rec['distance_km'] = dist_km
                if not rec['run_days'] and run_days: rec['run_days'] = run_days
                if not rec['classes'] and classes: rec['classes'] = classes
                if not rec['zone'] and zone: rec['zone'] = zone
                if not rec['return_train'] and return_train: rec['return_train'] = return_train

    print(f'Compiled {len(trains_dict)} unique trains across {len(stations_used)} stations.')

    routes_iri_path = DATA_DIR / 'routes_iri.csv'
    with open(routes_iri_path, mode='w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow([
            'source', 'destination', 'mode', 'duration_min', 'cost_inr',
            'train_number', 'train_name', 'available', 'date', 'dep_time',
            'arr_time', 'valid_from', 'valid_to', 'run_days'
        ])
        for tno, rec in sorted(trains_dict.items()):
            writer.writerow([
                rec['source'],
                rec['destination'],
                'train',
                rec['duration_min'],
                rec['cost_inr'],
                rec['train_number'],
                rec['train_name'],
                'true',
                '',
                rec['dep_time'],
                rec['arr_time'],
                rec['valid_from'],
                rec['valid_to'],
                rec['run_days']
            ])
    print(f'Generated {routes_iri_path} with {len(trains_dict)} routes.')

    stations_iri_path = DATA_DIR / 'stations_iri.csv'
    with open(stations_iri_path, mode='w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(['code', 'name', 'state', 'lat', 'lon'])
        for code, info in EXTRA_STATION_COORDS.items():
            writer.writerow([code, info['name'], info['state'], info['lat'], info['lon']])
    print(f'Updated {stations_iri_path} with {len(EXTRA_STATION_COORDS)} extra stations.')

    metadata_out = {}
    for tno, rec in trains_dict.items():
        metadata_out[tno] = {
            'name': rec['train_name'],
            'type': rec['train_type'],
            'zone': rec['zone'],
            'classes': rec['classes'],
            'halts': rec['halts'],
            'speed_kmh': rec['speed_kmh'],
            'distance_km': rec['distance_km'],
            'tags': sorted(list(rec['tags'])),
            'return_train': rec['return_train'],
        }

    meta_json_path = DATA_DIR / 'train_metadata.json'
    with open(meta_json_path, mode='w', encoding='utf-8') as fp:
        json.dump(metadata_out, fp, indent=2, ensure_ascii=False)
    print(f'Generated {meta_json_path} with rich train tags and attributes.')

if __name__ == '__main__':
    process_all_datasets()
