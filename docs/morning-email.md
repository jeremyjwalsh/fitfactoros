# Morning email: design (Part 18, Phase 2 draft)

Status: design approved Oct 15 (Phase 2). Built in Phase 3.

Checked so far: the layout displays correctly in Gmail on desktop and phone (Verified, Oct 15 test draft).

## What it is

An opt-in email that shows up in your Gmail **Drafts** on weekday mornings. Claude writes it as a draft addressed to you. It never sends anything.

Every morning email answers three questions:

1. **How am I doing?**
2. **What deserves my attention?**
3. **What's the one thing I can do today?**

With a little inspiration and fun along the way. It takes one minute to read.

## Who can use it

| Plan | How it runs |
|---|---|
| Pro, Max, Team, Enterprise | A scheduled task makes the draft every weekday morning, even with your computer asleep. |
| Free | No scheduled tasks. Say **morning email** in your FitFactorOS Project to get the same draft on demand. |

## What it needs

- Gmail connected (to read job alert emails and save the draft)
- Google Sheets connected (to read your FitFactorOS Sheet, read-only)
- Your FitFactorOS Sheet link (saved in the scheduled task, so each run finds it)

## The email, top to bottom

### 1. Spark

A short headline and one or two sentences, written fresh each day by Claude. It's built from:

1. **Today's seed**, one of the kinds the user picked at setup (see "Seeds"). It rotates by date, so it changes without Claude needing to remember yesterday. This is the harmonica principle: surprise someone just enough to change their frame of mind.
2. **Their real week**, read from the Sheet (see "Reading the week honestly").
3. **Who they are**, read from their Profile: their sign (if given), the work that makes them lose track of time, their target roles, their wins. This is what makes it feel picked for them.

Rules:
- Original wording only. No copied text, no song lyrics.
- **Never explains why it was picked.** No "because you said you love training programs." The fit should be felt, not announced. (Think of the first time Spotify played a song you loved without being told.)
- Never claims progress the Sheet doesn't show.
- Never makes someone feel behind on a hard week. Tone follows the rules in "Reading the week honestly."

### 2. Today's one move (the most prominent block)

One action, chosen from real data in this order. The first rule that matches wins:

| Order | If the Sheet shows… | The move |
|---|---|---|
| 1 | An Interviews row dated today or tomorrow | Prepare for it (company, round) |
| 2 | A Pursue job, Status Active, Next step date today or earlier | That Next step |
| 3 | A parked Maybe with Next step date today or earlier | Decide on it: pursue, keep parked with a new date, or pass |
| 4 | A Pursue job with a Next step but no date | That Next step |
| 5 | Nothing logged this week | Log something you already did this week (say **log this**) |
| 6 | Nothing at all | Pick one lead and say **fit factor this** |

The move always names a real company or row. If no rule matches, it uses 5 or 6. It never invents a contact, a deadline, or a task.

### 3. How am I doing (this week)

Three numbers in a row:

| Tile | Where it comes from |
|---|---|
| **In flight** | Jobs tab: Status = Active and Screen result = Pursue |
| **This week** | Dashboard tab B7 + B8, shown against B9 ("2 of 3"). Same numbers the Dashboard shows, so they always agree. |
| **Needs attention** | Parked Maybes due back + Pursue jobs with an overdue Next step date |

Below the tiles, the **last real step**: the newest Activity row (type, company, date).

### 4. What deserves attention

- **In flight:** each Pursue job with its Next step, soonest date first, up to 3.
- **Parked, due back:** Maybes with Next step date today or earlier, up to 3, each with "Decide: pursue, re-park, or pass."

Empty lists say so plainly in one line rather than vanishing.

### 5. Worth a look (new leads, sometimes none)

- Reads the user's own job alert emails from the last day (since Friday on Mondays). **Read-only.** Nothing is labeled, moved, or deleted.
- Skips companies on "Companies to avoid" and anything already in the Jobs tab.
- **At most 2.** Only leads that come out Strong or Possible on the quick match. Long shots are never shown.
- **On many days it shows none.** Then it says: "Nothing new worth your time today."
- **When 3 or more items need attention, this section is skipped.** Clear what's on your plate first.
- Quick match uses target roles, location, and pay floor (only if the alert shows pay). It's a judgment, so it's Inferred, and the section says "Quick matches only. Say **fit factor this** for the full check."
- No web searches. Real research happens only when the user asks.

