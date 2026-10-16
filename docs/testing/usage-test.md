# Usage test: how much does each step use?

A simple way to measure how much Claude usage Intake, a quick fit, a deep dive, and the dashboard take, so the docs can say it plainly. Takes about an hour per run. Do three runs.

## What you can and can't see
- **Paid plans:** **Settings → Usage** shows how much of your current session you've used, as a percent, and when it resets. That's the meter we use.
- **Free plan:** there's no percent meter that we know of. You only find out when you hit the limit. So we measure on a paid account, then check the result on a Free account.
- Free limits are lower than paid ones, so the percents won't match Free exactly. What carries over is the **ratio**: if a deep dive uses 4 times what a quick fit does on Pro, it's roughly 4 times on Free too.

Check the menu names on your next run and fix this page if they've changed.

## Setup (once)
- A paid test account with FitFactorOS set up (Basic mode is fine; add the Google Sheets connection only for the dashboard row).
- **Start each run at the beginning of a fresh session:** wait until **Settings → Usage** shows the session has reset, or close to 0%.
- Use the **same job** every run: one real public posting. Save its text in a file before run 1 and paste that same text each time, so the posting can't change between runs. (A made-up company would make the research come up empty and use less than a real one.) Don't put the company or the posting in this repository.
- Use the **sample profile** (`samples/sample-profile.md`) for Intake answers, so every run is the same.
- Use nothing else on the account during a run.

## Steps (each in its own new chat in the Project)
Before and after each step, write down the **Current session** percent.

| # | Step | What to type |
|---|---|---|
| 1 | Intake | **start my intake**, answer from the sample profile |
| 2 | Quick fit | paste the saved job text, then the link and **fit factor this**; choose **Hold** |
| 3 | Deep dive | in the same chat, **go deep**, then **Yes, go deeper**; choose **Pursue** at the end |
| 4 | Dashboard | new chat, **show my dashboard** |

## Log

| Run | Date | Intake | Quick fit | Deep dive | Dashboard | Searches in deep dive | Notes |
|---|---|---|---|---|---|---|---|
| 1 | | % | % | % | % | | |
| 2 | | % | % | % | % | | |
| 3 | | % | % | % | % | | |
| **Middle value** | | % | % | % | % | | |

"Searches in deep dive": count the "Searched the web" and page-read lines Claude shows. The deep dive should stop at 12.

## Free plan check (once)
On a fresh Free account, at the start of a session, run steps 1 to 4 in order. Write down:
- Which step you were on when the limit message appeared (or "none").
- The reset time the message gave.
- Whether the deep dive finished with a verdict, or at least the "So far / Leaning" lines, before the limit.

## What to do with the numbers
Put the middle values in the Free vs paid table in `docs/setup.md`, in plain words (for example, "a deep dive uses about as much as four quick fits"). Add a CHANGELOG entry.
