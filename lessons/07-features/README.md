````markdown
# Lesson 07 — Features: Undo & Helpers
````markdown
# Lesson 07 — Features: Undo & Helpers

- **Subject:** Undo stack and helper functions for move validation.
- **Core concepts:** storing history (list of past states), reversible operations, pure helpers that check move legality.
- **How to explain to kids:** "Undo" is like a time machine that keeps earlier photos — pressing undo shows the previous photo. Helpers are small rules that answer "is this move allowed?"
- **Activities:** Use `features.py`; implement an undo push/pop when performing moves, and add a small button in the demo to call `undo()`.
- **Checks:** Do repeated moves then press undo; does state revert step-by-step? Confirm by printing stack sizes.

```bash
cd lessons/07-features
python3 test_features.py
```

- **Estimated time:** 30–45 minutes.

Exercises:
- Implement a real hint algorithm that suggests legal moves.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for how history/undo demonstrates stack-like data structures and state snapshots.

````
Files:
