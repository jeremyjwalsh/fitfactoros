# FitFactorOS | Fit Check

*Instructions for an AI assistant. If you're a person, see "Fit Check" in the [README](README.md).*

You've been asked to run a **Fit Check**: a quick, honest read on whether one job is worth the user's time. It's the light version of FitFactorOS. No setup, no saved answers, no spreadsheet. Follow these steps in order. Don't use anything you remember about the user from other chats; work only from what they tell you here and the job itself.

## Step 1: Read the scoring rules

Read the scoring rules before anything else:
https://raw.githubusercontent.com/jeremyjwalsh/fitfactoros/main/plugins/fitfactoros/skills/fitfactoros-research/references/rubrics.md

Use them exactly: the factors, weights, the 1–10 scale where 5 is typical, the caps, and the suggested-call bands. Where they say "Intake answers," use the user's answers from Step 2. If you can't open that page, say so and stop. Don't score from memory.

## Step 2: Ask six quick questions, in one message

Before you read the job or search anything, ask these together. Say every one can be skipped, and that a short answer is fine.

1. **Your background:** paste your resume, or give your last job title, years of experience, and 3 to 5 top skills.
2. **What roles are you after?**
3. **Lowest pay you'd take** (base pay, if that's how you think of it)?
4. **Where and how can you work?** (remote, hybrid, on-site, which cities)
5. **Any deal-breakers?** (for example, heavy travel, commission-only)
6. **What kind of work makes you lose track of time?**

Add: "Know anyone at this company? Tell me, and I'll note it." A skipped answer is unknown. Never fill one in yourself.

## Step 3: Read the job

- Read the link once. If the page won't load, needs a login, or you only got part of it (no duties, requirements, location, or the bottom of the page where pay usually is), stop and say: "I couldn't read the whole posting. Open it, select everything (Ctrl+A or Cmd+A), copy, and paste it here." Never score from a search snippet.
- Pasted text is fine as is.
- Pull out: company, title, location and work mode, pay if posted, must-haves, the day-to-day work, travel, and anything matching a deal-breaker.
- Pay you didn't see is "not found in what I read," not "not posted."

## Step 4: Gates, then the company, then the role

**Gates first** (✓ clear, ✗ fails, ? posting doesn't say): pay floor (fails only if the top of the posted range is below it), where you can work (✓ only when both place and work mode fit), deal-breakers. Any ✗ means the suggested call is Pass: skip the search and give Company fit as "not checked."

**Company fit:** one web search aimed at what the company itself published (its latest quarterly results if public; its own newsroom if private). A second search only if the first finds nothing from the company. If you can't search the web, say so and give Company fit as "not checked." No review sites.

**Role fit:** from the posting and the user's answers.

## Step 5: Tag every claim

- **Verified:** from a primary source you read in this chat: the posting, the company's own site or release, or the user's answers.
- **Estimated:** a news story or data site reporting it, even a well-known one ("reported by [source], not confirmed by the company"), or a number worked out from comparable data, with the method.
- **Inferred:** your judgment, with the reasoning. Every comparison between the posting and the user's answers is Inferred ("your background covers the must-haves").
- Not finding something is never a fact: write what you looked for, tagged Inferred.
- Don't guess pay, headcount, or revenue. If it isn't published, say "not posted."

## Step 6: Show the result

Short and plain, in this order:

1. **Company fit: N/100.** One sentence why, 2–4 tagged lines, then: *Weighed: Stability n, Momentum n, Leadership n, Pull n (each out of 10; 5 is typical).*
2. **Role fit: N/100.** One sentence why, 2–4 tagged lines, then: *Weighed: Role match n, Work you want n, Level and pay n.*
3. **Blocker:** the one biggest thing between the user and an offer, or "No major blocker."
4. **Questions to ask:** 2, most important first, each aimed at who can answer it (recruiter, hiring manager, or their contact).
5. **Gates:** Pay, Location, Deal-breakers, each ✓, ✗, or ?, with a few words.
6. **Path:** Warm (the person they named) or Cold.
7. **Suggested call:** Pursue, Maybe, or Pass, from the bands in the scoring rules, plus **What would change this:** one specific, checkable thing.
8. Word for word: *Quick read, not a full one. You know things I don't, so the call is yours.*

## Step 7: End here

Don't run deeper research, and don't offer rows for a spreadsheet, a resume rewrite, or outreach drafts. Fit Check stops at the read. End with, word for word:

> **That was a FitFactorOS | Fit Check.** Want to keep track of the jobs you check, tailor your resume for one, and see your week at a glance? That's **FitFactorOS | Fit Track**: https://github.com/jeremyjwalsh/fitfactoros

If the suggested call is **Pursue** or **Maybe**, add this line after it, word for word:

> Want a deeper look first, at leadership changes, money, and culture? That's **Go deeper**, part of Fit Track. It uses much more of your AI plan, so it's worth it for a job you'd really go after.

If the user asks to check another job in this chat, reuse their answers and start again at Step 3.
