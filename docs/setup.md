# Setup guide

> **Draft for the friends test.** Screenshots and a plan recommendation come after the test. Menu names in Claude change from time to time; if a step doesn't match what you see, tell us through the feedback form.

**What you'll need:** a Claude account, a Google account, and about 20 minutes.

## 1. Create or sign in to your Claude account
Go to [claude.ai](https://claude.ai) and sign up or sign in. Skills are available on the Free, Pro, and Max plans, according to Anthropic's help center. Which plan works best for FitFactorOS is being measured during this test.

## 2. Turn on file creation and web search
In Claude, open **Settings → Capabilities** and turn on **Code execution and file creation**. Skills don't work without it.

Research also needs **web search**. In a chat, open the tools menu next to the message box and make sure **Web search** is on.

## 3. Add the skills
1. Download `fitfactoros-intake.zip` and `fitfactoros-research.zip` from this repository's `dist/` folder.
2. In Claude, go to **Customize → Skills**.
3. Click **+** and upload one ZIP file. Repeat for the other.
4. Make sure both skills are switched on.

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

## 5. Run Intake
1. Start a new chat in Claude.
2. Type: **Start my intake**
3. Answer the questions. Skip anything you like.
4. At the end, Claude shows the steps above your answer block: tap **Copy**, open your Google Sheets copy, go to the **Profile** tab, click cell **B2**, and paste. Your answers fill B2 through B19. Intake asks for your Gmail address at the start; it's used to build links that open your own inbox.

That's it. Your Profile is set.

## 6. Screen your first job
1. Start a new chat in Claude.
2. Type **fit factor this** and paste a job link or the job text. If the link needs a login (LinkedIn often does), paste the text instead.
3. Claude asks for your Profile the first time in each chat. On the **Profile** tab, select cells **B2 through B19**, copy, and paste them into the chat.
4. You get a fit score, the reasons, and two rows to paste: one on the **Jobs** tab and one or more on the **Evidence** tab. Click the first empty cell in column A of each tab and paste.
5. Want more? Choose **Go deep**. Deep research uses more of your Claude plan, so save it for jobs you're serious about.

## Coming in later phases
Connecting Google Drive and Gmail, the Job Finder, Outreach, and more. See the [Roadmap](../README.md#roadmap).

## Your data
Your answers are saved in your own Google Sheet. FitFactorOS has no server of its own and collects nothing. Your chats with Claude go through Anthropic like any Claude chat, and if Claude's memory feature is on, Claude may remember details between chats. You can control that in Claude's settings. Anthropic's privacy policy covers the rest.