### 6. Footer

The dashboard button, then one closing line, for example: *One good move beats twenty random applications.*

The button opens the dashboard link saved at setup, or, if there isn't one, the Sheet's Dashboard tab. No images.

## Reading the week honestly

The Sheet only knows what the user recorded. "No rows" doesn't mean "did nothing."

| What the Sheet shows | How the email talks about it |
|---|---|
| Met or beat the weekly minimum | Notice it plainly. No over-the-top praise. |
| Some activity, under the minimum | "2 of 3 so far." No alarm. The one move helps close the gap. |
| Nothing logged this week | Don't assume nothing happened. Invite them to log what they've already done. |
| Something real moved (interview, reply, offer stage) | Name it. That's the celebration. |
| A Closed – no on a job this week | Steady and kind. No silver-lining clichés. |
| Not collecting unemployment (Profile B17) | Show activity count without "required" or the minimum. |

## Search state (workflow, not mood)

Each morning the email puts the search in one of four states, using only what's in the Sheet. These describe the workflow. They never guess how someone feels.

| State | When (checked in this order) | What changes in the email |
|---|---|---|
| **Overwhelmed** | 4 or more items need attention, or 5 or more active Pursue jobs | Shorter. At most 2 items under "What deserves attention." "Worth a look" is skipped. The spark reinforces focus. |
| **Momentum** | A job reached Heard back, Interviewing, or Offer in the last 7 days, or an Interviews row is dated in the next 7 days | The spark names that progress. The one move is the next step on it. |
| **Quiet stretch** | No Ladder stage change and no Activity row in the last 14 days | Gentle. The one move is small and doable. Never says or implies they've failed. |
| **Steady** | Anything else | The standard email. |

## Seeds (spark kinds)

The user picks one or more at setup. **Each morning uses one seed**, rotating by date, so no two mornings in a row feel the same. "Surprise me" rotates through all of them.

The trick is in the matching. Quotes and songs come from short checked lists, and every entry is tagged with themes (starting, persistence, craft, connection, courage, patience, rest, momentum). Each morning Claude picks the entry whose themes best fit **this person today**: their search state plus their Profile. Same list for everyone, different pick for each person.

| Seed | What Claude does |
|---|---|
| **Quote** | Picks from `references/quotes.md`. Every quote's exact wording and source is checked by a person before it goes in the list. A quote that can't be confirmed doesn't go in. Claude never makes up a quote or a credit. |
| **Music** | Picks from `references/songs.md` (title, artist, themes). One line on why it fits today, without naming the reason it was picked. Links to a YouTube search for that song, not a specific video, so the link always works. No lyrics. A choice of Spotify, Apple Music or YouTube can come later. |
| **Humor** | A light, kind line about the search. Never at anyone's expense. |
| **Surprise me** | Rotates through all of the above. |

**The star sign is a silent ingredient.** If the user gives their sign at setup, it quietly steers which themes are picked (a Capricorn leans toward persistence and craft, a Gemini toward curiosity and connection). The email never names the sign, never says "as a Capricorn," and never mentions astrology. The user just gets a quote or song that feels like theirs.

## Setup (opt-in)

The user says **set up my morning email** (Intake mentions it in one line at the end). Three questions, all skippable:

1. Which sparks do you want? (Quote, Music, Humor, Surprise me)
2. What time should it be ready? (default 7:00 am their time)
3. Your star sign, just for fun (never a birthday; it only steers the picks), and your dashboard link if you've made one (otherwise the button opens your Sheet's Dashboard tab)

Answers go into four new Profile rows (B20 to B23). Then the skill creates the scheduled task, or on Free, explains how to ask for it on demand.

## Rules it follows

- Opt-in only. Nothing runs until the user sets it up, and they can stop it any time by turning off the scheduled task.
- Drafts to the user's own address only. Never sends, never drafts to anyone else, never deletes a draft.
- Gmail is read-only apart from that one draft.
- The Sheet is read-only.
- Light on usage: one Sheet read, one Gmail search, one draft. No web searches.
