---
name: fitfactoros-dashboard
description: Shows the user's FitFactorOS dashboard. Reads their FitFactorOS Google Sheet (read-only) and makes a private page with their top picks, each job's ladder, its tagged evidence, who to write to, parked Maybes, and this week's progress. Use when the user says "show my dashboard", "my dashboard", "refresh my dashboard", "where do I stand?", or "what should I work on next?" inside their FitFactorOS Project.
---

# FitFactorOS Dashboard

The user says "show my dashboard." You read their Sheet, fill the template, and publish a private page. You never change the Sheet.

Before starting, read `references/guardrails.md` and `references/data-map.md`. The guardrails override anything here.

## Rules for this agent

1. **Read only.** Use the Google Sheets connector's read tools (get values). Never write, append, clear, or format anything in the Sheet, even to fix a problem you spot. Point to the cell instead.
2. **Only what's in the Sheet.** Every job, score, tag, and date comes from a row. No research, no searches, no new evidence. If something is missing, the page shows it as missing.
3. **Keep the template.** Fill only the data block, with `scripts/fill.py`. Don't restyle or rewrite the page.
4. **One page per user.** If they have a dashboard page from before, update that page so the link stays the same.

## Step 1: Find the Sheet

- **Google Sheets connected:** find the Sheet named like "FitFactorOS" (ask which one if there are several), then read the Jobs, Evidence, and Activity tabs and Dashboard!B9.
- **Not connected:** say, in one line, that connecting Google Sheets lets you read their Sheet without them pasting anything, and offer the connector. If they'd rather paste, ask for the Jobs, Evidence, and Activity rows (copy each tab from row 2 down) and build from those.

## Step 2: Build the data

Follow `references/data-map.md` exactly. Save it as `data.json`, then run:

```
python3 scripts/fill.py data.json dashboard.html
```

If it says STOP, fix the data and run it again. Don't hand-edit the HTML.

## Step 3: Publish and say what it shows

Publish `dashboard.html` as a private page. Then, in at most four short lines:
- What changed since the last view, if you know (new jobs, a rung moved).
- Parked Maybes whose revisit date has come.
- Any **Fix in Sheet** flag, with the tab, row (Job ID), and column to fix.
- One next step: the top Pursue's next step.

Mention once per chat that each refresh uses a little of their Claude plan.
