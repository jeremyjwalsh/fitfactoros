# Activity rows, and what the weekly log reads

Rows run across columns, so fields are separated by a **tab character**. Output each row as a single line inside a code block. The user pastes it into the first empty cell in column A of the **Activity** tab.

## Activity tab: 15 columns, A through O

| Col | Field | What to write |
|---|---|---|
| A | Date | The day it happened, YYYY-MM-DD |
| B | Week ending | The last day of the state's benefit week that contains the Date (Massachusetts: that week's Saturday). Blank if there's no state file or the user isn't collecting. |
| C | Job ID | The Jobs tab ID if this is about a specific job. Otherwise blank. |
| D | Activity type | One of: Applied, Reviewed job posting, Outreach message, Networking contact, Informational interview, Interview, Job fair, Workshop or training, Other |
| E | Company / organization | The employer, or the group that ran the event |
| F | Contact person | Name, if there was one |
| G | Contact method | One of: Email, Phone, In person, Video, Online application, Other |
| H | Position | The job title, if there is one |
| I | Result | What happened, in one short plain sentence: "Submitted application", "Recruiter replied, call set for 10/2", "No reply yet" |
| J | Counts for unemployment | `Yes` or `No` only as the state file says for this activity type. Otherwise blank. |
| K | Email link | Blank. The user or a later agent fills it. |
| L | Notes | Anything else, short |
| M | Pay rate | As posted, or `Not posted`. Never an estimate. |
| N | Employer address | As the user gives it. Blank if unknown. Don't use the job's location as the address. |
| O | Contact info | The email, website, or phone used for this activity. For an online application, the job link. |

## Which Jobs columns the weekly log reads

Match by Job ID (Jobs column A). The weekly log uses: B Date added, C Company, D Role, E Job link, J Pay range, M Screen result, S Status. A Jobs row with a Date added inside the week and no Activity row for that Job ID in that week becomes a **Reviewed job posting** entry:

- Date = Date added; Activity type = Reviewed job posting; Company = Company; Position = Role; Pay rate = Pay range; Employer address = blank (a job's location isn't the employer's address); Contact method = Other; Contact info = Job link (or blank if it says `Pasted text`); Result = "Reviewed posting; decided to [pursue / hold as a maybe / pass]" from the Screen result.

## How to build a row

Use `scripts/make_row.py`. Its keys, A to O: date, week_ending, job_id, type, company, contact_person, method, position, result, counts, email_link, notes, pay_rate, employer_address, contact_info. Leave blank fields out.

```
python3 scripts/make_row.py date=2026-09-24 week_ending=2026-09-26 type=Applied company="Northwind" method="Online application" position="Enablement Manager" result="Submitted application" counts=Yes contact_info="https://example.com/job"
```

**Only if you can't run code:** blank cells make it easy to add one tab too many, which shifts everything after it into the wrong column. So:

1. Write the row as a list of **exactly 15 values**, A through O, in order. Use an empty value for each blank cell.
2. If you can run code, join the list with tabs in code (for example Python `"\t".join(values)`) and check `len(values) == 15`. If you can't, count: **15 fields means exactly 14 tabs.**
3. Output the joined line in a code block.

**Worked example.** An online application with no Job ID, contact person, email link, notes, pay rate, or address:

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-24 | 2026-09-26 | | Applied | Northwind | | Online application | Enablement Manager | Submitted application | Yes | | | | | https://example.com/job |

Between `Yes` (J) and the link (O) there are four blank cells (K, L, M, N), so exactly **five** tabs.

## Row rules
- Blank cells are two tabs in a row. Never write "blank" or "skipped" in a cell.
- No field starts with `=`, `+`, `-`, `@`, or `"`. Start with a word or a number instead.
- No line breaks or tabs inside a field. Separate list items with "; ".
- Dropdown values must match the lists above exactly, including capitals.
- Output only rows that are new. Never re-send rows already in the Sheet.

## Pasted rows from the user
When the user copies cells from Google Sheets into the chat, they arrive tab-separated. If the header row is included, use it. If not, assume the column order above (Activity) and in the Jobs tab (A Job ID through U Notes). If a pasted row doesn't fit either layout, ask which tab it came from rather than guess.

Older Sheets may have only columns A through L on the Activity tab. Treat missing M, N, and O as blank, and tell the user once: "Your Activity tab is missing three new columns. Add these headers in M1, N1, and O1: Pay rate, Employer address, Contact info."
