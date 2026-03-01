````markdown
# Lesson 09 — Face-down Cards

- **Subject:** Card visibility: `face_up` flag on cards and reveal-on-remove rules.
- **Core concepts:** extended card representation (tuples with flag), conditional rendering, more complex move logic.
- **How to explain to kids:** Some cards are "covered" (face-down) like hidden cards in a real game; when you remove the covering card, the next card flips up. Use a physical demo with a small stack and flip cards.
- **Activities:** Inspect `deck.py` and `game_model.py`. Implement reveal logic so when a card is removed, the top face-down card becomes face-up. Visualize face-down cards as a back image.
- **Checks:** After removing a face-up card, is the next card now face-up? Add unit tests in the lesson to assert reveal behavior.

```bash
cd lessons/09-face-down
python3 test_face_down.py
```

- **Estimated time:** 45–75 minutes.

Exercises:
- Integrate this face-down logic into the UI to show card backs for `face_up=False`.
- Add an action to flip a facedown card manually.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for how the `face_up` flag extends the card tuple and affects rendering logic.

````
# Lesson 09 — Face-down Cards

Goal: Teach face-down/face-up card handling: deal tableau with face-down cards, reveal the top card when the below card is removed.

How it works:
- The model represents cards as `(rank, suit, face_up)` tuples.
- `setup_game()` deals tableau piles with only the top card face-up.
- When a move removes the top card from a pile, the newly exposed card is set to `face_up=True`.

Run the demo:

```bash
cd lessons/09-face-down
python3 test_face_down.py
```

Exercises:
- Integrate this face-down logic into the UI to show card backs for `face_up=False`.
- Add an action to flip a facedown card manually.
