---
name: fitfactoros-intake
description: Runs the FitFactorOS Intake, a short set of questions that builds the user's job-search Profile and ends with an answer block they save in their FitFactorOS Project and, if they use it, paste into the Profile tab of their FitFactorOS Google Sheet. Use when the user says "start my intake", "set up my profile", "FitFactorOS intake", or asks to update or change an answer in their FitFactorOS profile ("update my profile", "update my FitFactorOS profile", "change my pay floor", "add a dream company", "add a contact"). Inside a FitFactorOS Project, "update my profile" always means this Profile; go straight to the update without asking which profile.
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
- Buttons are for real answers only. The buttons already come with their own "Something else" and "Skip" choices, so don't spend a slot on them and don't add a line telling the user to type their own answer.

If there are no tappable choices, ask the same questions as short numbered lists the user can answer with numbers or words.

## The conversation (5 turns)

### Turn 1: Welcome, resume, and Gmail
Start with this line, word for word: *Thanks for giving FitFactorOS a try. I built it for people in the middle of a job search, and I'm rooting for you. — Jeremy*

Then, in 3 sentences or fewer: this takes about 10 minutes; every question can be skipped; you won't send or submit anything, and the answers end up in their own Sheet.

Then add this line word for word: *Tip: run this inside your FitFactorOS Project in Claude, so I can use your answers every time you ask me to fit factor a job.*

Then add this line word for word: *You don't need anything else set up to start. At the end, I'll show you where to save your answers.*

Then ask, in one message:
1. Their resume (PDF or Word), or "skip" to go without it.
2. *(Optional)* The Gmail address they'll use with FitFactorOS. Say why: *"Only if you'll use the FitFactorOS Google Sheet: it builds links that open your own inbox. Skip it if you're not sure."*

If they give no Gmail address, record it as `skipped` and don't ask again.

If they upload it, note for yourself: their name, the file name, their most recent title and employer, total years of experience (from the dates; mark it as an estimate), 4–6 top skills, and any results with numbers in them.

### Turn 2: Tappable (questions 2, 3, 5)
If you read a resume, start with a one-line summary: "From your resume: [most recent role], about [N] years of experience, strongest in [skills]. You can correct any of this in a minute." Then ask:

- **Q2. What roles are you targeting?** Multi-select, up to 4 titles that fit the resume. *With no resume, leave Q2 out of this turn; it's asked as typed in Turn 4.*
- **Q3. Where can you work?** Single select: "Remote only," "Remote or hybrid," "Hybrid or on-site," "Anywhere."
- **Q5. Any of these deal-breakers?** Multi-select: "Heavy travel," "Commission-heavy pay," "Full-time in the office," "Relocation." Say above the buttons that they can add others in the next step.

### Turn 3: Tappable (questions 6, 8, and 9)
Above the buttons, add this line word for word: *Your unemployment answer only powers the Activity Log, and it goes in your own Sheet.*

Then ask:
- **Q6. What kind of work makes you lose track of time?** Multi-select, 4 options. With a resume, draw them from it (for example, "Building training programs," "Fixing a messy process"). Without one, use: "Solving tough problems," "Teaching or coaching others," "Building something new," "Working directly with customers."
- **Q8. Are you collecting unemployment?** Single select: "Yes," "No," "Prefer not to say." Record "Prefer not to say" as `skipped`.
- **Q9. Wins with numbers.** *Only if the resume had numbered results:* put up to 3 of them **inside the question text itself**, in short form, so the user sees exactly what they're approving. Short form means about 10 words or fewer each, with every number kept exactly as the resume has it. Example: *"Use these wins from your resume? (1) Cut onboarding from 60 to 35 days (2) Renewed 96% of a $4M book."* Single select: "Use these" or "I'll write my own." (Skip comes with the buttons.) *With no numbered results, leave Q9 out of this turn; it's asked as typed in Turn 4.*

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
9. People you know at companies you'd like to work for. For each person: first name and last initial, **where they work now**, and how you know them. For example: "Priya N. at Fabrikam Health, former teammate." *(It's used only to find warm introductions, and it goes in your own Sheet.)*
10. What state do you live in?
11. *(If they chose "I'll write my own," or had no numbered results)* Two or three wins from your career, with numbers. One short line each. Optional.

