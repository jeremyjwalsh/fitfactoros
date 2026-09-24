# Profile tab map

The Profile tab has one answer per row in column B. Row 2 (Gmail address) is filled in during setup, so Intake's answer block always starts at **B3** and must contain exactly **17 lines, in this order**.

| Line | Cell | Field | Filled from |
|---|---|---|---|
| 1 | B3 | Your name | Resume, or Turn 4 if no resume |
| 2 | B4 | Resume file | Resume (file name) |
| 3 | B5 | Most recent role | Resume, or Turn 4 if no resume |
| 4 | B6 | Years of experience | Resume ("About N (estimate)" unless confirmed), or Turn 4 if no resume |
| 5 | B7 | Top skills | Resume, or Turn 4 if no resume |
| 6 | B8 | Target roles | Question 2 |
| 7 | B9 | Where you can work | Question 3 |
| 8 | B10 | Pay floor | Question 4 |
| 9 | B11 | Deal-breakers | Question 5 |
| 10 | B12 | Companies to avoid | Question 5 |
| 11 | B13 | Work that makes you lose track of time | Question 6 |
| 12 | B14 | Dream companies | Question 7 |
| 13 | B15 | People you know (and where) | Question 7 |
| 14 | B16 | State | Question 8 |
| 15 | B17 | Collecting unemployment? | Question 8 |
| 16 | B18 | Wins with numbers | Question 9 |
| 17 | B19 | Profile last updated | Today's date, YYYY-MM-DD |

## Formatting rules for the block
- One line per field. Never let an answer wrap onto a second line; separate list items with "; ".
- A skipped question is the single word `skipped`. Never leave a line out, or every answer below it shifts.
- No line may start with `=`, `+`, `-`, `@`, or `"`. Google Sheets reads the first four as formulas, and a leading quote can make Sheets merge lines. Start with a word instead (for example, "About $95,000").
- No tab characters.

## Single-field updates
When the user asks to change one answer, output just that answer and the cell to paste it into (for example, "Paste this into B10"). Also give an updated line for B19.
