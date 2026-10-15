# Changelog

What changed in each FitFactorOS update, newest first. Your Sheet and your Intake answers carry over between updates unless a note here says otherwise.

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
