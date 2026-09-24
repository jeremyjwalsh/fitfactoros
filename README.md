# FitFactorOS

**A job search system for people who are tired of applying into the void.**

FitFactorOS helps you go after fewer jobs that fit you well, get a real person on your side before you apply, and see your progress at every step. It runs on one Google Sheet and a set of AI agents that read, research, and draft for you. **You send everything yourself.** The agents never send, submit, or post.

It is free, open source, and built for people who don't think of themselves as technical. If you can use a spreadsheet and a chat window, you can use this.

> **Status:** Early build. Phase 1 (Sheet template + Intake agent) is built and being tested. See [Roadmap](#roadmap).

---

## Why this exists

### The fear: the black hole and the doom loop

Most job seekers know the feeling: you apply, and nothing happens. No reply, no rejection, no signal. Just the black hole.

Greenhouse CEO Daniel Chait has named what's happening on both sides of that hole. Job seekers use AI to apply to more and more roles. Recruiters, buried under the volume, use AI to filter them out. Applicants who get filtered out respond by applying to even more jobs. He calls it the **"AI doom loop"** ([Fortune, Nov 2025](https://fortune.com/2025/11/18/hiring-job-seekers-recruiters-talent-acquisition-ai-doom-loop-application-technology/); [Fortune, Jul 2026](https://fortune.com/2026/07/27/greenhouse-ceo-daniel-chait-ai-doom-loop-job-seekers-spam-interview-applications-unemployment/)). Greenhouse reports that applications per recruiter on its platform have risen 412% ([Fortune, Jul 2026](https://fortune.com/2026/07/27/greenhouse-ceo-daniel-chait-ai-doom-loop-job-seekers-spam-interview-applications-unemployment/)). Nobody is winning.

Tools that help you apply to more jobs, faster, make this worse. FitFactorOS goes the other way.

### The research: why the grind wears people down

A job search is mostly effort you can't see paying off. Researchers who tracked unemployed job seekers every day for three weeks found that people's mood and confidence swung with how much progress they *felt* they'd made that day, and that a low-progress day was followed by *more* effort the next day ([Wanberg, Zhu & Van Hooft, 2010](#the-science-behind-it)). In today's market, "more effort" often means more applications, which feeds the loop.

Other research explains why visible progress matters so much: people work harder as a goal gets closer, and a head start makes people more likely to finish. Putting feelings into words also takes some of the sting out of them. Details and sources are in [The science behind it](#the-science-behind-it).

### The proof that precision works

Greenhouse offers a "My Dream Job" feature that lets a candidate flag one role per month as their top pick. **Greenhouse reports** that these intentional applicants are hired at roughly **5x the rate** of other applicants ([Fortune, Jul 2026](https://fortune.com/2026/07/27/greenhouse-ceo-daniel-chait-ai-doom-loop-job-seekers-spam-interview-applications-unemployment/)). Intent is a signal employers can trust. Volume isn't.

### The solution

FitFactorOS is built on three moves:

1. **Fewer, better-fit roles.** Every job is researched and scored against *your* criteria before you spend time on it.
2. **A human attached before you apply.** For every role you pursue, the system helps you find the best path to a real person, starting with people you already know.
3. **Every step visible.** Each opportunity gets its own short ladder. You always know what you've done and what the next step is.

---

## Principles

These are the rules every part of FitFactorOS follows. If a feature breaks one, the feature is wrong.

- **Precision over volume.** A few well-researched, well-connected applications beat a hundred cold ones.
- **Humans send everything.** Agents read, research, and draft. They never send an email, submit an application, or post anything. You do.
- **Every claim is tagged.** Anything an agent tells you about a company, role, or person is labeled:
  - **Verified**: confirmed from a primary source (the job posting, the company's site, a filing, your own records), with a link and the date checked.
  - **Estimated**: a number or range worked out from comparable data (for example, a pay band from similar postings), with the method stated.
  - **Inferred**: a judgment drawn from the evidence, with the reasoning stated. Never presented as fact.
- **Warm path first.** Before you apply, find the warmest route to a person. When you can, reach out first and apply 2–3 days later, so your contact has a chance to flag you before your application lands in the pile.
- **Keep it simple.** Built for non-technical people. Questions come as tappable choices where possible, and every question can be skipped.
- **Only real progress counts.** Every rung on your ladder is something you actually did or something that actually happened. No fake rungs, no points for opening the app.
- **Light by design.** Claude plans have usage limits. FitFactorOS spends your usage only where it changes a decision: a quick screen first, deep research only on jobs you choose to pursue, and never researching the same thing twice.
- **Your data stays yours.** Your information lives in your own Google Sheet. This repository contains no personal data; it ships with a fictional sample profile.

---

## How it works

### The hub: one Google Sheet

Everything lives in one Google Sheet with five tabs. Every row that belongs to a specific opportunity carries the same **Job ID**, so the tabs join together.

| Tab | What it holds |
|---|---|
| **Profile** | Your answers from Intake: target roles, where you can work, pay floor, deal-breakers, dream companies, people you know. |
| **Jobs** | One row per opportunity: company, role, fit score, warm path, ladder stage, next step. |
| **Evidence** | Every research claim, tagged Verified / Estimated / Inferred, with source link and date. |
| **Interviews** | Each conversation: who, when, what was asked, what you learned. |
| **Activity** | A dated log of every job-search action, formatted for your state's unemployment requirements if you need that. |

Emails you send and receive are linked from the sheet with `=HYPERLINK(...)` formulas that include `authuser=<your email>`, so clicking a link opens the right inbox even if you're signed into more than one Google account. The sheet becomes your audit trail.

### The agents

| Agent | What it does | What it never does |
|---|---|---|
| **Intake** | Asks 9 short questions to build your Profile. Every question is skippable. | Guess answers you didn't give. |
| **Job Finder** | Finds roles that match your Profile and your deal-breakers. | Apply to anything. |
| **Research** | Scores each role and company, runs a diligence checklist, and tags every claim. | Present an inference as a fact. |
| **Outreach** | Finds your warmest path to a person and drafts a short note. | Send the note. |
| **Activity Log** | Logs your real activity and formats it for your state's weekly work-search certification. | Submit anything to a state portal, or give legal advice. |

#### The Intake questions

1. Upload your resume.
2. What roles are you targeting?
3. Where can you work? (remote, hybrid, which cities)
4. What's the lowest pay you'd accept?
5. Deal-breakers, and any companies to avoid?
6. What kind of work makes you lose track of time?
7. Dream companies, and people you know at companies you like?
8. What state are you in, and are you collecting unemployment?
   *Your answer only powers the Activity Log, and it stays in your own Sheet.*
9. *(Optional)* Two or three wins from your career, with numbers.

#### The warm-path ladder

For each role, Outreach looks for the warmest route, in this order:

1. **You know someone there.**
2. **You know someone who knows someone there.**
3. **You share a background** with someone there (former employer, school, community).
4. **A direct, researched note** to the right person.
5. **Cold application**, only when nothing above is available.

Every outreach draft follows the **two-fact rule**: it includes two specific, checkable facts that show you did your homework and explain why you're writing to *this* person about *this* role.

### The dashboard and the ladders

The dashboard shows your top opportunities, why each one scored the way it did, what's known about it (with tags), and who to write to.

Each opportunity also gets its own **ladder**: a short, visible sequence of real steps. Warm paths have fewer rungs because a person is already in the loop.

```
Warm path                          Cold path
─────────                          ─────────
Offer                              Offer
Interviewing                       Interviewing
Heard back                         Heard back
Applied (with referral)            Applied
Reached out to your contact        Sent a researched note
Picked                             Found the right person
                                   Researched
                                   Picked
```

"Heard back" counts whether the answer is yes or no. A closed loop is real progress; the black hole is the thing we're fighting.

FitFactorOS tracks **your own** warm-path vs cold-path results over time and shows them back to you, instead of quoting someone else's statistics. After a few weeks you'll see what works for you.

---

## Getting started

**What you'll need:** a Claude account (plan details in the [setup guide](docs/setup.md)), a Google account, and about 20 minutes.

1. Create or sign in to your Claude account.
2. Copy the Sheet template into your Google Drive.
3. Add the FitFactorOS skills to Claude and connect Google Drive and Gmail.
4. Start a new chat and say **"Start my intake."**

The [setup guide](docs/setup.md) walks through every step. Screenshots are coming after the first round of testing.

---

## Repository layout

This is the planned layout. Files arrive as each phase ships.

```
fitfactoros/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── dist/
│   └── fitfactoros-intake.zip   # Ready-to-upload Intake skill
├── docs/
│   ├── setup.md              # Step-by-step setup for non-technical users
│   ├── sheet-schema.md       # Every tab and column, Job ID joins, HYPERLINK pattern
│   ├── claim-tags.md         # Verified / Estimated / Inferred, with examples
│   ├── science.md            # Longer version of "The science behind it"
│   └── roadmap.md
├── sheet/
│   └── fitfactoros-template.xlsx   # Import into Google Sheets
├── agents/
│   ├── shared/
│   │   └── guardrails.md     # Rules every agent loads: humans send, tag claims, no fake rungs
│   ├── intake/
│   ├── job-finder/
│   ├── research/             # Scoring rubrics, diligence checklist, output templates
│   ├── outreach/             # Warm-path ladder, two-fact rule, draft templates
│   └── activity-log/
│       └── states/           # One rules file per state (MA first) + template
├── dashboard/
│   └── index.html            # Standalone dashboard with ladder view
└── samples/
    ├── sample-profile.md     # Fictional job seeker
    └── fitfactoros-sample.xlsx
```

Each agent folder contains a `SKILL.md` (the agent's instructions) and a `references/` folder for the rubrics, checklists, and templates it reads.

### State rules for the Activity Log

Each file in `agents/activity-log/states/` records one state's work-search requirements: minimum activities per week, how the benefit week is defined, the state portal, required fields for each activity, how long records must be kept, a link to the official source, and the date the rules were last verified. The agent warns you if a state's rules haven't been checked in over 90 days.

**This is not legal advice.** Unemployment rules change. Always confirm requirements with your state's official unemployment agency.

---

## Roadmap

**V1 (in progress)**

| Phase | What ships | Status |
|---|---|---|
| 0 | README and repo structure | Done |
| 1 | Sheet template + Intake agent | Testing |
| 2 | Research (scoring rubrics, diligence checklist, output templates) | Planned |
| 3 | Job Finder | Planned |
| 4 | Outreach (warm-path ladder, two-fact rule) | Planned |
| 5 | Activity Log (Massachusetts first, then more states) | Planned |
| 6 | Dashboard with per-opportunity ladders and your own warm vs cold results | Planned |

**V2 (future)**

- **Interview Prep**: research on each person you'll meet, voice mock interviews, and a debrief after every round that feeds prep for the next one.
- **Materials**: help tailoring your resume and cover letter to a specific role, reviewing your version rather than replacing it.
- **Follow-up**: reminders and drafts for thank-you notes and check-ins, timed to your ladder.
- **Momentum check-in**: a short weekly check-in that shows your real progress and offers encouragement. It is not therapy; it points to real support when that's what you need.

---

## The science behind it

FitFactorOS is designed around a small set of findings. Here's what each one says and how we use it.

**The job search grind.** Wanberg, Zhu, and Van Hooft followed 233 unemployed job seekers with a daily survey over three weeks. Mood and confidence swung from day to day, and those swings tracked how much progress people felt they'd made. Lower perceived progress on a given day was followed by *more* search effort the next day.
*How we use it:* Visible progress matters, and effort alone isn't the fix. FitFactorOS makes real progress visible and channels extra effort into quality (research, warm paths) rather than more applications.

**Quality, not just quantity.** A large meta-analysis (378 samples, about 166,000 people) found that job-search intensity modestly predicts interviews, offers, and getting hired, but not the *quality* of the job you land. Job-search quality and self-regulation predicted both.
*How we use it:* We're honest that volume isn't useless. FitFactorOS is a bet on quality and fit, because that's what predicts a job worth having.

**The goal-gradient effect.** Kivetz, Urminsky, and Zheng found that people speed up as they get closer to a goal, the way a coffee-card customer buys more often as the free drink gets near.
*How we use it:* Short ladders, one per opportunity, so the next rung is always within reach.

**Endowed progress.** Nunes and Drèze found that people given a head start toward a goal were more likely to complete it and got there faster, even when the total work required was the same.
*How we use it, with a deliberate difference:* The original studies used an artificial head start. FitFactorOS only credits work you've *actually* done, like finishing Intake or already knowing someone at a company. Real head starts, never fake ones.

**Affect labeling.** In a brain-imaging study, Lieberman and colleagues found that labeling the emotion in negative images, compared with processing them in other ways, reduced the response of the amygdala, a brain region involved in emotional reaction. It was a lab study, so applying it to a weekly check-in is our design choice, not a tested result.
*How we use it:* The V2 Momentum check-in invites you to name how the week felt, briefly, alongside what you got done. Encouragement, not therapy.

**Intent beats volume, in the field.** Greenhouse reports that candidates who use its one-per-month "My Dream Job" flag are hired at roughly 5x the rate of other applicants.
*How we use it:* It's the closest real-world evidence that a small number of intentional applications outperforms a large number of automated ones.

### Sources

- Paoli, N. "'Trust is at an all-time low for both job seekers and recruiters': Hiring platform CEO says talent acquisition is in an 'AI doom loop'." *Fortune*, Nov. 18, 2025. <https://fortune.com/2025/11/18/hiring-job-seekers-recruiters-talent-acquisition-ai-doom-loop-application-technology/>
- Royle, O. R. "CEO of the top-rated hiring platform says the job market is so bad that candidates are paying $20 to mass apply and driving bosses crazy with spam." *Fortune*, Jul. 27, 2026. <https://fortune.com/2026/07/27/greenhouse-ceo-daniel-chait-ai-doom-loop-job-seekers-spam-interview-applications-unemployment/>
- Kivetz, R., Urminsky, O., & Zheng, Y. (2006). The goal-gradient hypothesis resurrected: Purchase acceleration, illusionary goal progress, and customer retention. *Journal of Marketing Research, 43*(1), 39–58. <https://doi.org/10.1509/jmkr.43.1.39>
- Lieberman, M. D., Eisenberger, N. I., Crockett, M. J., Tom, S. M., Pfeifer, J. H., & Way, B. M. (2007). Putting feelings into words: Affect labeling disrupts amygdala activity in response to affective stimuli. *Psychological Science, 18*(5), 421–428. <https://doi.org/10.1111/j.1467-9280.2007.01916.x>
- Nunes, J. C., & Drèze, X. (2006). The endowed progress effect: How artificial advancement increases effort. *Journal of Consumer Research, 32*(4), 504–512.
- van Hooft, E. A. J., Kammeyer-Mueller, J. D., Wanberg, C. R., Kanfer, R., & Basbug, G. (2021). Job search and employment success: A quantitative review and future research agenda. *Journal of Applied Psychology, 106*, 674–713. <https://doi.org/10.1037/apl0000675>
- Wanberg, C. R., Zhu, J., & Van Hooft, E. A. J. (2010). The job search grind: Perceived progress, self-reactions, and self-regulation of search effort. *Academy of Management Journal, 53*, 788–807. <https://doi.org/10.5465/AMJ.2010.52814599>

---

## Contributing

Contributions are welcome, especially **state rules files** for the Activity Log. Every state file needs an official source link and a verification date. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

Not technical? You can still help. Share feedback through the [feedback form](https://forms.gle/JAvtLkWR3unQQZQ77). No GitHub account needed.

## License

[MIT](LICENSE)

## About

Built by [Jeremy Walsh](https://github.com/jeremyjwalsh).
