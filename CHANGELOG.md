# Changelog

What changed in each FitFactorOS update, newest first. Your Sheet and your Intake answers carry over between updates unless a note here says otherwise.

## 2026-10-15

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
