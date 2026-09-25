# Setup guide

> **Draft for the friends test.** Screenshots and a plan recommendation come after the test. Menu names in Claude change from time to time; if a step doesn't match what you see, tell us through the feedback form.

**What you'll need:** a Claude account, a Google account, and about 20 minutes.

## 1. Create or sign in to your Claude account
Go to [claude.ai](https://claude.ai) and sign up or sign in. Skills are available on the Free, Pro, and Max plans, according to Anthropic's help center. Which plan works best for FitFactorOS is being measured during this test.

## 2. Turn on the settings FitFactorOS needs
In Claude, open **Settings** and turn on:
- **Code execution and file creation** (under Capabilities). Skills don't work without it.
- **Generate memory from chat history** and **Search and reference chats**. These let Claude use your Intake answers every time you fit factor a job, so you only answer them once.

Research also needs **web search**. In a chat, open the tools menu next to the message box and make sure **Web search** is on.

## 3. Add the skills
1. Download `fitfactoros-intake.zip`, `fitfactoros-research.zip`, and `fitfactoros-activity-log.zip` from this repository's `dist/` folder.
2. In Claude, go to **Customize → Skills**.
3. Click **+** and upload one ZIP file. Repeat for the others.
4. Make sure all the FitFactorOS skills are switched on.

Anthropic's instructions: [Get started with Claude skills](https://support.claude.com/en/articles/12512180).

## 4. Copy the Sheet template into Google Drive
1. Download the Sheet: [fitfactoros-template.xlsx](https://github.com/jeremyjwalsh/fitfactoros/raw/main/sheet/fitfactoros-template.xlsx) (the download starts right away).
2. In Google Drive, click **New → File upload** and choose the file.
3. Double-click the uploaded file to open it.
4. **Click File → Save as Google Sheets.** A new copy opens in a new tab. Use that copy from now on.

> [!IMPORTANT]
> **Don't skip step 4: File → Save as Google Sheets.**
> The file you uploaded is an Excel file. It opens in Google Sheets, but some things won't work until you save it as a Google Sheet.
> **How to check:** an Excel file shows a small **.XLSX** tag next to its name at the top. A Google Sheet doesn't. If you see .XLSX, do step 4.
> You can delete the uploaded .xlsx file afterward.

5. On the other tabs, delete the grey example row when you're ready.

## 5. Create your FitFactorOS Project
1. In Claude, click **Projects**, then **New project**.
2. Name it **FitFactorOS** and create it.
3. Do everything below inside this Project. That's how Claude keeps your answers between chats.

**Tip to save usage:** start a short new chat inside the Project for each task (one job, one log, one update). Long chats use up your Claude plan faster, because Claude re-reads everything earlier in the chat each time.

## 6. Run Intake (once)
1. Inside your FitFactorOS Project, start a new chat.
2. Type: **Start my intake**
3. Answer the questions. Skip anything you like.
4. At the end, Claude shows the steps above your answer block: tap **Copy**, open your Google Sheets copy, go to the **Profile** tab, click cell **B2**, and paste. Your answers fill B2 through B19. Intake asks for your Gmail address at the start; it's used to build links that open your own inbox.

Your Profile is set. You only do this once. If something changes later, say "update my profile."

## 7. Fit factor a job (any time)
1. Inside your FitFactorOS Project, paste a job link and type **fit factor this**. If the link needs a login (LinkedIn often does), paste the job text instead.
2. Claude shows **Company fit**, then **Role fit**, the biggest blocker, and a suggested call.
3. You decide: **Pursue**, **Pass**, or **Go deeper first**. Going deeper uses more of your Claude plan, so save it for jobs you're serious about.
4. Claude gives you a row to paste on the **Jobs** tab. If you chose Pursue, you also get rows for the **Evidence** tab. Click the first empty cell in column A of each tab and paste. Every job gets recorded, even the ones you pass on, so you keep a dated record of your search.

If Claude says it doesn't have your answers, check that you're inside your FitFactorOS Project and that the memory settings in step 2 are on.

## 8. Log your activity (any time)
Tell Claude what you did, inside your FitFactorOS Project: **"I applied to Northwind today"** or **"had coffee with Priya about Fabrikam."** Claude may ask a few quick questions (all skippable), then gives you a row for the **Activity** tab. Click the first empty cell in column A and paste.

## 9. Build your weekly log
Say **"this week's work search log."** Claude asks you to copy your **Activity** rows and **Jobs** rows for the week into the chat (copying the whole tab is fine). You get:
- a log in your state's format, ready to copy into your weekly certification,
- a count against your state's weekly minimum, and a plain warning if you're short,
- rows to add to your Activity tab, so your records stay complete.

Every job you fit factored that week shows up as a job posting you reviewed, even ones you passed on. Looking at jobs is part of looking for work.

**Claude never submits your certification. You do that yourself.** FitFactorOS has rules for **Massachusetts** so far. In other states you still get the log, but "Counts for unemployment" stays blank. This isn't legal advice; check your state's unemployment agency for what it requires.

## Getting updates
FitFactorOS is still being built, and the skills get improved. When there's an update:
1. Download the new ZIP files from the `dist/` folder.
2. In Claude, go to **Customize → Skills**, delete the old FitFactorOS skill (**⋮ → Delete**), and upload the new ZIP.

Your Sheet and your answers stay as they are. You don't need to run Intake again.

**If you set up your Sheet before the Activity Log came out,** make two small changes on the **Activity** tab:
1. Type these headers: **M1** Pay rate, **N1** Employer address, **O1** Contact info.
2. Select column D, click **Data → Data validation**, and add **Reviewed job posting** to the list.

## Coming in later phases
Connecting Google Drive and Gmail (so the weekly log can read your Sheet without copying), the Job Finder, Outreach, and more. See the [Roadmap](../README.md#roadmap).

## Your data
Your answers are saved in your own Google Sheet. FitFactorOS has no server of its own and collects nothing. Your chats with Claude go through Anthropic like any Claude chat, and if Claude's memory feature is on, Claude may remember details between chats. You can control that in Claude's settings. Anthropic's privacy policy covers the rest.
