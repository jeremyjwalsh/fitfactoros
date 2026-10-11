#!/usr/bin/env python3
"""Fill the dashboard template with data.

Usage: python3 fill.py data.json out.html
Checks the data shape, then writes the template with the data block filled in.
"""
import json, sys, pathlib

CALLS = {"Pursue", "Maybe", "Pass"}
RUNGS = {"", "Picked", "Researched", "Found the right person", "Reached out to contact",
         "Sent a researched note", "Applied", "Heard back", "Interviewing", "Offer"}
TAGS = {"V", "E", "I"}

def fail(msg):
    sys.exit(f"STOP: {msg}")

data = json.loads(pathlib.Path(sys.argv[1]).read_text())
for k in ("sheet", "readAt", "jobs", "activities"):
    if k not in data:
        fail(f"missing '{k}'")
for j in data["jobs"]:
    if "EXAMPLE" in j.get("id", "").upper():
        fail(f"example row included: {j['id']}")
    for k in ("id", "date", "co", "role", "call", "path"):
        if not j.get(k):
            fail(f"job {j.get('id')} is missing '{k}'")
    if j["call"] not in CALLS:
        fail(f"job {j['id']}: call must be Pursue, Maybe or Pass")
    if j["path"] not in ("Warm", "Cold"):
        fail(f"job {j['id']}: path must be Warm or Cold")
    if j.get("stage", "") not in RUNGS:
        fail(f"job {j['id']}: unknown ladder stage '{j['stage']}'")
    for e in j.get("ev", []):
        if len(e) != 2 or e[0] not in TAGS:
            fail(f"job {j['id']}: evidence must be [V|E|I, text]")
for a in data["activities"]:
    if "EXAMPLE" in a.get("notes", "").upper():
        fail("example activity row included")

tpl = (pathlib.Path(__file__).parent.parent / "assets" / "template.html").read_text()
blob = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
pathlib.Path(sys.argv[2]).write_text(tpl.replace("__DATA__", blob, 1))
print(f"OK: {len(data['jobs'])} jobs, {len(data['activities'])} activities -> {sys.argv[2]}")
