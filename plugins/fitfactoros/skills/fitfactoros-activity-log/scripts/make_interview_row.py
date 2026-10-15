#!/usr/bin/env python3
"""Build one FitFactorOS Interviews row (11 columns, A-K) as a tab-separated line.

Usage:
  python3 make_interview_row.py job_id=J-261011-NORTHWIND date=2026-10-09 round="Hiring manager" \
    interviewer="Pat L." interviewer_title="Director, Customer Success" format=Video \
    learned="Team doubled this year; next step is a panel" thank_you=No

Leave out any field that is blank. Prints exactly 11 fields (10 tabs) or exits with an error.
"""
import re, sys

KEYS = ["job_id", "date", "round", "interviewer", "interviewer_title", "format",
        "asked", "learned", "thank_you", "email_link", "notes"]
LISTS = {"format": ["Phone", "Video", "On-site"], "thank_you": ["Yes", "No"]}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def fail(msg):
    sys.exit("ERROR: " + msg)

v = {}
for arg in sys.argv[1:]:
    if "=" not in arg:
        fail(f"'{arg}' is not key=value")
    k, val = arg.split("=", 1)
    k, val = k.strip().lower(), val.strip()
    if k not in KEYS:
        fail(f"unknown field '{k}'. Allowed: {', '.join(KEYS)}")
    if "\t" in val or "\n" in val or "\r" in val:
        fail(f"{k} contains a tab or line break")
    if val[:1] in ("=", "+", "-", "@", '"'):
        fail(f"{k} starts with a character Sheets treats as a formula")
    if k in LISTS and val and val not in LISTS[k]:
        fail(f"{k} must be one of: {', '.join(LISTS[k])}")
    if k == "date" and val and not DATE.match(val):
        fail("date must be YYYY-MM-DD")
    v[k] = val

if not v.get("date"):
    fail("date is required")
if not v.get("interviewer") and not v.get("round"):
    fail("give at least the round or the interviewer")

line = "\t".join(v.get(k, "") for k in KEYS)
assert line.count("\t") == 10
print(line)
