---
name: fitfactoros-morning-email
description: Runs the FitFactorOS morning email, an opt-in weekday email saved as a Gmail draft to the user (never sent) that answers how am I doing, what deserves my attention, and the one thing to do today. Also sets it up as a scheduled task. Use when the user says "set up my morning email", "morning email", "run my morning email", "change my morning email", or "stop my morning email", or when a scheduled FitFactorOS morning email run starts.
---

# FitFactorOS Morning Email

A one-minute email that shows up in the user's Gmail **Drafts** on weekday mornings. Every email answers three questions: How am I doing? What deserves my attention? What's the one thing I can do today? With a little inspiration along the way.

Before starting, read `references/guardrails.md` and `references/email-rules.md`. The guardrails override anything here.

## Rules for this agent

1. **Never send.** Save exactly one Gmail draft, addressed to the user's own Gmail address (Profile B2), and stop. Never use a send, reply, or forward tool. Never draft to anyone else. Never delete or change any other draft or email.
2. **Read only, everywhere else.** The Sheet is read-only. Gmail is read-only apart from the one draft: no labels, no moving, no marking read.
3. **Only what's in the Sheet.** Every company, step, date, and count comes from a row. If something is missing, the email says so plainly. Never invent a contact, a task, or progress.
4. **Light by design.** One Sheet read, one Gmail search, one draft. No web searches.
5. **Keep the layout.** Build the email only with `scripts/build_email.py`. Don't write the HTML by hand. Gmail drops ordinary background colors, and the script uses the kind that survives.

## Mode A: Set up (first time, or "change my morning email")

Check what's connected first. The email needs **Gmail** and **Google Sheets**. If either is missing, say which in one line, offer to connect it, and stop until it is.

Find the Sheet named like "FitFactorOS" (ask which one if there are several), and read `Profile!A2:B23`. If B2 (Gmail address) is blank or `skipped`, ask for it once; the draft can't be addressed without it.

Then ask, in one turn, all skippable:

- **Q1. What would you like at the top each morning?** Multi-select: "A quote," "A song," "Something funny," "Surprise me." (Skipped counts as Surprise me.)
- **Q2. What time should it be ready?** Single select: "6:30 am," "7:00 am," "8:00 am." Default 7:00 am.
- **Q3.** *(Typed, optional)* Two things, both optional:
  1. Your star sign, just for fun. Say it like this, word for word: *"It quietly helps pick quotes and songs that suit you. The email never mentions it."* Ask only for the sign, never a birthday.
  2. Your dashboard link, if you've made one. Without it, the button opens your Sheet's Dashboard tab.

Record Q1 as "Quote; Music; Humor" style (Surprise me as "Surprise me"). Record the sign as one of the 12 sign names, or `skipped`. Then give the paste steps, word for word in this shape:

**Next: add these to your Sheet**
1. Open the **Profile** tab and click cell **B20** (the **Morning email sparks** row).
2. Paste the block below. It fills **B20 through B23**.

Then a code block of exactly 4 lines: sparks, sign or `skipped`, ready-by time (like `7:00 am`), dashboard link or `skipped`. No line may start with `=`, `+`, `-`, `@`, or `"`.

*Older Sheets:* if rows 20 to 23 of the Profile tab have no labels, tell the user to type **Morning email sparks**, **Sign (optional)**, **Morning email ready by**, and **Dashboard link** into A20 through A23 first, and to move any notes in those rows further down.

### Schedule it

Find the session's scheduling tool (search the tool list for "trigger" or "schedule" if none is loaded). Call it a **scheduled task** when talking to the user.

- **A scheduling tool exists:** first list existing scheduled tasks and don't create a second "FitFactorOS morning email." Create a recurring task:
  - Name: `FitFactorOS morning email`
  - Schedule: weekdays at the chosen time, in the user's time zone. If you don't know their time zone, ask.
  - Notifications: push on, so they know the draft is ready.
  - Prompt (standalone, since each run starts fresh): *Run the FitFactorOS morning email (fitfactoros-morning-email skill), Mode B, for the Sheet at [Sheet link]. Save one Gmail draft to [Gmail address]. Never send anything.*
  - Then tell the user in one line which approval setting the task got. If runs will ask for approval, mention they can switch it to automatic approval in the task's settings, if their organization allows it.
- **No scheduling tool (for example, the Free plan):** say so in one line, and tell them to say **morning email** in their FitFactorOS Project any morning to get the same draft.

Then run Mode B once now, so they see their first email today.

Close with two lines: the draft lands in **Drafts**, not the inbox; and old drafts aren't deleted for them, so they can delete each one after reading.

### Stop it

"Stop my morning email": find the scheduled task named `FitFactorOS morning email` and, after the user confirms, turn it off. If you can't reach it, tell them to turn it off in their scheduled tasks list.

## Mode B: Make today's email

Used by the scheduled task, or when the user says "morning email."

1. **Read** the Sheet ranges in `references/email-rules.md` (read the Sheet link from the task prompt, or find the Sheet as in Mode A).
2. **Work out** the counts, the search state, the one move, and the attention list, exactly as the rules file says.
3. **New leads:** run the one Gmail search in the rules file, unless the state skips the section.
4. **Spark:** get the seed, pick themes, and pick the quote or song with the script, then write the headline and body.
5. **Build:** save `data.json`, then run:
   ```
   python3 scripts/build_email.py build data.json out
   ```
   If it prints STOP, fix `data.json` and run it again.
6. **Save the draft** with the Gmail draft tool: `to` = Profile B2 only, `subject` = `out/subject.txt`, `htmlBody` = `out/email.html`, `body` = `out/email.txt`.
7. **Finish** with one line: "Your morning email is in Drafts." In a scheduled run, that line is all.

If Gmail or Sheets can't be reached in a scheduled run, don't guess. Finish with one line saying which one failed, so the notification tells the user.

## Checks before saving the draft

- The draft is addressed only to Profile B2.
- The one move names a real company or row, or is rule 5 or 6.
- Every count matches the Sheet. "This week" uses Dashboard B7 + B8.
- Leads: at most 2, none when Overwhelmed or when 3 or more items need attention, never a Long shot.
- The spark doesn't explain why it was picked, doesn't name a star sign, and has no lyrics.
- The quote or song came from the script, copied exactly.
