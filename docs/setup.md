# Setup guide

> **Draft for the friends test.** Screenshots and a plan recommendation come after the test. Menu names in Claude change from time to time; if a step doesn't match what you see, tell us through the feedback form.

**What you'll need:** a Claude account, a Google account, and about 20 minutes.

**Built for Claude.** FitFactorOS is built and tested on Claude. The skills use the open SKILL.md format, so parts of it may work in other AI tools (ChatGPT, for example), but that hasn't been tested. The one-click install, the dashboard page, and the morning email rely on Claude features and are Claude-only for now.

## 1. Create or sign in to your Claude account
Go to [claude.ai](https://claude.ai) and sign up or sign in.

**Which plan?** Plugins, the easiest way to add FitFactorOS, need a paid plan (Pro, Max, Team, or Enterprise), according to Anthropic's help center. On the Free plan you can still add the five skills by hand (step 3, Option B), but you won't get updates automatically. Which plan works best for FitFactorOS is being measured during this test.

## 2. Turn on the settings FitFactorOS needs
In Claude, open **Settings** and turn on:
- **Code execution and file creation** (under Capabilities). Skills don't work without it.
- **Generate memory from chat history** and **Search and reference chats**. These let Claude use your Intake answers every time you fit factor a job, so you only answer them once.

Then, in Claude's **connectors**, connect **Google Sheets**. This lets Claude read your Sheet when you say **show my dashboard**. Claude only reads it, never changes it.

Research also needs **web search**. In a chat, open the tools menu next to the message box and make sure **Web search** is on.

## 3. Add FitFactorOS to Claude

**Already added the FitFactorOS skills from ZIP files?** Remove them first, or two copies will both answer "fit factor this." In **Customize → Skills**, open each FitFactorOS skill and choose **⋮ → Delete**. Your Sheet and your Intake answers aren't affected.

### Option A: add the plugin (Pro plan or above, recommended)
1. In Claude, go to **Customize → Plugins**.
2. Click **Add** (top right), then **Add marketplace**.
3. Enter `jeremyjwalsh/fitfactoros`. Leave **Sync automatically** off unless you have a GitHub account (see "Getting updates" below). Click **Sync**.
4. Click **Discover**. Find the **FitFactorOS** card (it may be partway down the page, under "New plugins") and click its **+**.
5. Click **Yours**. FitFactorOS should be listed under "From marketplaces you added." If it isn't, it isn't installed yet: go back to step 4.

**Skip "Try in chat."** It opens a chat outside your FitFactorOS Project, where Claude can't find your Intake answers. Always use FitFactorOS from a new chat inside your Project (see "5. Create your FitFactorOS Project" below).

All five skills (Intake, Research, Activity Log, Dashboard, Morning Email) come in one plugin.

Anthropic's instructions: [Plugins](https://claude.com/docs/plugins/overview).

### Option B: add the skills by hand (Free plan, or if Option A doesn't show for you)
1. Download all five skills (each download starts right away):
   - [fitfactoros-intake.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-intake.zip)
   - [fitfactoros-research.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-research.zip)
   - [fitfactoros-activity-log.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-activity-log.zip)
   - [fitfactoros-dashboard.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-dashboard.zip)
   - [fitfactoros-morning-email.zip](https://github.com/jeremyjwalsh/fitfactoros/raw/main/dist/fitfactoros-morning-email.zip) (optional; the weekday schedule needs a paid plan, but you can ask for one any time)
2. In Claude, go to **Customize → Skills**.
3. Click **+** and upload one ZIP file. Repeat for the others. Don't unzip them first.
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
3. You decide: **Pursue**, **Hold** (park it and come back in a week), **Pass**, or **Go deeper first**. Going deeper uses more of your Claude plan, so save it for jobs you're serious about.
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

## 10. Optional: the morning email
A one-minute weekday email that lands in your Gmail **Drafts**: how you're doing, what needs attention, and the one thing to do today, with a quote, a song, or something funny at the top. It's a draft to you and is never sent.

1. Connect **Gmail** and **Google Sheets** in Claude (**Customize → Connectors**), if you haven't already.
2. In your FitFactorOS Project, say **set up my morning email** and answer three quick questions. All can be skipped.
3. Paste the 4 answers it gives you into your Sheet's **Profile** tab, starting at **B20**.
4. On Pro and above, Claude sets it up as a weekday scheduled task and makes your first one right away. On the Free plan, say **morning email** any morning to get the same draft.

Look for it in **Drafts**, not your inbox. Old drafts aren't deleted for you, so delete each one after you read it. To stop, say **stop my morning email**.

**Older Sheets:** if your Profile tab has no labels in rows 20 to 23, type **Morning email sparks**, **Sign (optional)**, **Morning email ready by**, and **Dashboard link** into A20 through A23 first, and move any notes in those rows further down.

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
| **set up my morning email** | An optional weekday email draft with your one next move |
| **morning email** | Today's email draft, any time |
| **stop my morning email** | Turns the weekday email off |

## Getting updates
FitFactorOS is still being built, and the skills get improved. See [CHANGELOG.md](../CHANGELOG.md) for what changed.

**If you added the plugin (Option A):**
1. Go to **Customize → Plugins**, click **Add**, then **Manage marketplaces**.
2. Click the **⋮** next to **fitfactoros**, then **Check for updates**.
3. Start a new chat in your Project to use the new version. Chats you already had open may keep the old one.

The "Synced commit" code under fitfactoros shows which version you have. If you have a GitHub account, you can turn on **Sync automatically** in that same menu so updates arrive on their own. Claude will ask you to give its GitHub app access to the FitFactorOS repository first.

**If you added the skills by hand (Option B):**
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
