# Data map: Sheet → dashboard

Read with the Google Sheets connector, values only. Skip every row whose Job ID contains `EXAMPLE` and any Activity row whose Notes say EXAMPLE. Skip blank rows.

## Top level

| Key | From |
|---|---|
| `sheet` | The Sheet's title |
| `readAt` | Today, YYYY-MM-DD |
| `weeklyMin` | Dashboard tab, cell B9 (the yellow cell). Leave out if blank. |
| `jobs` | One per Jobs row (below) |
| `activities` | One per Activity row (below) |

## `jobs[]` (Jobs tab)

| Key | Column | Notes |
|---|---|---|
| `id` | A Job ID | |
| `date` | B Date added | |
| `co` | C Company | |
| `role` | D Role | |
| `link` | E Job link | Only if it starts with http |
| `loc` | H Location + I Work mode | "Location · Work mode", shortened to the first place if long |
| `pay` | J Pay range + K Pay tag | "range (tag)"; blank if "Not posted" |
| `fit` | L Fit score | Number |
| `call` | M Screen result | Pursue, Maybe, Pass |
| `path` | N Path | Warm or Cold |
| `contact` | O Warm contact | |
| `stage` | P Ladder stage | Copy exactly; blank stays blank |
| `next` | Q Next step | |
| `nextDate` | R Next step date | |
| `cfit` | U Notes | The number after "Company fit" |
| `gap` | U Notes | The text after "Blocker:" up to the next period |
| `ev` | Evidence tab | Rows with this Job ID: `[V/E/I, Claim]`, at most 4, picked in this order: (1) pay, (2) risks (layoffs, cuts, leadership changes, a hard requirement the user lacks), (3) what the role is and why it's open, (4) anything else. Within a group, newest Date checked first; on a tie, the row lower in the Sheet. |
| `log` | Activity tab | The latest Activity row for this company, as "[type] on [date]: [result]" |
| `flag` | your check | Only for a visible problem in the row, such as a date in Next step date that isn't a date. Say what to fix in plain words. |

## `activities[]` (Activity tab)

| Key | Column |
|---|---|
| `date` | A Date |
| `type` | D Activity type |
| `co` | E Company / organization |
| `result` | I Result |
| `counts` | J Counts for unemployment |
