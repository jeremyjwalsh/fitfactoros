# Morning email rules

How to turn the user's Sheet and job alert emails into `data.json`. Read values only. Skip every row whose Job ID contains `EXAMPLE`, any Activity row whose Notes say EXAMPLE, and blank rows. "Today" means today in the user's time zone.

## What to read (one pass)

| Range | What it's for |
|---|---|
| `Profile!A2:B23` | Gmail address (B2), Target roles (B8), Where you can work (B9), Pay floor (B10), Companies to avoid (B12), Work that makes you lose track of time (B13), Collecting unemployment (B17), Wins (B18), Sparks (B20), Sign (B21), Ready by (B22), Dashboard link (B23) |
| `Jobs!A2:U300` | Job ID (A), Company (C), Role (D), Screen result (M), Ladder stage (P), Next step (Q), Next step date (R), Status (S), Fit score (L) |
| `Interviews!A2:K200` | Job ID (A), Date (B), Round (C). Find the company by matching the Job ID in the Jobs tab. |
| `Activity!A2:O500` | Date (A), Activity type (D), Company (E), Result (I) |
| `Dashboard!B7:B9` | Jobs screened this week (B7), Counting activities this week (B8), Weekly minimum (B9) |

If a tab is missing or empty, treat it as no rows. Never stop the email because one part is empty.

## Counts

- **Pursue jobs:** Screen result = Pursue and Status = Active.
- **Due:** Next step date is today or earlier.
- **Needs attention** = Pursue jobs that are Due + Maybe jobs (Status = Active) that are Due.
- **Tiles:** `inFlight` = number of Pursue jobs. `thisWeek` = Dashboard B8 (counting activities only; the tile reads "Activities counted", or "Goal met" once it reaches the weekly minimum). `screened` = Dashboard B7 (jobs screened this week). Never add the two together: screened jobs become Reviewed job posting rows in the Activity tab, so adding them would count the same job twice. `weeklyMin` = Dashboard B9, only if Profile B17 is "Yes"; otherwise leave it out. `needsAttention` as above.
- **Last real step:** the newest Activity row by Date, written "[Activity type] · [Company] · [Mon D]". When the type is Other, use its Result instead of the type, shortened to 60 characters at a word ("Met with the recruiter about pay · Northwind · Oct 15"). If none, leave `lastStep` out.
- **Coming up:** up to 2 things dated 2 to 7 days from today, soonest first: Interviews rows (written "[Company] — [Round] · [Ddd Mon D]"), then Pursue jobs' Next steps ("[Company] — [Next step] · [Ddd Mon D]"). Today and tomorrow are left out; rule 1 of the one move covers them. If none, leave `comingUp` out.

## Search state (first match wins)

| State | When |
|---|---|
| Overwhelmed | Needs attention is 4 or more, or 5 or more Pursue jobs |
| Momentum | A job's Ladder stage is Heard back, Interviewing, or Offer and an Activity row for that company is dated in the last 7 days, or an Interviews row is dated today through 7 days from now |
| Quiet stretch | No Activity row dated in the last 14 days |
| Steady | Anything else |

This is about the workflow. Never write about how the person feels.

## Today's one move (first match wins)

| # | If… | `move.title` | `move.why` |
|---|---|---|---|
| 1 | An Interviews row is dated today or tomorrow | "Prepare for your [Round] with [Company]" | When it is |
| 2 | A Pursue job is Due | Its Next step, with the company named | How overdue, plainly ("Due today," "Due since Oct 12"). If it's more than a day overdue, add: "Already done? Say **log this** and update the Next step in your Jobs tab." |
| 3 | A Maybe job is Due | "Decide on [Company]: pursue, re-park, or pass" | When it was parked |
| 4 | A Pursue job has a Next step and no date | That Next step | "No date set yet" |
| 5 | No Activity row this benefit week | "Log something you already did this week" | "Say **log this** in your FitFactorOS Project." |
| 6 | Otherwise | "Pick one lead and say fit factor this" | Short and encouraging |

Among several matches for the same rule, pick the oldest date, then the higher Fit score. Use the words in the Sheet. Never add a contact name, a deadline, or a task the Sheet doesn't have.

## What deserves attention

Up to 3 items (2 when Overwhelmed), Due items first, oldest date first.
- Pursue: `title` "[Company] — [Next step]", `detail` "Pursue · due [today / Mon D]" or "Pursue · no date set".
- Maybe that's Due: `title` "[Company] — parked, due back", `detail` "Decide: pursue, re-park, or pass".
- Leave out the job that's already today's one move. If nothing is left, use `attentionEmpty`.
- `moveIsDue`: true when the one move is itself a Due item (rule 2 or 3), otherwise false.
- `attentionMore`: Needs attention, minus the items shown, minus 1 if `moveIsDue`. When it's above 0 the section is titled "Top items needing attention" and ends with "Plus N more in your Sheet." The script checks the sum.

## Worth a look (new leads)

Skip the whole section (leave out `leads` and `leadsNote`) when the state is Overwhelmed or Needs attention is 3 or more.

Otherwise, search Gmail read-only:

