# Activity check: calendar and email

People forget to log, especially on hard weeks. Their calendar and email usually remember. The activity check reads both, read-only, finds what looks like job-search activity, and **asks** about it. Nothing becomes a row until the user confirms it.

## When it runs

| Situation | What to do |
|---|---|
| **Weekly log**, once the user has pasted their rows | Offer it once: "Want me to check your calendar and email for anything you haven't logged this week?" Run it only on a yes. |
| **check my week** / **what did I miss?** | Run it for the current benefit week (the state file's week; Sunday to Saturday if there's no state file). |
| **Log it**, when the user describes something that happened | If Google Calendar is connected, look up that day's events once to fill in details (see "Filling in details"). Don't sweep the whole week. |

If Google Calendar or Gmail isn't connected, say once which one is missing and that the user can connect it in Claude's connector settings, then carry on with whatever is connected. If neither is, skip the check and continue normally. Never stop the log because of it.

## What to read (one pass)

**Calendar:** one list of events from the start of the week through 14 days after its end (the extra days catch interviews already booked). Skip declined events, all-day events, and events the user created with no other attendees unless the title names a company in their Jobs tab.

**Gmail:** at most two searches over the week's dates. Read sender, subject, date, and snippet only. Open a message only if the snippet doesn't say which company or role it's about, and open no more than 5 in a run.

1. **Received from hiring systems and companies:**
   ```
   after:YYYY/MM/DD before:YYYY/MM/DD -in:sent (from:(greenhouse.io OR ashbyhq.com OR myworkday.com OR lever.co OR smartrecruiters.com OR icims.com OR jobvite.com OR calendly.com OR goodtime.io) OR subject:("application" OR "interview" OR "your candidacy" OR "next steps" OR "thank you for applying") OR <company names from the Jobs tab, each in quotes, joined by OR>)
   ```
2. **Sent by the user:**
   ```
   after:YYYY/MM/DD before:YYYY/MM/DD in:sent (resume OR referral OR role OR position OR application OR interview OR "job" OR <company names from the Jobs tab>)
   ```

`before:` is the day after the week ends. Job alert emails (LinkedIn, Indeed, Glassdoor, ZipRecruiter alerts) are not activities. Skip them.

## What counts as a possible activity

| Seen | Likely type (Inferred) |
|---|---|
| Calendar event with someone at a company in the Jobs tab, or titled interview, screen, chat, or "[Name] + [User]" | Interview, or Networking contact if it's someone the user knows |
| Calendar event from Calendly or GoodTime with a recruiter | Interview (screen) |
| "Application received" or "Thanks for applying" email | Applied |
| User sent an email with a resume, or asked for a referral or an intro | Outreach message or Networking contact |
| A recruiter wrote and the user replied | Outreach message |
| A job fair, workshop, or career event on the calendar | Job fair, or Workshop or training |

Ignore everything else silently: personal events, family, health, money, anything not about the job search. **Never list or mention a non-job item**, even to say it was skipped.

## Remove what's already logged

Drop any candidate that matches an Activity row you've read from the Sheet, or one already in the chat (pasted rows, or rows you gave earlier), with the same company, the same date (give or take one day), and the same kind of activity. If you're unsure whether it's a duplicate, ask instead of dropping it.

## How to ask

One message. Lead with the count, then a numbered list, at most 8 items, oldest first. Each item is one line: the date, where you saw it, what you saw (event title or email subject, copied as written), and one short question. Mark your guess about what it was as a guess.

> I found 3 things that may be job-search activity you haven't logged:
> 1. **Oct 13, calendar (Zoom):** "Priya + Sam - Sr. CSM" with northwind.com. Looks like an interview (my guess). How did it go?
> 2. **Oct 15, calendar (phone):** "Sam Lee and Dana Cho" via Calendly. What was the call about?
> 3. **Oct 14, email:** "Thanks for applying" from Workday. Did you apply to something? Which role?
>
> **Coming up:** Oct 22, 4–5 pm, Zoom: "Interview Details: Northwind…" Want me to set it as the Next step for Northwind?
>
> Answer by number (for example "1 yes went well, 2 recruiter call about comp, 3 skip"). Anything you skip stays out of your log.

If there are more than 8, show 8 and say how many more there are. If nothing turns up, say so in one line and continue.

**When an email and the calendar disagree** (a different time or date for the same meeting), the calendar invite is usually the newer word. Compare the invite's last-updated time with the email's date. If the invite is newer, say it in one calm line: "Your Oct 14 email said 2 pm; the invite, updated Oct 15, says 4 pm, so 4 pm is probably current." Only raise it as something to check when the email is newer than the invite. Don't repeat it once the user has answered.

## After they answer

- Build a row with `scripts/make_row.py` only for items the user confirmed. Use the user's words for Result. Never upgrade them.
- An item the user skips or says didn't happen is dropped. Don't ask again in this chat.
- Interviews also get an Interviews row, as in Step 2A.
- **Coming up** items: give the Jobs cells to change (Next step and Next step date), never a new Activity row. Nothing is logged before it happens.
- Then continue where you were: the weekly log, or the rows the user asked for.

## Filling in details

From a confirmed event or email, fill only what it shows:

| Field | From |
|---|---|
| Date | The event's date, or the email's date |
| Contact method | A Zoom, Meet, Teams, or Webex link → `Video`. A phone number as the location → `Phone`. A street address → `In person`. An email thread → `Email`. |
| Contact person | A name the event or email shows. If there's only an email address, ask for the name or leave it blank. |
| Contact info | The other person's email address from the event or email |
| Notes | A next step the event or email states, such as the next interview's date |

When you use anything from the calendar or email, say so in one line ("From your calendar: Zoom, Oct 13, 5:30 pm"), so the user can check it.

## Never

- Log anything the user hasn't confirmed.
- Change, label, move, mark read, reply to, or delete any email or event.
- Copy an email's body into a row. Results are short and in the user's words.
- Read further back than the week being logged (plus the 14-day look-ahead on the calendar).
- Save what you read anywhere outside the rows the user pastes.
