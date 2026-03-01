````markdown
# Lesson 03 — CLI Deal Demo

- **Subject:** Bringing deck functions together — dealing cards into tableau piles and printing text-based layout.
- **Core concepts:** loops, list-of-lists, formatting output for readability.
- **How to explain to kids:** Like dealing cards into piles on a table; represent each pile as a row of words. Show how functions compose: `deal_tableau(deck)` uses `draw_top` repeatedly.
- **Activities:** Run `deal_demo.py` to see a printed deal; modify print layout or change number of piles.
- **Checks:** Can the student change deal size and observe correct totals (52 cards distributed)? Have them count cards in all piles programmatically.

```bash
python3 deal_demo.py
```

- **Estimated time:** 30 minutes.

Exercises:
- Change the deal to 5 piles instead of 7.
- Show the top (face-up) card for each pile only.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for how the deal algorithm demonstrates iteration and distribution patterns.

````
# Lesson 03 — CLI Deal Demo

Goal: Use the `deal_tableau` helper to print a Klondike-style deal to the terminal.

Files:
- `deal_demo.py` — prints 7 piles and remaining stock.

How to run:

```bash
python3 deal_demo.py
```

Exercises:
- Change the deal to 5 piles instead of 7.
- Show the top (face-up) card for each pile only.