### Turn 5: The answer block
Give these in this order:

1. **Steps first, above the block.** Word for word:

   **Next: save your answers in your Project (do this now)**
   This is how I find your answers every time you say **fit factor this**, in any chat in this Project.
   1. Tap **Copy** on the block below.
   2. Open your FitFactorOS Project: click its name at the top of this chat, or find it under **Projects** in the left sidebar.
   3. On the right of the Project page, find **Context** and click its **Add** button, then **Add text content**.
   4. Type **My FitFactorOS answers** as the **Title**, paste into **Content**, and click **Add Content**.

   **Using the FitFactorOS Sheet too?** Open your Sheet in Google Sheets, click the **Profile** tab, click cell **B2**, and paste (**Ctrl+V** on Windows, **Cmd+V** on Mac). Your answers fill **B2 through B19**. No Sheet yet? That's fine. You can set it up later: [setup guide, "Keep a record in your Sheet"](https://github.com/jeremyjwalsh/fitfactoros/blob/main/docs/setup.md#7-keep-a-record-in-your-sheet-optional).

2. **The block**, in a single code block: **exactly 18 lines**, answers only, no field names, following every rule in `references/profile-map.md`. The first line is the Gmail address; the last line is today's date as YYYY-MM-DD.
3. **Preview table below the block**, with two columns, **Field** and **Your answer**, covering all 18 fields in the order in `references/profile-map.md`. Introduce it in a few words, such as "Here's what goes where."
4. Close in 2–3 sentences: their Profile is set. Then this, word for word: **Next:** start a new chat in your FitFactorOS Project, paste a job link (and the job description, for the best result), and say **fit factor this**.

If you noticed a resume issue worth flagging, add it as one line after the close.

## How specific answers are recorded

- **Years of experience (B6):** if you estimated it from resume dates and the user didn't confirm or correct it, write it as "About N (estimate)." If they confirmed it, write the number.
- **Wins (B18):** keep each win short, about 10 words or fewer, and at most 3 wins. Use only numbers that appear in the resume or that the user typed, exactly as given. Never round up or add numbers. Separate wins with "; ".
- **Lists:** separate items with "; ".

## Updating one answer later

When the user asks to change an answer ("update my pay floor," "add a dream company"):
Inside a FitFactorOS Project, don't ask which profile they mean. If they haven't said what to change, ask which answer, in one line.

1. **Never fill in anything yourself.** For a person on the People line, you need their name, where they work now, and how the user knows them. If any part is missing, ask once. If the user skips "how," write `Name at Company` with nothing after it. Never use a job title or anything from memory in its place.
2. **List fields (Top skills, Target roles, Where you can work, Deal-breakers, Companies to avoid, Work, Dream companies, People, Wins): always give the whole line,** never a piece to add on. Find the current answer the same way Research does (newest Intake in this chat, the "My FitFactorOS answers" file in this Project, or past chats in this Project). If you can't find it, ask the user to copy the cell and paste it here, then build the full new line. If the current answer is `skipped` or `None`, the new line is just the new item. The line never starts with "; ".
3. Confirm the new answer in one line.
4. Give the paste steps with the cell **and** its row label, word for word in this shape: "Click cell **B15** (the **People you know** row) and paste. This replaces what's there." Then the new answer in a code block.
5. Give today's date for **B19** (the **Profile last updated** row) in a second code block.
6. Then this line, word for word: *Saved your answers in your Project? Open **My FitFactorOS answers** (under **Context** on the Project page) and change the same line, and the date on the last line, so fit factor uses the new answer.*

Don't re-run Intake or reprint the whole block for a single change.

## Checks before sending the answer block

- The block has exactly 18 lines, and the first line is the Gmail address or `skipped`.
- Skipped answers say `skipped`; no line is missing.
- No line starts with `=`, `+`, `-`, `@`, or `"`.
- No answer runs onto a second line.
- Nothing in the block came from you rather than from the user or the resume.
- The paste steps say **B2**, and the block starts with the Gmail line.
- Every person on the People line (line 14) has a company. If one is missing, ask once where they work now; if the user skips, record them as "[Name] at company unknown".
- Wins (line 17) are short, and every number matches the resume or what the user typed.
