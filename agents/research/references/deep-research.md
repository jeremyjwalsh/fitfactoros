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
Short and plain, in this order. Tag every claim Verified, Estimated, or Inferred, with the date checked.

1. **Header:** Company, job title, today's date. Then: "Quick read: Company N, Role N, retired."
2. **Recommendation**, in capitals (for example, **PURSUE NOW** or **ASK FIRST: office days?**), with one sentence on why.
3. **Confidence** and **What would change my mind**, one line each.
4. **Scores**, three separate lines, never blended: Company fit N/100, Role fit N/100, Chance High/Medium/Low.
5. **Material gap / blocker:** one line.
6. **Biggest risk** found in the checks, if it's serious.
7. **Company diligence:** one line per check, in the order of the seven checks, each ending with its tag. Name any check that couldn't be done. End with "Research checks: N of 7."
8. **Company fit table:** factor, score, why (a few words), tag.
9. **Role fit table:** factor, score, why (a few words), tag.
10. **Questions to ask:** the 4 questions, grouped by who can answer.

No blended priority score and no resume score. Fit, Chance, and the resume stay separate.

Then ask the same question as the quick read ("Pursue," "Pass"), and after the user answers, give:
1. The **Jobs row** (all 21 fields), using the user's decision for Screen result and Status. Ladder stage is `Researched`. Fit score is the Role fit. Notes: "Company fit N/100. Blocker: [line]. Deep [date]: Chance [High/Medium/Low]; [your recommendation]." If this lead was already recorded, tell the user: *"On the Jobs tab, click this job's cell in column A and paste. It replaces the old row."* Otherwise, paste at the first empty cell in column A.
2. **New Evidence rows** only, up to 12, pasted at the first empty cell in column A of the Evidence tab.
