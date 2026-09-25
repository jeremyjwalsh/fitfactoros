#!/usr/bin/env python3
"""Build one FitFactorOS Activity row (columns A-O) as a tab-separated line.

Usage:
  python3 make_row.py date=2026-09-24 week_ending=2026-09-26 type=Applied \
    company="Northwind" method="Online application" position="Enablement Manager" \
    result="Submitted application" counts=Yes contact_info="https://example.com/job"

Leave out any field that is blank. Prints exactly 15 fields (14 tabs) or exits with an error.
"""
import re, sys

FIELDS = [  # (column, key)
    ("A", "date"), ("B", "week_ending"), ("C", "job_id"), ("D", "type"),
    ("E", "company"), ("F", "contact_person"), ("G", "method"), ("H", "position"),
    ("I", "result"), ("J", "counts"), ("K", "email_link"), ("L", "notes"),
    ("M", "pay_rate"), ("N", "employer_address"), ("O", "contact_info"),
]
LISTS = {
    "type": ["Applied", "Reviewed job posting", "Outreach message", "Networking contact",
             "Informational interview", "Interview", "Job fair", "Workshop or training", "Other"],
    "method": ["Email", "Phone", "In person", "Video", "Online application", "Other"],
    "counts": ["Yes", "No"],
}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def fail(msg):
    sys.exit("ERROR: " + msg)

keys = [k for _, k in FIELDS]
values = {}
for arg in sys.argv[1:]:
    if "=" not in arg:
        fail(f"'{arg}' is not key=value")
    k, v = arg.split("=", 1)
    k = k.strip().lower()
    if k not in keys:
        fail(f"unknown field '{k}'. Allowed: {', '.join(keys)}")
    v = v.strip()
    if "\t" in v or "\n" in v or "\r" in v:
        fail(f"{k} contains a tab or line break")
    if v[:1] in ("=", "+", "-", "@", '"'):
        fail(f"{k} starts with a character Sheets treats as a formula")
    if k in LISTS and v and v not in LISTS[k]:
        fail(f"{k} must be one of: {', '.join(LISTS[k])}")
    if k in ("date", "week_ending") and v and not DATE.match(v):
        fail(f"{k} must be YYYY-MM-DD")
    values[k] = v

if not values.get("date"):
    fail("date is required")

row = [values.get(k, "") for k in keys]
assert len(row) == 15
line = "\t".join(row)
assert line.count("\t") == 14
print(line)
