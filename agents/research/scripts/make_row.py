#!/usr/bin/env python3
"""Build one FitFactorOS Jobs row (21 columns, A-U) or Evidence row (8 columns, A-H)
as a tab-separated line.

Usage:
  python3 make_row.py jobs job_id=J-261011-NORTHWIND date=2026-10-11 company="Northwind" \
    role="Enablement Manager" link="https://example.com/job" source="Company site" \
    location="Massachusetts - Remote (+3 more)" work_mode=Remote pay="Not posted" \
    fit=62 screen=Maybe path=Cold next_step="Ask the recruiter for the pay range" \
    next_date=2026-10-11 status=Active notes="Company fit 55/100. Blocker: ..."

  python3 make_row.py evidence job_id=J-261011-NORTHWIND date=2026-10-11 \
    claim="Posted pay is $150,000 to $170,000." tag=Verified link="https://example.com/job" \
    source_type="Job posting" how="Stated in the pay section" by=Agent

Leave out any field that is blank. Prints exactly one row or exits with an error.
"""
import re, sys

TABS = {
    "jobs": [
        ("A", "job_id"), ("B", "date"), ("C", "company"), ("D", "role"), ("E", "link"),
        ("F", "source"), ("G", "suggested_by"), ("H", "location"), ("I", "work_mode"),
        ("J", "pay"), ("K", "pay_tag"), ("L", "fit"), ("M", "screen"), ("N", "path"),
        ("O", "warm_contact"), ("P", "ladder"), ("Q", "next_step"), ("R", "next_date"),
        ("S", "status"), ("T", "email_link"), ("U", "notes"),
    ],
    "evidence": [
        ("A", "job_id"), ("B", "date"), ("C", "claim"), ("D", "tag"), ("E", "link"),
        ("F", "source_type"), ("G", "how"), ("H", "by"),
    ],
}
LISTS = {
    "source": ["Job board", "Company site", "Referral", "Conversation", "Recruiter", "Job Finder", "Other"],
    "work_mode": ["Remote", "Hybrid", "On-site"],
    "pay_tag": ["Verified"],
    "screen": ["Pursue", "Maybe", "Pass"],
    "path": ["Warm", "Cold"],
    "ladder": ["Picked", "Researched", "Found the right person", "Reached out to contact",
               "Sent a researched note", "Applied", "Heard back", "Interviewing", "Offer"],
    "status": ["Active", "Passed", "Closed – offer", "Closed – no", "Withdrawn"],
    "tag": ["Verified", "Estimated", "Inferred"],
    "source_type": ["Job posting", "Company site", "Filing", "News", "Person", "Your records", "Other"],
    "by": ["Agent"],
}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
JOB_ID = re.compile(r"^J-\d{6}-[A-Z0-9]{1,10}(-\d+)?$")

def fail(msg):
    sys.exit("ERROR: " + msg)

if len(sys.argv) < 2 or sys.argv[1] not in TABS:
    fail("first argument must be 'jobs' or 'evidence'")
tab = sys.argv[1]
keys = [k for _, k in TABS[tab]]
v = {}
for arg in sys.argv[2:]:
    if "=" not in arg:
        fail(f"'{arg}' is not key=value")
    k, val = arg.split("=", 1)
    k, val = k.strip().lower(), val.strip()
    if k not in keys:
        fail(f"unknown {tab} field '{k}'. Allowed: {', '.join(keys)}")
    if "\t" in val or "\n" in val or "\r" in val:
        fail(f"{k} contains a tab or line break")
    if val[:1] in ("=", "+", "-", "@", '"'):
        fail(f"{k} starts with a character Sheets treats as a formula")
    if val.lower() in ("blank", "skipped", "n/a"):
        fail(f"{k}: leave blank fields out instead of writing '{val}'")
    if k in LISTS and val and val not in LISTS[k]:
        fail(f"{k} must be one of: {', '.join(LISTS[k])}")
    if k in ("date", "next_date") and val and not DATE.match(val):
        fail(f"{k} must be YYYY-MM-DD")
    v[k] = val

for req in ("job_id", "date"):
    if not v.get(req):
        fail(f"{req} is required")
if not JOB_ID.match(v["job_id"]):
    fail("job_id must look like J-YYMMDD-COMPANY (capitals and digits, up to 10)")

if tab == "jobs":
    for req in ("company", "role", "pay", "fit", "screen", "path", "status"):
        if not v.get(req):
            fail(f"{req} is required")
    if not v["fit"].isdigit() or not 0 <= int(v["fit"]) <= 100:
        fail("fit must be a whole number 0-100")
    if v["pay"] == "Not posted" and v.get("pay_tag"):
        fail("pay_tag must be blank when pay is Not posted")
    if v["pay"] != "Not posted" and v.get("pay_tag") != "Verified":
        fail("posted pay needs pay_tag=Verified")
    if v["path"] == "Warm" and not v.get("warm_contact"):
        fail("Warm path needs warm_contact")
    if v["path"] == "Cold" and v.get("warm_contact"):
        fail("Cold path must leave warm_contact blank")
    if v["screen"] == "Pass":
        if v["status"] not in ("Passed", "Withdrawn", "Closed – no"):
            fail("Pass needs status=Passed")
        if v.get("next_step") or v.get("next_date"):
            fail("Pass leaves next_step and next_date blank")
    elif v["status"] == "Active":
        if not v.get("next_step") or not v.get("next_date"):
            fail(f"{v['screen']} needs next_step and next_date")
    if v["screen"] == "Pursue" and not v.get("ladder"):
        fail("Pursue needs a ladder stage: Picked, or the furthest real step reached (Researched, Applied, Interviewing, ...)")
    if not v.get("notes", "").startswith("Company fit"):
        fail("notes must start with 'Company fit'")
else:
    for req in ("claim", "tag", "source_type", "how"):
        if not v.get(req):
            fail(f"{req} is required")
    v.setdefault("by", "Agent")
    if v["source_type"] == "News" and v["tag"] == "Verified":
        fail("a News source can't be Verified; use Estimated ('reported by ..., not confirmed by the company')")
    if v["tag"] == "Verified" and v["source_type"] in ("Other",):
        fail("Verified needs a primary source: Job posting, Company site, Filing, Person, or Your records")

row = [v.get(k, "") for k in keys]
line = "\t".join(row)
assert line.count("\t") == len(keys) - 1
print(line)
