# Setup guide

> **Draft for the Phase 1 friends test.** Screenshots and a plan recommendation come after the test. Menu names in Claude change from time to time; if a step doesn't match what you see, tell us through the feedback form.

**What you'll need:** a Claude account, a Google account, and about 20 minutes.

## 1. Create or sign in to your Claude account
Go to [claude.ai](https://claude.ai) and sign up or sign in. Skills are available on the Free, Pro, and Max plans, according to Anthropic's help center. Which plan works best for FitFactorOS is being measured during this test.

## 2. Turn on file creation
In Claude, open **Settings → Capabilities** and turn on **Code execution and file creation**. Skills don't work without it.

## 3. Add the Intake skill
1. Download `fitfactoros-intake.zip` from this repository's `dist/` folder.
2. In Claude, go to **Customize → Skills**.
3. Click **+** and upload the ZIP file.
4. Make sure the skill is switched on.

Anthropic's instructions: [Get started with Claude skills](https://support.claude.com/en/articles/12512180).

## 4. Copy the Sheet template into Google Drive
1. Download `sheet/fitfactoros-template.xlsx` from this repository.
2. In Google Drive, click **New → File upload** and choose the file.
3. Right-click the uploaded file and choose **Open with → Google Sheets**. Then use **File → Save as Google Sheets**, so you're working in a Google Sheet rather than an Excel file.
4. On the **Profile** tab, type your Gmail address in cell **B2**. Email links throughout the sheet use it.
5. On the other tabs, delete the grey example row when you're ready.

## 5. Run Intake
1. Start a new chat in Claude.
2. Type: **Start my intake**
3. Answer the questions. Skip anything you like.
4. At the end, tap **Copy** on the answer block, go to your Sheet's **Profile** tab, click cell **B3**, and paste.

That's it. Your Profile is set.

## Coming in later phases
Connecting Google Drive and Gmail, the Research agent ("fit factor this"), and more. See the [Roadmap](../README.md#roadmap).

## Your data
Your answers are saved in your own Google Sheet. FitFactorOS has no server of its own and collects nothing. Your chats with Claude go through Anthropic like any Claude chat, and if Claude's memory feature is on, Claude may remember details between chats. You can control that in Claude's settings. Anthropic's privacy policy covers the rest.
