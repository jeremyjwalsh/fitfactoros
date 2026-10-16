# Changelog

What changed in each FitFactorOS update, newest first. Your Sheet and your Intake answers carry over between updates unless a note here says otherwise.

## 2026-10-15 (night)

### Morning email setup
- The sign question now says **zodiac sign**. Not sure of yours? Give your birthday month and day instead (never the year). Claude works out the sign and saves only the sign.
- The sign and the dashboard link are now two separate, simpler questions (four questions in all, every one skippable).
- The ready-by time is written as **Weekdays at 7:00 am**, so Google Sheets keeps it as text instead of turning it into a time value. Existing entries still work.

### Morning email: the weekly number
- The middle tile is now **Counted**: only activities that count for unemployment, against your weekly minimum ("2 of 3"). Jobs screened this week show on their own line underneath. Before, the two were added together, so the same job could count twice and the tile could read "7 of 3." It now matches your dashboard page.

### Your Sheet
- **Dashboard B10** ("On track this week?") now uses counting activities only, for the same reason. **Older Sheets:** the [setup guide](docs/setup.md) has the one-cell fix.

### Also
- README: "Coming next" now matches the Roadmap (Job Finder and Outreach). Job Finder and Outreach are marked *(planned)* in the agents table. The V2 "Momentum check-in" is now a **Friday look-back** in the morning email, since the email already covers the daily check-in.
- Plugin description now lists the morning email. README and setup guide say "download the Sheet template and save it as a Google Sheet" instead of "copy," since there's no Make a copy link. Morning email design page heading updated.
- New page: [Want to go further?](docs/learn-more.md), with free official Anthropic courses and help pages on Projects, Skills, and scheduled tasks. Linked from the README and the setup guide.

## 2026-10-15 (evening)

### New: the morning email (optional)
- Say **set up my morning email** for a one-minute weekday email in your Gmail **Drafts**. It answers three questions: How am I doing? What deserves my attention? What's the one thing I can do today?
- At the top: a quote, a song, or something funny, picked to suit you and your week. Quotes come from a short list where every quote's wording and source has been checked.
- It reads your Sheet and your job alert emails (read-only), shows at most 2 new leads, and skips them entirely on busy weeks. It never sends anything.
- On Pro and above it runs as a weekday scheduled task. On the Free plan, say **morning email** to get one any time.
- Needs Gmail and Google Sheets connected in Claude. See the [setup guide](docs/setup.md), step 10, and [how it decides what to show](docs/morning-email.md).

### Your Sheet
- Four new optional rows on the **Profile** tab, B20 to B23, for the morning email. **Older Sheets:** type **Morning email sparks**, **Sign (optional)**, **Morning email ready by**, and **Dashboard link** into A20 through A23, and move the "How to use this tab" notes further down. Only needed if you use the morning email.

### Research
- "Nothing found" is never used as a tag. When Research looks for something and doesn't find it (layoffs, news), it records that as **Inferred**, with what it searched.
- Comparisons between a job and your answers ("your experience covers the must-haves," "fits your pay floor") are always **Inferred**, even when both sides are Verified.
- The row builder now refuses both mistakes.

### Also
- Guardrails: one exception to "humans send everything." The opt-in morning email may save one draft addressed to you. It never sends it.
- Intake ends with a one-line mention of the morning email.
- README and setup guide: a note that FitFactorOS is built and tested on Claude. Other AI tools are untested.

## 2026-10-15 (afternoon)

- README: new **A note from Jeremy** and **What to expect** sections near the top. Roadmap adds the morning email and "no more copy and paste."
- Research: a new **Hold** choice next to Pursue, Pass, and Go deeper first. Hold parks the job (recorded as Maybe) with a revisit date a week out.
- Intake: opens with a short thank-you.

## 2026-10-15

### Setup clarifications (same day)
- Setup guide: clearer plugin steps (where the **+** is, how to check it installed), how to **Check for updates**, and why to skip "Try in chat."
- **Sync automatically** is optional: it needs a GitHub account and access for Claude's GitHub app. Everyone else uses **Check for updates**.
- The old `agents/` folder was removed. Everything in it now lives in `plugins/fitfactoros/skills/`.

### New way to install: plugin marketplace
- FitFactorOS is now a Claude plugin. On a Pro plan or above, add it once in **Customize → Plugins → Add → Add marketplace** with `jeremyjwalsh/fitfactoros`, and updates reach you without reinstalling. See the [setup guide](docs/setup.md), step 3.
- The four skill ZIPs in `dist/` are still here for the Free plan, built from the same files as the plugin.
- **Already using the ZIP skills?** Delete them in **Customize → Skills** before adding the plugin, so two copies don't both answer "fit factor this."

### Changed
- The skills moved from `agents/` to `plugins/fitfactoros/skills/`. Their names and what they do are unchanged.
- The shared guardrails moved to `docs/guardrails.md`.
- README: new install step, a "Feedback and support" section, a thank-you to JobFinderOS, and an updated repository layout.
- Roadmap: Job Finder now includes bringing your own leads. Negotiation and Close the loop added to V2.

## Earlier (September to October 2026)

- **Setup fixes:** download links for all four skills, and connecting Google Sheets moved up in the setup guide.
- **Dashboard:** "show my dashboard" reads your Sheet (read-only) and makes a private page with your top picks, each job's ladder, its tagged evidence, and parked Maybes.
- **Activity Log:** "log this" and "this week's work search log," with Massachusetts rules first.
- **Research:** "fit factor this" shows Company fit, then Role fit, with every claim tagged Verified, Estimated, or Inferred.
- **Intake and the Sheet template:** the first release.
