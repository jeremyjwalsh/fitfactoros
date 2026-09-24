# Profile tab map

The Profile tab has one answer per row in column B. Row 2 (Gmail address) is filled in during setup, so Intake's answer block always starts at **B3** and must contain exactly **17 lines, in this order**.

| Line | Cell | Field | Filled from |
|---|---|---|---|
| 1 | B3 | Your name | Resume, or Turn 4 if no resume |
| 2 | B4 | Resume file | Resume (file name) |
| 3 | B5 | Most recent role | Resume, or Turn 4 if no resume |
| 4 | B6 | Years of experience | Resume ("About N (estimate)" unless confirmed), or Turn 4 if no resume |
| 5 | B7 | Top skills | Resume, or Turn 4 if no resume |
| 6 | B8 | Target roles | Q2 (Turn 2), or Turn 4 if no resume |
| 7 | B9 | Where you can work | Q3 (Turn 2) plus cities from Turn 4 |
| 8 | B10 | Pay floor | Turn 4 |
| 9 | B11 | Deal-breakers | Q5 (Turn 2) plus any added in Turn 4 |
| 10 | B12 | Companies to avoid | Turn 4 |
| 11 | B13 | Work that makes you lose track of time | Q6 (Turn 3) |
| 12 | B14 | Dream companies | Turn 4 |
| 13 | B15 | People you know (and where) | Turn 4 |
| 14 | B16 | State | Turn 4 |
| 15 | B17 | Collecting unemployment? | Q8 (Turn 3) |
| 16 | B18 | Wins with numbers | Q9 (Turn 3), or Turn 4 |
| 17 | B19 | Profile last updated | Today's date, YYYY-MM-DD |

## Formatting rules for the block
- One line per field. Never let an answer wrap onto a second line; separate list items with "; ".
- A skipped question is the single word `skipped`. Never leave a line out, or every answer below it shifts.
- No line may start with `=`, `+`, `-`, `@`, or `"`. Google Sheets reads the first four as formulas, and a leading quote can make Sheets merge lines. Start with a word instead (for example, "About $95,000").
- No tab characters.

## Single-field updates
When the user asks to change one answer, output just that answer and the cell to paste it into (for example, "Paste this into B10"). Also give an updated line for B19.
