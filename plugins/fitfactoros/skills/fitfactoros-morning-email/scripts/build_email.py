#!/usr/bin/env python3
"""FitFactorOS morning email helper.

Three commands:

  seed  "<picks from Profile B20>" YYYY-MM-DD
        Prints today's seed (Quote, Music or Humor). Rotates by date.

  pick  quotes|songs "<theme>,<theme>" YYYY-MM-DD
        Prints one entry from references/quotes.md or references/songs.md
        whose themes best match, rotating by date among the best matches.

  build data.json OUTDIR
        Checks data.json against the rules and writes OUTDIR/email.html,
        OUTDIR/email.txt and OUTDIR/subject.txt. Prints STOP and exits 1
        if something breaks a rule.

Standard library only.
"""
import datetime
import html
import json
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.join(HERE, "..", "references")
SEEDS = ["Quote", "Music", "Humor"]
STATES = ["Momentum", "Steady", "Quiet stretch", "Overwhelmed"]
MATCHES = ["Strong", "Possible"]



def screened_line(t):
    """Jobs screened (Dashboard B7) shown on its own, never added to the counted number."""
    n = t.get("screened") or 0
    if n <= 0:
        return ""
    jobs = "1 job" if n == 1 else "%d jobs" % n
    if isinstance(t.get("weeklyMin"), int):
        return "Also %s screened this week. Your weekly log can add any that aren't in your Activity tab yet." % jobs
    return "Also %s screened this week." % jobs

def stop(msg):
    print("STOP: " + msg)
    sys.exit(1)


def day_number(date_str):
    try:
        d = datetime.date.fromisoformat(date_str)
    except ValueError:
        stop("date must be YYYY-MM-DD, got %r" % date_str)
    return d.toordinal()


# ---------- seed ----------
def cmd_seed(picks, date_str):
    raw = [p.strip().lower() for p in re.split(r"[;,]", picks or "") if p.strip()]
    chosen = []
    if not raw or "skipped" in raw or any("surprise" in p for p in raw):
        chosen = list(SEEDS)
    else:
        for s in SEEDS:
            if s.lower() in raw:
                chosen.append(s)
    if not chosen:
        chosen = list(SEEDS)
    print(chosen[day_number(date_str) % len(chosen)])


