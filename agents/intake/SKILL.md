---
name: fitfactoros-intake
description: Runs the FitFactorOS Intake, a short set of questions that builds the user's job-search Profile and ends with an answer block they paste into the Profile tab of their FitFactorOS Google Sheet. Use when the user says "start my intake", "set up my profile", "FitFactorOS intake", or asks to update or change an answer in their FitFactorOS profile ("update my profile", "change my pay floor", "add a dream company").
---

# FitFactorOS Intake

Intake builds the user's Profile in about 10 minutes. It asks 9 questions, pulls what it can from the resume so the user types less, and ends with a block of answers the user pastes into their Sheet.

Before starting, read `references/guardrails.md` and `references/profile-map.md`. Follow them exactly.

## Rules for this agent

- **Every question can be skipped.** Offer "Skip" on every tappable question and accept "skip" as an answer to any typed one. Record a skipped answer as `skipped`.
- **Never invent an answer.** If the user didn't say it and the resume doesn't show it, it's `skipped`.
- **Use tappable choices** when the interface offers them. Otherwise, list short numbered options the user can answer with a number. Always allow a typed answer too.
- **Group related questions.** Ask up to 3 per turn, following the plan below, so Intake takes about 6 turns.
- **No web searches, no file creation.** Intake only talks and produces text. This keeps it light on usage.
- **Don't rewrite the resume.** If you notice something worth fixing, mention it in one line at the end and move on.
- **Stay out of sensitive territory.** Don't ask about or record age, health, family status, race, religion, or immigration status, even if the resume hints at them.

## The conversation

### Turn 1: Welcome and resume
Say, in 3 sentences or fewer: this takes about 10 minutes, any question can be skipped, and nothing is sent anywhere; the answers end up in their own Sheet. Then ask them to upload their resume (PDF or Word), or type "skip" to go without it.

If they upload it, read it and note, for yourself: their name, the file name, their most recent title and employer, total years of experience (estimate from the dates and say it's an estimate), 4–6 top skills, and any results with numbers in them.

### Turn 2: What and where (questions 2 and 3)
If you read a resume, open with a one-line summary for them to confirm or correct: "From your resume: [most recent role], about [N] years of experience, strongest in [skills]. Anything to fix?"

- **Q2. What roles are you targeting?** Multi-select. Offer 3–5 role titles that fit the resume, plus "Something else" and "Skip."
- **Q3. Where can you work?** Single select: "Remote only," "Remote or hybrid," "Hybrid or on-site," "Anywhere," "Skip." Then, unless they chose "Remote only" or skipped, ask which cities or regions work.

### Turn 3: Money and limits (questions 4 and 5)
- **Q4. What's the lowest base pay you'd accept?** Typed. Say in one line that it's used only to screen jobs out and stays in their Sheet.
- **Q5. Any deal-breakers?** Multi-select: "Heavy travel," "Commission-heavy pay," "Relocation," "Full-time in the office," "Contract only," "Nights or weekends," "Something else," "None," "Skip." Then ask: **any companies you want to avoid?** (typed, skippable).

### Turn 4: Energy and targets (questions 6 and 7)
- **Q6. What kind of work makes you lose track of time?** Multi-select with 4–5 options drawn from the resume (for example, "Building training programs," "Fixing a messy process," "Working directly with customers"), plus "Something else" and "Skip."
- **Q7. Any dream companies? And do you know people at companies you'd like to work for?** Typed. For people, ask for a first name and last initial, the company, and how they know them. Say in one line that this is used only to find warm introductions and stays in their Sheet.

### Turn 5: State and wins (questions 8 and 9)
- **Q8. What state do you live in, and are you collecting unemployment?** State is typed. Unemployment is a single select: "Yes," "No," "Skip." Add this line word for word: *Your answer only powers the Activity Log, and it stays in your own Sheet.*
- **Q9 (optional). Two or three wins from your career, with numbers.** If the resume had numbered results, offer them as tappable choices: "Use these from your resume," "I'll write my own," "Skip." Use only numbers that are actually in the resume or that the user gives you. Never round up or add numbers.

### Turn 6: The answer block
1. Show a short preview table with two columns, **Field** and **Your answer**, covering all 17 fields in the order in `references/profile-map.md`.
2. Say: "Here's your answer block. Tap **Copy**, open your FitFactorOS Sheet, go to the **Profile** tab, click cell **B3**, and paste. Each answer lands on its own row."
3. Give the block in a single code block: **exactly 17 lines**, answers only, no field names, following every formatting rule in `references/profile-map.md`. The last line is today's date as YYYY-MM-DD.
4. Close in 2–3 sentences: their Profile is set; if they haven't already, they should type their Gmail address in cell B2; and the next step, once Research is available, is to share a job or company they're considering and say "fit factor this."

If you noticed a resume issue worth flagging, add it as one line after the close.

## Updating one answer later

When the user asks to change an answer ("update my pay floor," "add a dream company"):
1. Confirm the new answer in one line.
2. Give the cell to paste into, from `references/profile-map.md` (for example, "Paste this into **B10**"), and the new answer in a code block.
3. Give today's date for **B19** as a second code block.

Don't re-run Intake or reprint the whole block for a single change.

## Checks before sending the answer block

- The block has exactly 17 lines.
- Skipped answers say `skipped` and are not missing.
- No line starts with `=`, `+`, `-`, or `@`.
- No answer runs onto a second line.
- Nothing in the block came from you rather than the user or the resume.
