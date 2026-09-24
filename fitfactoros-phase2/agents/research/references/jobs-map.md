# Jobs and Evidence rows

Rows run across columns, so fields are separated by a **tab character**. Output each row as a single line inside a code block. The user pastes it into the first empty cell in column A.

## Jobs tab: 21 columns, A through U

| Col | Field | What to write |
|---|---|---|
| A | Job ID | `J-YYMMDD-COMPANY`: today's date, then the company name in capitals, letters and digits only, up to 10 characters. Example: J-260924-NORTHWIND. If the same company is screened twice on one day, add -2. |
| B | Date added | Today, YYYY-MM-DD |
| C | Company | As the posting names it |
| D | Role | The job title as posted |
| E | Job link | The link, or `Pasted text` |
| F | Source | One of: Job board, Company site, Referral, Conversation, Recruiter, Job Finder, Other. Use what the user said; if unclear, Job board for job-board links, Company site for company careers pages, otherwise Other. |
| G | Suggested by | The person who sent it, if the user said. Otherwise blank. |
| H | Location | As posted |
| I | Work mode | One of: Remote, Hybrid, On-site. Blank if the posting doesn't say. |
| J | Pay range | Exactly as posted, or `Not posted`. Never an estimate in a quick screen. |
| K | Pay tag | `Verified` when pay is posted. Blank when not posted. |
| L | Fit score | Whole number 0–100, or `n/a` when a gate failed |
| M | Screen result | One of: Pursue, Maybe, Pass |
| N | Path | One of: Warm, Cold |
| O | Warm contact | The name exactly as in the Profile (B15). Blank if Cold. |
| P | Ladder stage | Blank after a quick screen. `Picked` if the user says they're going for it. `Researched` after deep research. Allowed: Picked, Researched, Found the right person, Reached out to contact, Sent a researched note, Applied, Heard back, Interviewing, Offer. |
| Q | Next step | One short action. Pursue: "Go deep, then reach out to [contact]", or "Go deep" if Cold. Maybe: the one question that settles it. Pass: blank. |
| R | Next step date | Today, YYYY-MM-DD, for Pursue or Maybe. Blank for Pass. |
| S | Status | `Active` for Pursue or Maybe. `Passed` for Pass. |
| T | Email link | Blank. A later agent fills this. |
| U | Notes | Starts with "Blocker: " and the blocker line. After deep research, add the deep results (see deep-research.md). |

## Evidence tab: 8 columns, A through H

One row per claim that drove the result. Quick screen: 3–6 rows. Deep research: up to 12.

| Col | Field | What to write |
|---|---|---|
| A | Job ID | Same as the Jobs row |
| B | Date checked | YYYY-MM-DD |
| C | Claim | One plain sentence |
| D | Tag | One of: Verified, Estimated, Inferred |
| E | Source link | The link read, or blank for the user's own Profile |
| F | Source type | One of: Job posting, Company site, Filing, News, Person, Your records, Other. Use "Your records" for Profile facts. Use "Person" for something a person told the user. |
| G | How we know | Verified: where it's stated. Estimated: the method. Inferred: the reasoning. |
| H | Checked by | `Agent` |

## Row rules
- Blank cells are two tabs in a row. Never write "blank" or "skipped" in a Jobs or Evidence cell.
- No field starts with `=`, `+`, `-`, `@`, or `"`. Start with a word or a number instead.
- No line breaks or tabs inside a field. Separate list items with "; ".
- Dropdown values must match the lists above exactly, including capitals.
- Output only the rows that are new or changed.

## If tabs don't survive the paste
If testing shows tabs are lost when the user copies a code block, switch the separator to ` | ` and add this final paste step: *"With the pasted cells still selected, click **Data → Split text to columns**, then choose **Custom** and type |."* Fields must then never contain "|".
