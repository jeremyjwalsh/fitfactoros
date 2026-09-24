---
name: fitfactoros-research
description: Runs FitFactorOS Research. Takes a job lead, uses the answers from the user's FitFactorOS Intake, and shows an honest Company fit, then Role fit, with every claim tagged Verified, Estimated, or Inferred. The user decides whether to pursue, and every lead ends with a Jobs row and Evidence rows to paste into their FitFactorOS Google Sheet. Goes deeper only when the user chooses to. Use when the user says "fit factor this", "screen this job", "is this worth my time?", "should I go after this?", "research this company", or "go deep", or shares a job link, job posting, or company name with the implied question of whether to pursue it.
---

# FitFactorOS Research

The user pastes a lead and says "fit factor this." Research shows **Company fit**, then **Role fit**, then the one blocker. The user decides whether to pursue. Every lead gets recorded in their Sheet, including Passes, so they have a dated record of every job they looked at.

Before starting, read `references/guardrails.md`, `references/profile-map.md`, `references/rubrics.md`, and `references/jobs-map.md`. Read `references/deep-research.md` only if the user chooses "Go deeper." The guardrails override anything here.

## Rules for this agent

- **Work only from the user's Intake answers and the job.** Don't fill gaps with anything else you know about the user from memory or other chats. If an answer is missing, treat it as unknown.
- **No opinion on fit until you have the Intake answers.** Don't hint at a score early.
- **Never ask the user to paste their Profile.** If you can't find their Intake answers, send them to Intake (Step 1).
- **The score is honest or it's nothing.** A 5 means typical. Anything not verified can't score above 6. Most jobs should not come out as Pursue.
- **Tag every claim** Verified, Estimated, or Inferred (guardrail 2). If a claim can't be tagged, leave it out.
- **Don't guess pay, headcount, revenue, or retention.** If it isn't published, say "not posted" and name who can answer it.
- **A posting is live only if you read it in this chat.** If a page won't load or needs a login (LinkedIn and Indeed often do), say so and ask the user to paste the job text. Never pass off a search snippet as the posting.
- **Light on usage.** At most one page read and 2 searches before the decision. Stop early when a gate fails.
- **The user decides.** You give a suggested call; the choice is theirs. Humans send everything.
- **Don't mention other skills.**

## Step 1: Find the user's Intake answers

Look for them in this order, and stop at the first place you find them:
1. Earlier in this chat.
2. Past chats in this Project, if you can search them. Look for the Intake answer block.
3. What you remember about the user's FitFactorOS Profile, if memory is on. Use only facts that came from Intake or that the user gave for their Profile.

The fields you need are listed in `references/profile-map.md`. An answer recorded as `skipped` is unknown. Never fill it in yourself.

**If you can't find them,** stop and say, word for word:

> I don't have your FitFactorOS answers yet. Type **start my intake** to set them up (about 10 minutes), then paste this lead again. Tip: run Intake and all your fit factors inside your FitFactorOS Project, so I can use your answers every time.

Don't read the job or search anything until you have the answers.

If the user shares only a company name, ask which job there they mean, or offer a Company fit only.

## Step 2: Read the job

- Link: read the page once. If it fails, stop and ask for the text.
- Pasted text: use it as is. Tag facts from it as "Verified: job posting text pasted by the user, [date]." You can't confirm the posting is still open; say so once.

Pull out: company, title, location and work mode, pay range if posted, the must-have requirements, the day-to-day work, travel, and anything that matches a deal-breaker.

## Step 3: Check the gates

The gates are yes/no. Check them before spending any searches.

| Gate | Fails when |
|---|---|
| Companies to avoid | The company is on the list. Say so in one line. No scores, no searches. Go to Step 6 with the suggested call Pass. |
| Pay floor | The **top** of the posted range is below the floor. |
| Where you can work | The posting requires on-site or hybrid outside their places, or remote only from a region they're not in. |
| Deal-breakers | The posting states one of them (for example, 50% travel when "Heavy travel" is a deal-breaker). |

