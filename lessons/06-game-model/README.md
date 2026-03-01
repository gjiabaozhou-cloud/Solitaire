````markdown
# Lesson 06 — Game Model Basics

- **Subject:** Pure game model: represent tableau, stock, waste, foundations; functions to `setup_game` and simple moves.
- **Core concepts:** state as an immutable data structure (tuples/lists), function composition, small unit tests.
- **How to explain to kids:** The model is a snapshot of the board — we write functions that take a snapshot and create a new snapshot after a move. Compare to taking a photo before and after moving a card.
- **Activities:** Run `demo_game.py` to see setup; try writing or modifying a `move_waste_to_tableau(state)` function.
- **Checks:** Unit-check: after `setup_game(deck)`, are there 7 tableau piles with expected lengths? Run the lesson demo/test and inspect printed state.

```bash
cd lessons/06-game-model
python3 test_game_model.py
```

- **Estimated time:** 60 minutes.

Exercises:
- Implement move legality checks and a `is_won` function.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for data-structure mapping (tableau = list-of-lists) and where to introduce algorithmic checks.

````
# Lesson 06 — Functional Game Model

Goal: Implement the Solitaire game model as pure functions operating on immutable data structures.

Files:
- `game_model.py` — starter model: initialize piles and simple move functions.
- `test_game_model.py` — small tests for model behavior.

How to run tests:

```bash
cd lessons/06-game-model
python3 test_game_model.py
```

Exercises:
- Implement move legality checks and a `is_won` function.
