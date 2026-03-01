````markdown
# Lesson 10 — Drag & Drop UI + Colored Suits

- **Subject:** Simulated drag/drop interactions and adding suit color rendering.
- **Core concepts:** mouse events (press/move/release), mapping UI coordinates to model piles, visual feedback, simple styling.
- **How to explain to kids:** Demonstrate dragging a card with a finger (or mouse). Show suit colors: red for hearts/diamonds, black for spades/clubs. Relate color to quick recognition.
- **Activities:** Run `ui_drag.py`. Try dragging stacks, see highlighted drop targets, and add a small toggle to show/hide suit colors.
- **Checks:** Does dragging a pile update the model correctly? Are drop-target validations enforced (can't drop on invalid pile)? Visual and programmatic checks (console logs) should match.

```bash
cd lessons/10-drag-drop
python3 ui_drag.py
```

- **Estimated time:** 60–120 minutes.

Notes:
- Click and hold a card in the tableau to start a drag; release over a target pile to attempt a move.
- Suits are colored (red for ♥ ♦, black for ♠ ♣) for clarity.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for mapping of UI events to controller logic and model updates.

````
# Lesson 10 — Drag & Drop

Goal: Implement drag-and-drop interaction for moving stacks between tableau piles.

How to run:

```bash
cd lessons/10-drag-drop
python3 ui_drag.py
```

Notes:
- Click and hold a card in the tableau to start a drag; release over a target pile to attempt a move.
- Suits are colored (red for ♥ ♦, black for ♠ ♣) for clarity.
