````markdown
# Lesson 02 — Deck Helpers

- **Subject:** Small pure functions operating on decks (shuffle, draw top, draw many, cut, deal_tableau).
- **Core concepts:** pure functions (input → output), returning new lists vs modifying in place, randomness.
- **How to explain to kids:** "A function is a machine: put a deck in, get a new deck out." Demonstrate both a function that returns a new shuffled deck and a function that removes a card and returns the card + new deck.
- **Activities:** Explore `deck.py`; implement or inspect `shuffle_deck(deck)` and `draw_top(deck)` following examples. Try drawing 5 cards.
- **Checks:** After calling `shuffle_deck`, is original deck unchanged (demonstrate by printing pre/post)? Does `draw_top` return `(card, new_deck)` and reduce deck length by 1? Run tests:

```bash
python3 test_deck.py
```

- **Estimated time:** 30–45 minutes.

Exercises:
- Implement `shuffle_deck` with a seed for reproducible shuffles.
- Write a CLI to simulate dealing and drawing.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for where shuffle and draw map to algorithm concepts and reproducible randomness.

````
# Lesson 02 — Deck Helpers

Goal: Add pure helper functions: shuffle, draw, cut, deal.

Files:
- `deck.py` — functional deck with `shuffle_deck`, `draw_top`, `draw_many`, `cut_deck`, `deal_tableau`.
- `test_deck.py` — simple tests to run with `python3 test_deck.py`.

How to run tests:

```bash
python3 test_deck.py
```

Exercises:
- Implement `shuffle_deck` with a seed for reproducible shuffles.
- Write a CLI to simulate dealing and drawing.
