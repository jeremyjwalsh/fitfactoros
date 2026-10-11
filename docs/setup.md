# Setup guide

> **Draft for the friends test.** Screenshots and a plan recommendation come after the test. Menu names in Claude change from time to time; if a step doesn't match what you see, tell us through the feedback form.

**What you'll need:** a Claude account, a Google account, and about 20 minutes.

## 1. Create or sign in to your Claude account
Go to [claude.ai](https://claude.ai) and sign up or sign in. Skills are available on the Free, Pro, and Max plans, according to Anthropic's help center. Which plan works best for FitFactorOS is being measured during this test.

## 2. Turn on the settings FitFactorOS needs
In Claude, open **Settings** and turn on:
- **Code execution and file creation** (under Capabilities). Skills don't work without it.
- **Generate memory from chat history** and **Search and reference chats**. These let Claude use your Intake answers every time you fit factor a job, so you only answer them once.

Then, in Claude's **connectors**, connect **Google Sheets**. This lets Claude read your Sheet when you say **show my dashboard**. Claude only reads it, never changes it.

Research also needs **web search**. In a chat, open the tools menu next to the message box and make sure **Web search** is on.

## 3. Add the skills
1. Download all four skills (each download starts right away):
   - [fitfactoros-intake.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-intake.zip)
   - [fitfactoros-research.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-research.zip)
   - [fitfactoros-activity-log.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-activity-log.zip)
   - [fitfactoros-dashboard.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-dashboard.zip)
2. In Claude, go to **Customize → Skills**.
3. Click **+** and upload one ZIP file. Repeat for the other three. Don't unzip them first.
4. Make sure all four FitFactorOS skills are switched on.

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

**Permission prompts:** Claude may ask before it reads a web page, searches, or opens a job page in your browser. **Allow** those; that's the research. FitFactorOS never sends, writes, or deletes anything, so if a prompt asks to send an email or change a file, choose **Deny**.

**Your Dashboard:** the first tab of your Sheet is a quick summary that fills in by itself as you paste rows. For the full view (your top picks, each job's ladder, its evidence, who to write to), say **show my dashboard** in your Project. Claude reads your Sheet through the Google Sheets connector from step 2 and makes a private page only you can see. Each view uses a little of your Claude plan.

**Tip to save usage:** start a short new chat inside the Project for each task (one job, one log, one update). Long chats use up your Claude plan faster, because Claude re-reads everything earlier in the chat each time.

## 6. Run Intake (once)
1. Inside your FitFactorOS Project, start a new chat.
2. Type: **Start my intake**
3. Answer the questions. Skip anything you like.
4. At the end, Claude shows the steps above your answer block: tap **Copy**, open your Google Sheets copy, go to the **Profile** tab, click cell **B2**, and paste. Your answers fill B2 through B19. Intake asks for your Gmail address at the start; it's used to build links that open your own inbox.

Your Profile is set. You only do this once. If something changes later, say "update my FitFactorOS profile." Claude tells you the exact cell and row to paste into.

## 7. Fit factor a job (any time)
1. Inside your FitFactorOS Project, paste a job link and type **fit factor this**.
   - **For the best result, paste the job description too.** Many job sites (Ashby, Workday, LinkedIn) don't let Claude read the whole page. On the posting, select all, copy, and paste it **in its own message first**, then send the link with **fit factor this**. If Claude can only read part of a page, it stops and asks for the text rather than guessing.
   - Scores can move a few points between runs on the same job. The suggested call is what to go by.
   - **Optional: Claude in Chrome.** This browser add-on lets Claude open job pages in your own Chrome, which helps on sites like Ashby and Workday. It acts in your real browser with your sign-ins, and it asks before opening a page. Skip it if you'd rather not; pasting the job description works just as well.
   - **Keep a Fit Report:** after **Go deeper first**, if you see **Create a doc** under Claude's reply, tap it to save the report as a doc you can keep or share.
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

## Things you can say

| Say this | What happens |
|---|---|
| **start my intake** | Builds your Profile (about 10 minutes) |
| **update my profile** (or "change my pay floor," "add a contact") | Changes one answer |
| **fit factor this** + a job link | Company fit, then Role fit, then you decide |
| **go deep** | Deeper research on a job you're serious about |
| **log this** (or "I applied to…," "I had a call with…") | Activity rows to paste |
| **this week's work search log** | Your weekly unemployment log |
| **did I do enough this week?** | Your count against your state's minimum |
| **show my dashboard** (or "where do I stand?") | Your top picks, ladders, and this week, on a private page |

## Getting updates
FitFactorOS is still being built, and the skills get improved. When there's an update:
1. Download the new ZIP files using the links in step 3.
2. In Claude, go to **Customize → Skills**, delete the old FitFactorOS skill (**⋮ → Delete**), and upload the new ZIP.

Your Sheet and your answers stay as they are. You don't need to run Intake again.

**If you set up your Sheet before the Activity Log came out,** make two small changes on the **Activity** tab:
1. Type these headers: **M1** Pay rate, **N1** Employer address, **O1** Contact info.
2. Select column D, click **Data → Data validation**, and add **Reviewed job posting** to the list.

## Coming in later phases
The weekly log reading your Sheet through Google Sheets (so you don't have to copy rows), the Job Finder, Outreach, and more. See the [Roadmap](../README.md#roadmap).

## Your data
Your answers are saved in your own Google Sheet. FitFactorOS has no server of its own and collects nothing. Your chats with Claude go through Anthropic like any Claude chat, and if Claude's memory feature is on, Claude may remember details between chats. You can control that in Claude's settings. Anthropic's privacy policy covers the rest.