# ---------- pick ----------
def read_list(kind):
    path = os.path.join(REFS, "quotes.md" if kind == "quotes" else "songs.md")
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("|") or line.startswith("|---") or line.startswith("| ID"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                continue
            themes = {t.strip().lower() for t in cells[-1].split(",") if t.strip()}
            rows.append((cells, themes))
    if not rows:
        stop("no entries found in " + path)
    return rows


def cmd_pick(kind, themes, date_str):
    if kind not in ("quotes", "songs"):
        stop("pick needs 'quotes' or 'songs'")
    want = {t.strip().lower() for t in themes.split(",") if t.strip()}
    rows = read_list(kind)
    scored = sorted(((len(t & want), i, c) for i, (c, t) in enumerate(rows)), key=lambda x: (-x[0], x[1]))
    best = scored[0][0]
    # Best matches first; widen to weaker matches until there are at least 3
    # choices, so the pick changes from day to day.
    pool = []
    for floor in range(best, 0 if best else -1, -1):
        pool = [c for s, _, c in scored if s >= floor]
        if len(pool) >= 3:
            break
    if not pool:
        pool = [c for _, _, c in scored]
    cells = pool[day_number(date_str) % len(pool)]
    if kind == "quotes":
        print(json.dumps({"id": cells[0], "text": cells[1], "source": cells[2]}))
    else:
        print(json.dumps({"id": cells[0], "title": cells[1], "artist": cells[2]}))


# ---------- build ----------
def esc(s):
    return html.escape(str(s or ""), quote=True)


def check(d):
    for k in ("date", "state", "spark", "move", "tiles", "dashboardUrl", "closing"):
        if k not in d:
            stop("data.json is missing '%s'" % k)
    if d["state"] not in STATES:
        stop("state must be one of %s" % STATES)
    sp = d["spark"]
    if sp.get("seed") not in SEEDS:
        stop("spark.seed must be Quote, Music or Humor")
    if sp["seed"] == "Humor" and not sp.get("headline"):
        stop("Humor seed needs spark.headline (the setup line)")
    if sp.get("headline") and len(sp["headline"]) > 60:
        stop("spark.headline must be 60 characters or fewer")
    if not sp.get("body") or len(sp["body"]) > 220:
        stop("spark.body is required and must be 220 characters or fewer")
    if sp["seed"] == "Quote" and not (sp.get("quote") or {}).get("source"):
        stop("Quote seed needs spark.quote with text and source from references/quotes.md")
    if sp["seed"] == "Music" and not (sp.get("song") or {}).get("title"):
        stop("Music seed needs spark.song from references/songs.md")
    if not d["move"].get("title"):
        stop("move.title is required")
    t = d["tiles"]
    for k in ("inFlight", "thisWeek", "needsAttention"):
        if not isinstance(t.get(k), int):
            stop("tiles.%s must be a whole number" % k)
    if not isinstance(t.get("screened", 0), int):
        stop("tiles.screened must be a whole number (Dashboard B7)")
    att = d.get("attention") or []
    cap = 2 if d["state"] == "Overwhelmed" else 3
    if len(att) > cap:
        stop("attention has %d items; the limit in state %s is %d" % (len(att), d["state"], cap))
    cu = d.get("comingUp") or []
    if not isinstance(cu, list) or len(cu) > 2:
        stop("comingUp must be a list of at most 2 items")
    more = d.get("attentionMore", 0)
    if not isinstance(more, int) or more < 0:
        stop("attentionMore must be a whole number, 0 or more")
    if more and len(att) + more + (1 if d.get("moveIsDue") else 0) != t["needsAttention"]:
        stop("attention items + attentionMore + the one move (if it is Due) must add up to tiles.needsAttention")
    leads = d.get("leads") or []
    if leads and (d["state"] == "Overwhelmed" or t["needsAttention"] >= 3):
        stop("leads must be empty when Overwhelmed or when 3 or more items need attention")
    if len(leads) > 2:
        stop("at most 2 leads")
    for l in leads:
        if l.get("match") not in MATCHES:
            stop("each lead's match must be Strong or Possible")
    if not str(d["dashboardUrl"]).startswith("https://"):
        stop("dashboardUrl must start with https://")
    blob = json.dumps(d)
    if "{{" in blob or "TODO" in blob or "EXAMPLE" in blob:
        stop("data.json still has a placeholder or an example row")


LABEL_TOP = 'padding:18px 28px 10px 28px;font-size:12px;font-weight:bold;letter-spacing:1px;color:#2b5d4f;text-transform:uppercase;'
SPARK_LABEL = {"Quote": "A thought for today", "Music": "Today&rsquo;s soundtrack", "Humor": "A little lightness"}
SPARK_LABEL_TXT = {"Quote": "A THOUGHT FOR TODAY", "Music": "TODAY'S SOUNDTRACK", "Humor": "A LITTLE LIGHTNESS"}
def goal_met(t):
    return isinstance(t.get("weeklyMin"), int) and t["thisWeek"] >= t["weeklyMin"]


def counted_label(t, html_out=False):
    """Tile label. Once the weekly minimum is met, the tile says so instead."""
    if not isinstance(t.get("weeklyMin"), int):
        return "Activities logged"
    if goal_met(t):
        return '<span style="color:#2b5d4f;font-weight:bold;">Goal met</span>' if html_out else "Activities counted (goal met)"
    return "Activities counted"


def att_label(d):
    """It's a shortlist whenever the tile counts more than the list shows."""
    return "Top items needing attention" if (d.get("attentionMore") or 0) > 0 else "What deserves attention"


def more_line(d):
    n = d.get("attentionMore") or 0
    if n <= 0:
        return ""
    return "Plus %d more in your Sheet." % n


def button_label(url):
    return "Open your dashboard" if "claude.ai" in url else "Open your Sheet"


def dash_note(url):
    """Second way in: the rich dashboard lives in Claude, so point there in words."""
    if "claude.ai" in url:
        return 'This opens your last snapshot. To refresh it, say "show my dashboard" in your FitFactorOS Project in Claude.'
    return 'Want the full picture? Open your FitFactorOS Project in Claude and say "show my dashboard".'


LABEL = 'padding:20px 28px 8px 28px;font-size:12px;font-weight:bold;letter-spacing:1px;color:#2b5d4f;text-transform:uppercase;border-top:1px solid #eee9e0;'


def nice_date(date_str):
    d = datetime.date.fromisoformat(date_str)
    return d.strftime("%A, %B ") + str(d.day)


def build_html(d):
    sp, t = d["spark"], d["tiles"]
    p = []
    p.append('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#f4f2ee" style="font-family:Arial,Helvetica,sans-serif;"><tr><td align="center" style="padding:24px 0;">')
    p.append('<table role="presentation" width="600" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="max-width:600px;width:100%;border:1px solid #e2ddd4;">')
    p.append('<tr><td style="padding:26px 28px 4px 28px;font-size:12px;letter-spacing:1px;color:#8a8478;text-transform:uppercase;">FitFactorOS &middot; %s</td></tr>' % esc(nice_date(d["date"])))
    serif = "font-family:Georgia,'Times New Roman',serif;"
    p.append('<tr><td style="%s">%s</td></tr>' % (LABEL_TOP, SPARK_LABEL[sp["seed"]]))
    if sp["seed"] == "Quote":
        q = sp["quote"]
        author = q["source"].split(",")[0].strip()
        p.append('<tr><td style="padding:2px 28px 4px 28px;%sfont-size:22px;line-height:1.35;color:#1f1d1a;">&ldquo;%s&rdquo;</td></tr>' % (serif, esc(q["text"])))
        p.append('<tr><td style="padding:0 28px 2px 28px;font-size:14px;color:#3a3732;">&mdash; %s</td></tr>' % esc(author))
        rest = q["source"][len(author):].lstrip(", ").strip()
        if rest:
            p.append('<tr><td style="padding:0 28px 14px 28px;font-size:12px;color:#8a8478;">%s</td></tr>' % esc(rest))
    elif sp["seed"] == "Music":
        s_ = sp["song"]
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus("%s %s" % (s_["title"], s_["artist"]))
        p.append('<tr><td style="padding:2px 28px 2px 28px;%sfont-size:22px;line-height:1.35;color:#1f1d1a;">&#9835; <a href="%s" style="color:#1f1d1a;text-decoration:none;">%s</a></td></tr>' % (serif, esc(url), esc(s_["title"])))
        p.append('<tr><td style="padding:0 28px 2px 28px;font-size:14px;color:#3a3732;">%s</td></tr>' % esc(s_["artist"]))
        if s_.get("why"):
            p.append('<tr><td style="padding:0 28px 14px 28px;font-size:12px;color:#8a8478;">%s</td></tr>' % esc(s_["why"]))
    else:
        p.append('<tr><td style="padding:2px 28px 10px 28px;%sfont-size:22px;line-height:1.35;color:#1f1d1a;">%s</td></tr>' % (serif, esc(sp["headline"])))
    lead = '<b style="color:#2b5d4f;">What it means today:</b> ' if sp["seed"] != "Humor" else ""
    p.append('<tr><td style="padding:6px 28px 24px 28px;%sfont-size:16px;line-height:1.55;color:#3a3732;">%s%s</td></tr>' % (serif, lead, esc(sp["body"])))
    # operational half
    p.append('<tr><td style="padding:0 28px 22px 28px;"><div style="border-top:1px solid #eee9e0;font-size:0;line-height:0;">&nbsp;</div></td></tr>')
    mv = d["move"]
    p.append('<tr><td style="padding:0 28px 24px 28px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td bgcolor="#e8f1ed" style="border-left:4px solid #2b5d4f;padding:16px 18px;">')
    p.append('<div style="font-size:12px;font-weight:bold;letter-spacing:1px;color:#2b5d4f;text-transform:uppercase;padding-bottom:6px;">Your one move</div>')
    p.append('<div style="font-size:17px;line-height:1.45;color:#1f1d1a;"><b>%s</b></div>' % esc(mv["title"]))
    if mv.get("why"):
        p.append('<div style="font-size:14px;line-height:1.5;color:#3a3732;padding-top:4px;">%s</div>' % esc(mv["why"]))
    p.append('</td></tr></table></td></tr>')
    # tiles
    wk = str(t["thisWeek"])
    if isinstance(t.get("weeklyMin"), int):
        wk += ' <span style="font-size:15px;color:#8a8478;font-weight:normal;">of %d</span>' % t["weeklyMin"]
    na_color = "#a06a00" if t["needsAttention"] else "#1f1d1a"
    tile = '<td width="33%%" align="center" bgcolor="#f7f5f1" style="padding:14px 4px;border:1px solid #eee9e0;"><div style="font-size:26px;font-weight:bold;color:%s;">%s</div><div style="font-size:12px;color:#8a8478;">%s</div></td>'
    p.append('<tr><td style="%s">How am I doing &middot; this week</td></tr>' % LABEL)
    p.append('<tr><td style="padding:0 28px 8px 28px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>')
    p.append(tile % ("#1f1d1a", t["inFlight"], "In flight"))
    p.append(tile % ("#1f1d1a", wk, counted_label(t, html_out=True)))
    p.append(tile % (na_color, t["needsAttention"], "Needs attention"))
    p.append('</tr></table></td></tr>')
    sl = screened_line(t)
    if sl:
        p.append('<tr><td style="padding:4px 28px 0 28px;font-size:13px;color:#6b665d;">%s</td></tr>' % esc(sl))
    if d.get("lastStep"):
        p.append('<tr><td style="padding:4px 28px 0 28px;font-size:13px;color:#6b665d;">Last real step: %s</td></tr>' % esc(d["lastStep"]))
    for c in (d.get("comingUp") or [])[:2]:
        p.append('<tr><td style="padding:4px 28px 0 28px;font-size:13px;color:#1f1d1a;"><b style="color:#2b5d4f;">Coming up:</b> %s</td></tr>' % esc(c))
    p.append('<tr><td style="padding:0 0 20px 0;font-size:0;line-height:0;">&nbsp;</td></tr>')
    # attention
    p.append('<tr><td style="%s">%s</td></tr>' % (LABEL, att_label(d)))
    att = d.get("attention") or []
    p.append('<tr><td style="padding:0 28px 18px 28px;font-size:15px;line-height:1.5;color:#1f1d1a;">')
    if att:
        p.append('<table role="presentation" width="100%" cellpadding="0" cellspacing="0">')
        for i, a in enumerate(att):
            border = "" if i == 0 else "border-top:1px solid #f1ede6;"
            p.append('<tr><td style="padding:8px 0;%s"><b>%s</b><br><span style="font-size:13px;color:#8a8478;">%s</span></td></tr>' % (border, esc(a.get("title")), esc(a.get("detail"))))
        p.append('</table>')
        if more_line(d):
            p.append('<p style="margin:8px 0 0 0;font-size:13px;color:#8a8478;">%s</p>' % esc(more_line(d)))
    else:
        p.append('<p style="margin:4px 0;color:#6b665d;">%s</p>' % esc(d.get("attentionEmpty") or "Nothing waiting on you right now."))
    p.append('</td></tr>')
    # leads
    if d.get("leadsNote") is not None or d.get("leads"):
        p.append('<tr><td style="%s">Worth a look</td></tr>' % LABEL)
        p.append('<tr><td style="padding:0 28px 6px 28px;font-size:15px;line-height:1.5;color:#1f1d1a;">')
        leads = d.get("leads") or []
        if leads:
            p.append('<table role="presentation" width="100%" cellpadding="0" cellspacing="0">')
            for l in leads:
                col = "#2b5d4f" if l["match"] == "Strong" else "#a06a00"
                p.append('<tr><td style="padding:6px 0;"><b>%s</b><br><span style="font-size:13px;color:#8a8478;">%s &middot; %s</span></td><td align="right" style="padding:6px 0;vertical-align:top;"><span style="font-size:12px;font-weight:bold;color:%s;">%s</span></td></tr>' % (esc(l.get("role")), esc(l.get("co")), esc(l.get("loc")), col, esc(l["match"])))
            p.append('</table><p style="margin:6px 0 0 0;font-size:13px;color:#8a8478;">Quick matches only. Say &ldquo;fit factor this&rdquo; for the full check.</p>')
        else:
            p.append('<p style="margin:4px 0;color:#6b665d;">%s</p>' % esc(d.get("leadsNote") or "Nothing new worth your time today."))
        p.append('</td></tr>')
    # footer
    p.append('<tr><td style="padding:22px 28px 6px 28px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0"><tr><td align="center" bgcolor="#2b5d4f" style="border-radius:4px;padding:13px 20px;"><a href="%s" style="color:#ffffff;font-size:15px;font-weight:bold;text-decoration:none;">%s &rarr;</a></td></tr></table></td></tr>' % (esc(d["dashboardUrl"]), button_label(d["dashboardUrl"])))
    p.append('<tr><td align="center" style="padding:6px 28px 4px 28px;font-size:13px;line-height:1.5;color:#3a3732;">%s</td></tr>' % esc(dash_note(d["dashboardUrl"])))
    p.append('<tr><td align="center" style="padding:14px 28px 26px 28px;font-size:13px;color:#8a8478;font-style:italic;">%s</td></tr>' % esc(d["closing"]))
    p.append('</table></td></tr></table>')
    return "\n".join(p)


def build_text(d):
    sp, t = d["spark"], d["tiles"]
    out = [nice_date(d["date"]).upper(), "", SPARK_LABEL_TXT[sp["seed"]]]
    if sp["seed"] == "Music":
        s_ = sp["song"]
        out += ["%s - %s" % (s_["title"], s_["artist"]),
                "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus("%s %s" % (s_["title"], s_["artist"]))]
        if s_.get("why"):
            out.append(s_["why"])
    elif sp["seed"] == "Quote":
        out += ['"%s"' % sp["quote"]["text"], "- " + sp["quote"]["source"]]
    else:
        out.append(sp["headline"])
    out += [("What it means today: " if sp["seed"] != "Humor" else "") + sp["body"], "", "----", ""]
    out += ["YOUR ONE MOVE", d["move"]["title"]]
    if d["move"].get("why"):
        out.append(d["move"]["why"])
    wk = str(t["thisWeek"]) + (" of %d" % t["weeklyMin"] if isinstance(t.get("weeklyMin"), int) else "")
    out += ["", "HOW AM I DOING (this week)",
            "In flight: %d | %s: %s | Needs attention: %d" % (t["inFlight"], counted_label(t), wk, t["needsAttention"])]
    if screened_line(t):
        out.append(screened_line(t))
    if d.get("lastStep"):
        out.append("Last real step: " + d["lastStep"])
    for c in (d.get("comingUp") or [])[:2]:
        out.append("Coming up: " + c)
    out += ["", att_label(d).upper()]
    att = d.get("attention") or []
    out += ["%s - %s" % (a.get("title"), a.get("detail")) for a in att] or [d.get("attentionEmpty") or "Nothing waiting on you right now."]
    if att and more_line(d):
        out.append(more_line(d))
    if d.get("leadsNote") is not None or d.get("leads"):
        out += ["", "WORTH A LOOK"]
        leads = d.get("leads") or []
        if leads:
            out += ["%s - %s - %s - %s" % (l["role"], l["co"], l["loc"], l["match"]) for l in leads]
            out.append('Quick matches only. Say "fit factor this" for the full check.')
        else:
            out.append(d.get("leadsNote") or "Nothing new worth your time today.")
    out += ["", button_label(d["dashboardUrl"]) + ": " + d["dashboardUrl"], dash_note(d["dashboardUrl"]), "", d["closing"]]
    return "\n".join(out)


def cmd_build(path, outdir):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    check(d)
    os.makedirs(outdir, exist_ok=True)
    day = datetime.date.fromisoformat(d["date"])
    move = d["move"]["title"]
    if ":" in move[:40]:
        move = move.split(":", 1)[0]
    elif len(move) > 50:
        move = move[:50].rsplit(" ", 1)[0] + "..."
    subject = "Your morning · %s %s · %s" % (day.strftime("%a %b"), day.day, move)
    for name, body in (("email.html", build_html(d)), ("email.txt", build_text(d)), ("subject.txt", subject)):
        with open(os.path.join(outdir, name), "w", encoding="utf-8") as f:
            f.write(body)
    print("OK: wrote email.html, email.txt, subject.txt to " + outdir)


def main(a):
    if len(a) == 3 and a[0] == "seed":
        cmd_seed(a[1], a[2])
    elif len(a) == 4 and a[0] == "pick":
        cmd_pick(a[1], a[2], a[3])
    elif len(a) == 3 and a[0] == "build":
        cmd_build(a[1], a[2])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
