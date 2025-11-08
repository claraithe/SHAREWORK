#!/usr/bin/env python3

import os
import re
import calendar
from datetime import datetime
import pandas as pd
import pdfplumber

INPUT_DIR = "2024_DATA"
OUTPUT_DIR = "2024_OUTPUT"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Map italian month names to month number
ITALIAN_MONTHS = {
    "GENNAIO":1,"FEBBRAIO":2,"MARZO":3,"APRILE":4,"MAGGIO":5,"GIUGNO":6,
    "LUGLIO":7,"AGOSTO":8,"SETTEMBRE":9,"OTTOBRE":10,"NOVEMBRE":11,"DICEMBRE":12
}

WEEKDAY_IT = {0: "LUN", 1: "MAR", 2: "MER", 3: "GIO", 4: "VEN", 5: "SAB", 6: "DOM"}

# Convert "HH:MM" to numeric H.MM (minutes as two decimal digits)
def time_to_numeric(timestr):
    try:
        h, m = map(int, timestr.split(':'))
        return h + (m / 100.0)
    except Exception:
        return None

# Extract raw text from PDF using pdfplumber
def pdf_to_text(path):
    text_parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                text_parts.append(txt)
    return "\n".join(text_parts)

# Parse a month's text into rows
def parse_month_text(text, year, month_number):
    # Normalize
    txt = text.replace('\r', '\n')
    lines = [l.rstrip() for l in txt.splitlines()]
    joined = '\n'.join(lines)

    # Heuristic segmentation: split on lines that start with day number
    segments = re.split(r'\n(?=\s*(?:[1-9]|[12][0-9]|3[01])\b)', joined)
    rows = []
    for seg in segments:
        seg = seg.strip()
        if not seg:
            continue
        m = re.match(r'(?P<day>\d{1,2})\b[\s\S]*(?P<body>.*)', seg, re.DOTALL)
        if not m:
            continue
        day = int(m.group('day'))
        body = m.group('body').strip()
        # Find first time range
        tm = re.search(r'(\d{1,2}:\d{2})\s*[-–—]\s*(\d{1,2}:\d{2})', body)
        time_from = tm.group(1) if tm else None
        time_to = tm.group(2) if tm else None
        if tm:
            activity_part = body[:tm.start()].strip()
        else:
            activity_part = body.split('\n',1)[0].strip()
        # Determine desc1/desc2: split by ' - ' or ':' or first comma (heuristic)
        desc1 = ''
        desc2 = ''
        if ' - ' in activity_part:
            p = activity_part.split(' - ',1)
            desc1 = p[0].strip(); desc2 = p[1].strip()
        elif ':' in activity_part:
            p = activity_part.split(':',1)
            desc1 = p[0].strip(); desc2 = p[1].strip()
        elif ',' in activity_part:
            p = activity_part.split(',',1)
            desc1 = p[0].strip(); desc2 = p[1].strip()
        else:
            desc1 = activity_part; desc2 = ''
        try:
            date_obj = datetime(year=year, month=month_number, day=day)
        except Exception:
            date_obj = None
        rows.append({
            'date': date_obj,
            'activity': activity_part,
            'desc1': desc1,
            'desc2': desc2,
            'time_from': time_from,
            'time_to': time_to
        })
    return rows

# Process a single PDF file path
def process_pdf_file(pdf_path):
    fname = os.path.basename(pdf_path)
    m = re.match(r'([A-Za-z]+)[_ ]?(\d{4})', fname)
    if not m:
        print('Could not infer month/year from filename:', fname)
        return None
    month_name = m.group(1).upper()
    year = int(m.group(2))
    month_index = ITALIAN_MONTHS.get(month_name)
    if not month_index:
        print('Unknown month name:', month_name)
        return None
    text = pdf_to_text(pdf_path)
    rows = parse_month_text(text, year, month_index)
    out_rows = []
    for r in rows:
        date = r['date']
        daycode = WEEKDAY_IT[date.weekday()] if date else ''
        tf = time_to_numeric(r['time_from']) if r['time_from'] else None
        tt = time_to_numeric(r['time_to']) if r['time_to'] else None
        out_rows.append({
            'A_date': date,
            'B_day': daycode,
            'C_activity': r['activity'],
            'D_desc1': r['desc1'],
            'E_desc2': r['desc2'],
            'F_time_from': tf,
            'G_time_to': tt
        })
    df = pd.DataFrame(out_rows, columns=['A_date','B_day','C_activity','D_desc1','E_desc2','F_time_from','G_time_to'])
    return month_name, year, df


def main():
    files = sorted([f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.pdf')])
    if not files:
        print('No PDF files found in', INPUT_DIR)
        return
    for f in files:
        path = os.path.join(INPUT_DIR, f)
        print('Processing', path)
        res = process_pdf_file(path)
        if not res:
            print('Skipping', f)
            continue
        month_name, year, df = res
        out_name = f"{month_name} {year}.xlsx"
        out_path = os.path.join(OUTPUT_DIR, out_name)
        if not df.empty:
            df['A_date'] = pd.to_datetime(df['A_date'])
        with pd.ExcelWriter(out_path, engine='openpyxl', datetime_format='yyyy-mm-dd', date_format='yyyy-mm-dd') as writer:
            df.to_excel(writer, index=False, sheet_name=month_name)
        print('Saved', out_path)

if __name__ == '__main__':
    main()