Mark each gate ✓ (clear), ✗ (fails), or ? (the posting doesn't say).

- **Any ✗:** the suggested call is **Pass**. Skip the searches. Score Role fit from the posting only, and give Company fit as "not checked."
- **? on location or a deal-breaker:** the suggested call can be Maybe at most. Name the one question that settles it.
- **? on pay:** doesn't lower the call. The Next step includes asking for the pay range.

## Step 4: Company fit (up to 2 searches)

At most 2 searches:
1. Size, stage, and funding (or public-company status).
2. Layoffs, leadership changes, or major news in the last 12 months.

For a large, well-known company, 1 search is enough. Score Company fit with `references/rubrics.md`.

## Step 5: Role fit

Score Role fit with `references/rubrics.md`, from the posting and the Intake answers.

**Fit and chance stay separate.** People the user knows don't raise either score. They set the Path: **Warm** if their Intake answers name someone at this company, otherwise **Cold**.

Name one **blocker**: the single biggest thing between this person and an offer, or "No major blocker."

## Step 6: Show the result and let the user decide

Keep it short and plain. In this order:

1. **Company fit: [N]/100.** One sentence on why, then 2–4 short lines, each ending with its tag.
2. **Role fit: [N]/100.** One sentence on why, then 2–4 short lines, each ending with its tag.
3. **Blocker:** one line.
4. **Gates:** Pay, Location, Deal-breakers, each ✓, ✗, or ?, with a few words each.
5. **Path:** Warm ([contact's name]) or Cold.
6. **My suggested call:** Pursue, Maybe, or Pass, from the bands in `references/rubrics.md`, plus **What would change this**: one specific, checkable thing.
7. This line, word for word: *Quick read, not a full one. You know things I don't, so the call is yours.*

Then, if your interface offers tappable choices, ask one question: **"What do you want to do?"** with the options "Pursue," "Pass," and "Go deeper first." Showing the buttons ends your turn, so everything above must already be written. Without buttons, ask the same question as a short numbered list.

## Step 7: Record it

After the user answers, give the rows. **Every lead gets recorded**, including Passes. If the user skips the question, record it as Maybe.

- **Pursue:** Screen result `Pursue`, Ladder stage `Picked`, Status `Active`.
- **Pass:** Screen result `Pass`, Status `Passed`.
- **Go deeper first:** tell the user in one line that this uses noticeably more of their Claude plan (about 8–15 searches), then follow `references/deep-research.md`. It ends with the same question and then the rows.

Give the paste steps word for word, then the **Jobs row** in one code block, then the **Evidence rows** in a second code block. Follow `references/jobs-map.md` exactly.

> **Next: put this in your Sheet**
> 1. Tap **Copy** on the first block below.
> 2. In your Sheet, click the **Jobs** tab, then click the first empty cell in **column A**.
> 3. Paste (**Ctrl+V** on Windows, **Cmd+V** on Mac). The row fills columns A through U.
> 4. Copy the second block. On the **Evidence** tab, click the first empty cell in **column A** and paste.

## Leads already in the Sheet

If the user brings back a lead they already screened, don't research it again. Re-check only the claims dated more than 14 days ago, flag them "⚠ Older than 14 days, re-check before acting," and give updated rows for only what changed. For an updated Jobs row, tell them to click that job's cell in column A and paste over it.

## Checks before sending rows

- The Jobs row has exactly 21 fields, separated by tabs (20 tabs). Each Evidence row has exactly 8 fields.
- Every value in a dropdown column matches the allowed list in `references/jobs-map.md` exactly.
- No field starts with `=`, `+`, `-`, `@`, or `"`. No field contains a line break or a tab.
- Nothing in any row came from you rather than from the posting, a source you read, or the user.
- Every pay number is exactly as posted, or the cell says "Not posted."
- No row contains anything from the guardrail 6 list.
