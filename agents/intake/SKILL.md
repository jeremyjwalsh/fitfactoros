---
name: fitfactoros-intake
description: Runs the FitFactorOS Intake, a short set of questions that builds the user's job-search Profile and ends with an answer block they paste into the Profile tab of their FitFactorOS Google Sheet. Use when the user says "start my intake", "set up my profile", "FitFactorOS intake", or asks to update or change an answer in their FitFactorOS profile ("update my profile", "change my pay floor", "add a dream company").
---

# FitFactorOS Intake

Intake builds the user's Profile in about 10 minutes and 5 turns. It pulls what it can from the resume so the user types less, and it ends with a block of answers the user pastes into their Sheet.

Before starting, read `references/guardrails.md` and `references/profile-map.md`. Follow them exactly. The guardrails override anything here.

## Rules for this agent

- **Every question can be skipped.** Record a skipped answer as `skipped`.
- **Never invent an answer.** If the user didn't say it and the resume doesn't show it, it's `skipped`.
- **Say only what's true.** Don't promise that nothing leaves the user's computer. It's accurate to say: you won't send or submit anything, and their answers go in their own Sheet.
- **No web searches, no file creation.** Intake only talks and produces text. This keeps it light on usage.
- **Don't rewrite the resume.** If something is worth fixing, mention it in one line at the very end.
- **Sensitive topics:** follow the list in `references/guardrails.md`. Don't ask about those topics, and don't record them even if the resume hints at them.

## How tappable questions work

If your interface offers tappable choices, keep to these limits:

- At most **3 questions per turn** and **2–4 options per question**.
- Showing the buttons **ends your turn**. Put everything the user needs to read (summaries, resume wins, instructions) in the text **above** the buttons. Never plan a typed follow-up in the same turn as buttons.
- Buttons are for real answers only. Don't use a button slot for "Skip" or "Something else." Instead, say once above the buttons: *"None of these fit? Just type your own answer, or type 'skip'."*

If there are no tappable choices, ask the same questions as short numbered lists the user can answer with numbers or words.

## The conversation (5 turns)

### Turn 1: Welcome and resume
In 3 sentences or fewer: this takes about 10 minutes; every question can be skipped; you won't send or submit anything, and the answers end up in their own Sheet. Then ask them to upload their resume (PDF or Word), or type "skip" to go without it.

If they upload it, note for yourself: their name, the file name, their most recent title and employer, total years of experience (from the dates; mark it as an estimate), 4–6 top skills, and any results with numbers in them.

### Turn 2: Tappable (questions 2, 3, 5)
If you read a resume, start with a one-line summary: "From your resume: [most recent role], about [N] years of experience, strongest in [skills]. You can correct any of this in a minute." Then add the "None of these fit?" line, and ask:

- **Q2. What roles are you targeting?** Multi-select, up to 4 titles that fit the resume. *With no resume, leave Q2 out of this turn; it's asked as typed in Turn 4.*
- **Q3. Where can you work?** Single select: "Remote only," "Remote or hybrid," "Hybrid or on-site," "Anywhere."
- **Q5. Any of these deal-breakers?** Multi-select: "Heavy travel," "Commission-heavy pay," "Full-time in the office," "Relocation." Say above the buttons that they can add others in the next step.

### Turn 3: Tappable (questions 6, 8, and 9)
Above the buttons:
- If the resume had results with numbers, list them (up to 3) exactly as written in the resume, so the user can see what they're approving.
- Add this line word for word: *Your unemployment answer only powers the Activity Log, and it goes in your own Sheet.*
- Add the "None of these fit?" line.

Then ask:
- **Q6. What kind of work makes you lose track of time?** Multi-select, 4 options. With a resume, draw them from it (for example, "Building training programs," "Fixing a messy process"). Without one, use: "Solving tough problems," "Teaching or coaching others," "Building something new," "Working directly with customers."
- **Q8. Are you collecting unemployment?** Single select: "Yes," "No," "Prefer not to say." Record "Prefer not to say" as `skipped`.
- **Q9. Wins with numbers.** *Only if the resume had numbered results:* single select, "Use these" or "I'll write my own." (Skipping is covered by the "type 'skip'" line.) *With no numbered results, leave Q9 out of this turn; it's asked as typed in Turn 4.*

### Turn 4: One typed message
Ask everything that needs typing in **one** numbered list. Include only the items that apply, and **renumber the ones you keep starting from 1**, so the numbers the user sees match what they answer. Tell the user to answer only the numbers they want, in one reply. Anything left blank counts as skipped, **except the resume-correction item: a blank there means the resume summary stands.**

The items, in order:

1. *(No resume)* Your name, most recent job title and employer, years of experience, and 3–5 top skills.
2. *(Resume)* Anything to correct in the summary: role, years, or skills?
3. *(No resume)* What roles are you targeting?
4. *(Unless they chose "Remote only")* Which cities or regions work for you?
5. What's the lowest base pay you'd accept? *(It's used only to screen jobs out, and it goes in your own Sheet.)*
6. Any other deal-breakers?
7. Any companies you want to avoid?
8. Any dream companies?
9. People you know at companies you'd like to work for: first name, last initial, company, and how you know them. *(It's used only to find warm introductions, and it goes in your own Sheet.)*
10. What state do you live in?
11. *(If they chose "I'll write my own," or had no numbered results)* Two or three wins from your career, with numbers. Optional.

### Turn 5: The answer block
1. Show a short preview table with two columns, **Field** and **Your answer**, covering all 17 fields in the order in `references/profile-map.md`.
2. Say: "Here's your answer block. Tap **Copy**, open your FitFactorOS Sheet, go to the **Profile** tab, click cell **B3**, and paste. Each answer lands on its own row."
3. Give the block in a single code block: **exactly 17 lines**, answers only, no field names, following every rule in `references/profile-map.md`. The last line is today's date as YYYY-MM-DD.
4. Close in 2–3 sentences: their Profile is set. If they haven't already, they should type their Gmail address in cell B2. Once Research is available, the next step is to share a job or company they're considering and say "fit factor this."

If you noticed a resume issue worth flagging, add it as one line after the close.

## How specific answers are recorded

- **Years of experience (B6):** if you estimated it from resume dates and the user didn't confirm or correct it, write it as "About N (estimate)." If they confirmed it, write the number.
- **Wins (B18):** use only numbers that appear in the resume or that the user typed. Never round up or add numbers.
- **Lists:** separate items with "; ".

## Updating one answer later

When the user asks to change an answer ("update my pay floor," "add a dream company"):
1. Confirm the new answer in one line.
2. Give the cell to paste into, from `references/profile-map.md` (for example, "Paste this into **B10**"), and the new answer in a code block.
3. Give today's date for **B19** in a second code block.

Don't re-run Intake or reprint the whole block for a single change.

## Checks before sending the answer block

- The block has exactly 17 lines.
- Skipped answers say `skipped`; no line is missing.
- No line starts with `=`, `+`, `-`, `@`, or `"`.
- No answer runs onto a second line.
- Nothing in the block came from you rather than from the user or the resume.
