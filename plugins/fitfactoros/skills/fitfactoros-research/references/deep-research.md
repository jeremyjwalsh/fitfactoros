# Deep research

Only when the user chooses "Go deeper first." Budget: about 8–15 searches and page reads. Tell the user once before starting that it uses more of their Claude plan.

The quick read's scores are **retired**, not averaged. Deep research scores from scratch. Keep the old scores only as a note ("Quick read: Company 62, Role 71, retired").

## The seven checks
Run all seven. Report how many were done: "Research checks: 7 of 7."

1. **Leadership changes, last 18 months.** Build the sequence, not just today's names: who held the senior seats 18 months ago, who holds them now, and who left. Watch for a role that was created and then removed, a title that was lowered, or a wave of exits after a new CEO. Name who left, not only who arrived.
2. **Funding:** every round, with dates, amounts, and who led the latest one. For public companies: the latest results and the trend.
3. **Major news, last 12 months:** launches, layoffs, lawsuits, acquisitions, pivots.
4. **Market position:** analyst reports or rankings if any exist, and how the company describes its category.
5. **Live careers page, read directly.** If it won't load, say "Careers page could not be read; open roles not confirmed." Never swap in a search snippet or job aggregator.
6. **Employee review themes:** Glassdoor, Comparably, Reddit. Themes, not cherry-picked quotes. Note how many reviews there are and how recent they are.
7. **Competitors and category moves:** who they compete with, and who is buying whom.

**If a check can't be done,** don't stop. Name the missing check, lower Confidence one level, and say what would fill the gap.

## Where the facts come from
- **Verified:** a primary source you read (posting, company site, filing, the user's records), with the date checked.
- **Estimated:** worked out from other data, **or reported by a third party** (news, data sites) but not confirmed by the company. Write "reported by [source], not confirmed by the company" in How we know.
- **Inferred:** your judgment from the evidence, with the reasoning.
- **Insiders:** what a person the user talked to says about their own job, team, or manager is Verified (name and date). What they say about company-wide numbers (revenue, runway, retention) is Estimated. If the user said a number and the insider agreed, it's still the user's number.
- If a pay, headcount, revenue, or retention number is too weak to act on, don't print it. Say what the source is, why it's weak, and who can answer.

## Scores (1–10 each; same rules as rubrics.md: 5 is typical, not verified caps at 6)

**Company fit, out of 100:** Product and market ×2, Leadership stability ×2, Money and stability ×2, Customers and momentum ×1.5, Culture (from reviews) ×1.5, Career upside ×1.

**Role fit, out of 100:** Core experience ×3, Work you want ×2.5, Gap risk ×2 (10 = no real gap), Level and scope ×1.5, Pay ×1 (5 if not posted; don't guess).

**Chance of getting it:** High, Medium, or Low. Never a number, never blended into a fit score. Weigh: a warm contact at the company, meeting the hard requirements, location eligibility, level match, how long the posting has been up, and signs of an internal candidate. If something is in progress (a referral sent, an application waiting), write "pending [what]" and don't re-rate until it resolves.

## Recommendation (pick one)
- **Pursue now:** strong fit, workable location, live posting.
- **Ask first:** strong fit with one open question that decides it (office days, pay, level). Name the question.
- **Pass: hard requirement:** the work fits, but a must-have doesn't.
- **Pass: too junior:** they could do it easily, but level or pay is below the line.
- **Watch for a repost:** right role, but closed or in the wrong location.

Then two lines:
- **Confidence:** High, Medium, or Low, about the recommendation. Low if a key claim is Inferred or couldn't be checked.
- **What would change my mind:** one specific, checkable fact that would flip the call. If you can't write one, the recommendation isn't ready.

If two readings fit the same facts, say so, and name the one question that decides between them.

## Questions to ask
Group them by who can answer:
- **Recruiter:** pay range, level, interview steps, timeline, new role or replacement.
- **Hiring manager:** what the first 90 days are for, team size, who sets the direction.
- **Their contact:** what the work is really like, and who really decides.

Keep 4 questions total for a 30-minute call, most important first. Say to ask the most important one early, not at the end.

## Output: the Fit Report
Easy to read first, proof second. Short sections, plain sentences, tables only for scores. Every claim still carries a tag, but keep it light: end the line with **(V)**, **(E)**, or **(I)**. Put the key under the header once: *(V) Verified · (E) Estimated · (I) Inferred, my judgment.* Judgment calls get (I) every time, including the reasons behind a score. The full source and date for each claim go in the Evidence rows, not in the report body.

1. **Header:** Company, job title, today's date, "Using your Intake answers from [date]," and "Quick read: Company N, Role N, retired." Then the tag key. Then "Research checks: N of 7," naming any that came up thin.
2. **Verdict**, in capitals (for example, **PURSUE NOW** or **PASS: HARD REQUIREMENT**), then **one plain sentence** a friend would say (for example, "Good company, wrong seat.").
3. **⚠ The one thing to know:** a single callout for the most important finding, if there is one: a serious risk, a surprise, or a possible path in. Two or three sentences. Leave it out if nothing rises to that level.
4. **The company:** a short paragraph (what it does, size, money, momentum), then the **leadership sequence** in one or two lines (who left, who arrived, which seats are open). One small table for funding rounds only if there's more than one round.
5. **Scores**, one small table: Company fit N/100, Role fit N/100, Chance High/Medium/Low, each with a few words of reading. Never blended, no decimals.
6. **Why these scores:** one line per factor that moved a score away from 5 (score, a few words why, tag). Skip factors that stayed at 5.
7. **Material gap / blocker:** one line.
8. **Confidence** and **What would change my mind:** one line each.
9. **Questions to ask:** the 4 questions, grouped by who can answer.
10. **If you want [Company] anyway:** for a Pass or Ask first only. One or two lines on the next move toward the company, not this job (for example, a different team or role the checks turned up, or the question to ask a contact there). Leave it out if there's no real move.

No blended priority score and no resume score. Fit, Chance, and the resume stay separate.

Then ask the same question as the quick read ("Pursue," "Pass"), and after the user answers, give:
1. The **Jobs row** (all 21 fields), using the user's decision for Screen result and Status. Ladder stage is `Researched`. Fit score is the Role fit. Notes: "Company fit N/100. Blocker: [line]. Deep [date]: Chance [High/Medium/Low]; [your recommendation]." If this lead was already recorded, tell the user: *"On the Jobs tab, click this job's cell in column A and paste. It replaces the old row."* Otherwise, paste at the first empty cell in column A.
2. **New Evidence rows** only, up to 12, pasted at the first empty cell in column A of the Evidence tab.