```
newer_than:1d (from:(jobalerts-noreply@linkedin.com OR jobs-noreply@linkedin.com OR alert@indeed.com OR noreply@glassdoor.com OR ziprecruiter.com) OR subject:("job alert" OR "jobs for you" OR "new jobs"))
```

On Mondays use `newer_than:3d`. Read the subject and snippet only. Open a thread only if the snippet doesn't name a role and company.

For each role found:
1. Drop it if the company is on Companies to avoid (B12), or the company and role are already in the Jobs tab.
2. Quick match against Target roles (B8), Where you can work (B9) and Pay floor (B10, only if the alert shows pay):
   - **Strong:** the title is a target role or a close match, and the location works.
   - **Possible:** one of the two is a stretch.
   - **Long shot:** anything else. Never shown.
3. Keep at most 2, Strong before Possible.

If none are left, set `leadsNote` to "Nothing new worth your time today." and `leads` to an empty list. A quick match is a judgment, never a fact. No web searches.

## Spark

1. Seed: `python3 scripts/build_email.py seed "<B20>" <today>`.
2. Themes: pick up to three from this list: starting, persistence, craft, connection, courage, patience, rest, momentum, focus, curiosity.
   - **From the state:** Momentum → momentum or courage. Quiet stretch → starting, patience or rest. Overwhelmed → focus or rest. Steady → craft, connection or curiosity.
   - **From the sign (Profile B21), if given:** use the table below. The sign only steers the pick. **Never name the sign, never write "as a Capricorn," never mention stars or astrology.**
   - **From the Profile:** building or teaching work → craft; people or customer work → connection; fixing or problem-solving → curiosity or persistence.
3. Quote or Music: `python3 scripts/build_email.py pick quotes|songs "<theme1>,<theme2>,<theme3>" <today>`. Copy the result exactly. Never change a quote's wording or credit.

| Sign | Themes |
|---|---|
| Aries | courage, starting |
| Taurus | patience, persistence |
| Gemini | curiosity, connection |
| Cancer | connection, rest |
| Leo | courage, momentum |
| Virgo | craft, focus |
| Libra | connection, patience |
| Scorpio | focus, persistence |
| Sagittarius | curiosity, momentum |
| Capricorn | persistence, craft |
| Aquarius | curiosity, courage |
| Pisces | rest, curiosity |

These are the traits people commonly link to each sign, used for fun. They're never presented as a prediction or a fact about the person.
4. Write `body` (one or two sentences, 220 characters or fewer). For Quote and Music it appears after **What it means today:**, so it says in plain words what the quote or song means for their real day, tied to the one move or the week. Write it so someone who has never heard of the source gets it without looking anything up. For Humor, also write `headline` (the setup, 60 characters or fewer); the body carries the humor itself, kind and never at anyone's expense. Leave `headline` out for Quote and Music.
   - Keep the mix: well-known and lesser-known sources are both welcome. Discovery is part of the point; the plain-words line is what makes an unfamiliar one land.
5. For Music, add `why`: one short phrase on the feel of the song (for example "Calm, focused, and in no rush"), without naming anything from their Profile.

Spark rules:
- Never explain why something was picked. No "because you love…", no "you told us…".
- Never claim progress the Sheet doesn't show.
- Never name a star sign (even though it may steer the pick), religion, or anything from the guardrails' sensitive list.
- No lyrics, no copied text, no made-up quotes.

## Reading the week honestly

| The Sheet shows | Say it like this |
|---|---|
| At or above the weekly minimum | Notice it plainly. No over-the-top praise. |
| Some activity, under the minimum | "2 of 3 so far." No alarm. |
| No Activity rows this week | Don't assume nothing happened. Invite them to log what they did. |
| Something real moved | Name it. That's the celebration. |
| A job closed as Closed – no this week | Steady and kind. No silver-lining clichés. |
| Not collecting unemployment | No "required," no minimum. |

## Closing line

Pick one, rotating by date (day of month mod 4):
0. One good move beats twenty random applications.
1. Small steps, real progress.
2. Fewer jobs, better fits.
3. You send everything. We just help you see it.

## data.json shape

```json
{
  "date": "YYYY-MM-DD",
  "state": "Momentum | Steady | Quiet stretch | Overwhelmed",
  "spark": {
    "seed": "Quote | Music | Humor",
    "headline": "… (Humor only)",
    "body": "… (shown after 'What it means today:' for Quote and Music)",
    "quote": {"text": "…", "source": "…"},
    "song": {"title": "…", "artist": "…", "why": "…"}
  },
  "move": {"title": "…", "why": "…"},
  "tiles": {"inFlight": 0, "thisWeek": 0, "weeklyMin": 3, "screened": 0, "needsAttention": 0},
  "lastStep": "…",
  "comingUp": ["…"],
  "attention": [{"title": "…", "detail": "…"}],
  "attentionEmpty": "…",
  "moveIsDue": true,
  "attentionMore": 0,
  "leads": [{"role": "…", "co": "…", "loc": "…", "match": "Strong | Possible"}],
  "leadsNote": "…",
  "dashboardUrl": "https://…",
  "closing": "…"
}
```

`dashboardUrl` is Profile B23 if it starts with https://, otherwise the Sheet's own link.
