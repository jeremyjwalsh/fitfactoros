# Sheet schema

FitFactorOS runs on one Google Sheet with five tabs. Every row about a specific opportunity carries the same **Job ID**, which is how the tabs join.

Import `sheet/fitfactoros-template.xlsx` into Google Sheets to get all five tabs with headers, dropdowns, and notes. Hover over any header to see what goes in that column.

## How data gets into the sheet

Agents don't edit your sheet. They give you text to paste:

- **Intake** gives one block of 17 answers. Click **Profile → B3** and paste.
- **Later agents** give only the new rows. Click the first empty row of the right tab and paste.

Agents never regenerate the whole file. This keeps usage low, and it means you always see exactly what's going in.

## Job ID

Format: `J-YYMMDD-COMPANY`, using the date the job was added and a short company name in capitals. Example: `J-260924-FABRIKAM`. For a second role at the same company on the same day, add `-2`.

The agent creates the ID when a job is first added, and every tab uses that same ID for that job.

## Email links

Emails are linked with a formula that opens the right Gmail account, even when you're signed into more than one:

```
=HYPERLINK("https://mail.google.com/mail/?authuser="&Profile!$B$2&"#all/THREAD_ID","Open email")
```

`Profile!$B$2` is the Gmail address you enter during setup, so you type it once. `THREAD_ID` is the ID of the Gmail thread. Agents that read your Gmail fill it in for you.

## Profile

One answer per row. Column A is the field, column B is your answer. Column C shows a fictional example, and column D shows which Intake question fills that row.

| Row | Field | Filled by |
|---|---|---|
| 2 | Gmail address (for inbox links) | You, during setup |
| 3 | Your name | Intake (resume) |
| 4 | Resume file | Intake (resume) |
| 5 | Most recent role | Intake (resume) |
| 6 | Years of experience | Intake (resume) |
| 7 | Top skills | Intake (resume) |
| 8 | Target roles | Intake Q2 |
| 9 | Where you can work | Intake Q3 |
| 10 | Pay floor | Intake Q4 |
| 11 | Deal-breakers | Intake Q5 |
| 12 | Companies to avoid | Intake Q5 |
| 13 | Work that makes you lose track of time | Intake Q6 |
| 14 | Dream companies | Intake Q7 |
| 15 | People you know (and where) | Intake Q7 |
| 16 | State | Intake Q8 |
| 17 | Collecting unemployment? | Intake Q8 (powers the Activity Log only) |
| 18 | Wins with numbers | Intake Q9 (optional) |
| 19 | Profile last updated | Intake |

## Jobs

One row per opportunity.

| Column | What goes in it | Choices |
|---|---|---|
| Job ID | See above | |
| Date added | YYYY-MM-DD | |
| Company | | |
| Role | | |
| Job link | Posting URL | |
| Source | Where you found it | Job board, Company site, Referral, Conversation, Recruiter, Job Finder, Other |
| Suggested by | Who pointed you to it. Often your warm path. | |
| Location | | |
| Work mode | | Remote, Hybrid, On-site |
| Pay range | As posted or estimated | |
| Pay tag | | Verified, Estimated, Inferred |
| Fit score | 0–100, from Research | |
| Screen result | | Pursue, Maybe, Pass |
| Path | | Warm, Cold |
| Warm contact | The person you'll reach out to | |
| Ladder stage | Last real step completed | Picked, Researched, Found the right person, Reached out to contact, Sent a researched note, Applied, Heard back, Interviewing, Offer |
| Next step | | |
| Next step date | YYYY-MM-DD | |
| Status | | Active, Closed – offer, Closed – no, Withdrawn, Passed |
| Email link | HYPERLINK formula | |
| Notes | | |

**Jobs you hear about in conversation.** Set Source to **Conversation** and put the person's name in **Suggested by**. Research will treat them as a likely warm path.

## Evidence

One claim per row, so every fact can be checked on its own.

| Column | What goes in it |
|---|---|
| Job ID | Matches Jobs |
| Date checked | YYYY-MM-DD |
| Claim | One fact |
| Tag | Verified, Estimated, or Inferred |
| Source link | Required for Verified |
| Source type | Job posting, Company site, Filing, News, Person, Your records, Other |
| How we know | Verified: where it was confirmed. Estimated: the method. Inferred: the reasoning. |
| Checked by | Agent or You |

## Interviews

One row per conversation: Job ID, Date, Round, Interviewer, Interviewer title, Format (Phone, Video, On-site), Questions asked, What I learned, Thank-you sent (Yes/No), Email link, Notes.

## Activity

One row per job-search action: Date, Week ending, Job ID (optional), Activity type, Company / organization, Contact person, Contact method, Position, Result, Counts for unemployment (Yes/No), Email link, Notes.

**Activity types:** Applied, Outreach message, Networking contact, Informational interview, Interview, Job fair, Workshop or training, Other.

**Week ending** depends on how your state defines the benefit week. The Activity Log agent (Phase 5) fills it in using your state's rules file. Whether an activity counts toward unemployment requirements is set by your state; FitFactorOS doesn't give legal advice.
