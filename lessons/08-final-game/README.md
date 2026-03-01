````markdown
# Lesson 08 — Final Game Scaffold (playable basics + undo)

- **Subject:** Combine model + UI to play a simple Klondike-like game with undo.
- **Core concepts:** integrating model and view, event-driven updates, simple win condition detection.
- **How to explain to kids:** You now have all parts: the deck machine, the rules, and the picture stage. Press buttons to play; the program enforces rules.
- **Activities:** Run `ui.py`; play a few moves; intentionally try illegal moves to see rule enforcement. Add a "restart" button and connect to `setup_game`.
- **Checks:** Can a student reach a game-over (win) condition? Are illegal moves blocked with a message? Add small test: try moving a card illegally programmatically and assert model unchanged.

```bash
cd lessons/08-final-game
python3 ui.py
```

- **Estimated time:** 60–90 minutes.

Notes:
- All tableau cards are shown face-up for simplicity (can be extended to face-down logic).
- Supports: stock->waste (Deal), waste->tableau, tableau->tableau (multi-card), tableau/waste->foundation, undo, restart.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for how the full game ties model/view/controller and where to highlight algorithms and data structures.

````
 # Lesson 08 — Final Game (Simple Klondike)

Goal: A minimal, playable Klondike Solitaire demonstrating the full flow: deal, moves, foundations, undo, and restart. The implementation is intentionally simple and easy to extend.

How to run:

```bash
cd lessons/08-final-game
python3 ui.py
```

Notes:
- All tableau cards are shown face-up for simplicity (can be extended to face-down logic).
- Supports: stock->waste (Deal), waste->tableau, tableau->tableau (multi-card), tableau/waste->foundation, undo, restart.
- Designed to be easy to extend with animations, face-down cards, scoring, and hints.
