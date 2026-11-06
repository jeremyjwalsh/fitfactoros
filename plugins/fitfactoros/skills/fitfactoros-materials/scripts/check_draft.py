#!/usr/bin/env python3
"""Check a tailored resume draft against its sources.

Usage: python3 check_draft.py resume.txt confirmed.txt draft.txt

Lists every number and every capitalized name or tool in the draft that
doesn't appear in the resume or in what the user confirmed in the chat.
Prints OK when there's nothing to check. This catches invented numbers,
employers, and tools. It can't catch a reworded claim, or a real number
moved onto a different claim (60 days becoming 60 accounts), so a person
still reads every line.
"""
import re, sys, pathlib

if len(sys.argv) != 4:
    sys.exit("Usage: python3 check_draft.py resume.txt confirmed.txt draft.txt")

resume, confirmed, draft = (pathlib.Path(p).read_text(errors="ignore") for p in sys.argv[1:])
source = resume + "\n" + confirmed

def norm_num(s):
    return s.replace(",", "").rstrip(".").lower()

NUM = re.compile(r"[$€£]?\d[\d,]*(?:\.\d+)?\s?(?:%|k|m|b|x|\+)?", re.I)
src_nums = {norm_num(m.group().replace(" ", "")) for m in NUM.finditer(source)}
src_digits = {re.sub(r"\D", "", n) for n in src_nums}

# Words that start a sentence or bullet are often capitalized for no reason,
# so only flag capitalized words that never appear in the sources at all,
# in any case, and skip a short list of common resume words.
COMMON = set("""a an and the of for to in on with by at as from or our my i
led built managed created drove grew owned ran launched designed developed delivered
improved reduced increased cut partnered worked helped supported trained coached hired
mentored wrote presented sold closed renewed expanded scaled set started rolled
summary experience education skills profile highlights certifications awards projects
present current today senior junior lead principal manager director head vice president
jan feb mar apr may jun jul aug sep sept oct nov dec january february march april june
july august september october november december
""".split())
src_words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9+#.&'-]*", source)}

problems = []
for m in NUM.finditer(draft):
    raw = m.group().replace(" ", "")
    n = norm_num(raw)
    if not re.search(r"\d", n):
        continue
    if n in src_nums or re.sub(r"\D", "", n) in src_digits:
        continue
    problems.append(f"Number not in your resume or the chat: {raw}")

seen = set()
for w in re.findall(r"\b[A-Z][A-Za-z0-9+#.&'-]*", draft):
    key = w.lower().rstrip(".,'")
    if key in COMMON or key in src_words or key in seen or len(key) < 2:
        continue
    seen.add(key)
    problems.append(f"Name or term not in your resume or the chat: {w.rstrip('.,')}")

if problems:
    print("CHECK THESE before sending. Remove each one, or ask the user to confirm it:")
    for p in problems:
        print(" - " + p)
    sys.exit(1)
print("OK: every number and name in the draft appears in the resume or the confirmed notes.")
