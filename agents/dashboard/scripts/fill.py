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

# Pre-render the same view the script draws, so exports, PDFs and link
# previews show real content. The page's script redraws it on load.
import datetime, html
E = lambda x: html.escape(str(x if x is not None else ""))
LADDER = ["Picked", "Researched", "Found the right person", "Reached out to contact",
          "Sent a researched note", "Applied", "Heard back", "Interviewing", "Offer"]
TAGNAME = {"V": "Verified", "E": "Estimated", "I": "Inferred"}
def d(x):
    try: return datetime.date.fromisoformat((x or "")[:10])
    except ValueError: return None
fmt = lambda x: x.strftime("%b ") + str(x.day)
today = d(data["readAt"]) or datetime.date.today()
ws = today - datetime.timedelta(days=(today.weekday() + 1) % 7); we = ws + datetime.timedelta(days=6)
inweek = lambda x: d(x) is not None and ws <= d(x) <= we
order = {"Pursue": 0, "Maybe": 1, "Pass": 2}
jobs = sorted(data["jobs"], key=lambda j: (order.get(j["call"], 1), -(j.get("fit") or 0)))
acts = data["activities"]
counted = sum(1 for a in acts if inweek(a.get("date")) and a.get("counts") == "Yes")
mn = int(data.get("weeklyMin") or 0)
warm = [j for j in jobs if j["path"] == "Warm"]; cold = [j for j in jobs if j["path"] != "Warm"]
far = lambda l: sum(1 for j in l if j.get("stage") in LADDER and LADDER.index(j["stage"]) >= 7)
dated = sorted([a for a in acts if a.get("date")], key=lambda a: a["date"], reverse=True)
last = dated[0] if dated else None
meter = ('<div class="meter" aria-hidden="true">' + "".join(
    f'<span class="{"on" if i < counted else ""}"></span>' for i in range(mn)) + "</div>") if mn else ""
strip = (f'<div class="tile"><div class="eyebrow">This week · {fmt(ws)}–{fmt(we)}</div><div class="big">{counted}{" of " + str(mn) if mn else ""}</div><div class="sub">Activities logged that count for unemployment</div>{meter}</div>'
  f'<div class="tile"><div class="eyebrow">Screened this week</div><div class="big">{sum(1 for j in jobs if inweek(j["date"]))}</div><div class="sub">Jobs you fit factored, Passes included</div></div>'
  f'<div class="tile"><div class="eyebrow">Warm vs cold</div><div class="big">{len(warm)} · {len(cold)}</div><div class="sub">Reached Interviewing: warm {far(warm)}, cold {far(cold)}</div></div>'
  '<div class="tile"><div class="eyebrow">Last step taken</div><div class="big" style="font-size:18px;font-family:var(--body);font-weight:600">'
  + (E(last["type"] + (", " + last["co"] if last.get("co") else "")) if last else "Nothing logged yet") + '</div><div class="sub">'
  + (E(fmt(d(last["date"])) + (" · " + last["result"] if last.get("result") else "")) if last else "") + "</div></div>")
pill = lambda c: "V" if c == "Pursue" else "parked" if c == "Maybe" else "I"
label = lambda c: "Parked" if c == "Maybe" else c
def nxt(j):
    if j["call"] == "Pass": return '<span style="color:var(--faint);font-weight:500">Passed</span>'
    if not j.get("next"): return '<span style="color:var(--flag-fg)">No next step set</span>'
    nd = d(j.get("nextDate")); when = ""
    if j["call"] == "Maybe" and nd: when = f'<span class="when">{"Revisit now" if nd <= today else "Revisit " + fmt(nd)}</span>'
    return f'<span class="clamp">{E(j["next"])}</span>{when}'
openj = [j for j in jobs if j["call"] != "Pass"]
rows = "".join(f'''<div class="row"><span class="rank">{i+1}</span><span style="display:flex;flex-direction:column;gap:2px;min-width:0"><span class="co">{E(j["co"])}</span><span class="role">{E(j["role"])}</span><span class="chips"><span class="pill {pill(j["call"])}">{label(j["call"])}</span><span class="pill {"warm" if j["path"]=="Warm" else "cold"}">{j["path"]}{" · " + E(j["contact"]) if j.get("contact") else ""}</span></span></span><span class="score"><span class="n">{j.get("fit","–")}</span><span class="bar"><i style="width:{j.get("fit") or 0}%"></i></span></span><span class="gap"><span class="clamp">{E(j.get("gap"))}</span></span><span class="next">{nxt(j)}</span></div>''' for i, j in enumerate(openj))
detail = ""
if openj:
    s0 = openj[0]; idx = LADDER.index(s0["stage"]) if s0.get("stage") in LADDER else -1
    detail = (f'<div class="eyebrow">Selected</div><h2>{E(s0["co"])}</h2><div class="sub">{E(s0["role"])}</div>'
      f'<div class="scorebig"><span class="n">{s0.get("fit","–")}</span><span class="pill {pill(s0["call"])}">{label(s0["call"])}</span></div>'
      + (f'<div class="nextbox"><div class="k">Next step</div><div>{E(s0["next"])}</div></div>' if s0.get("next") else "")
      + f'<div class="k">Biggest gap</div><div class="sub">{E(s0.get("gap") or "None noted")}</div>'
      + '<ol class="ladder">' + "".join(f'<li class="{"now" if i == idx else "done" if i < idx else ""}">{r}</li>' for i, r in enumerate(LADDER)) + "</ol>"
      + '<div class="sec"><div class="k">What we know</div>' + "".join(
          f'<div class="ev"><span class="pill {e[0]}">{TAGNAME[e[0]]}</span><span>{E(e[1])}</span></div>' for e in s0.get("ev", [])) + "</div>")
out = (tpl.replace("__DATA__", blob, 1).replace("__STAMP__", E(f"FitFactorOS · {data['sheet']} · read {fmt(today)}"), 1)
       .replace("__STRIP__", strip, 1).replace("__LIST__", rows, 1).replace("__DETAIL__", detail, 1))
pathlib.Path(sys.argv[2]).write_text(out)
print(f"OK: {len(data['jobs'])} jobs, {len(data['activities'])} activities -> {sys.argv[2]}")
