````markdown
# Lesson 11 — Full Rules & Auto-move

- **Subject:** Enforce full Klondike rules: multi-card moves, foundation rules, auto-move-to-foundations.
- **Core concepts:** rule-checking functions, multi-card sequences, win detection, test-driven validation.
- **How to explain to kids:** Present the official rule set as a concise list; give examples of legal vs illegal multi-card moves (use colors and ranks). Explain auto-move as "helper" that moves any eligible cards automatically to foundations.
- **Activities:** Run `test_rules.py` and examine `game_model.py`. Create small scenarios where an auto-move should trigger and verify it does.
- **Checks:** Run lesson tests — they should pass. Ask the learner to write a failing test (e.g., try to move an illegal sequence) and then fix the model until tests pass.

```bash
cd lessons/11-rules
python3 test_rules.py
```

- **Estimated time:** 60–120 minutes.

Notes:
- This lesson focuses on the model and correctness; UI integration is left for lesson 12.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) to review how rule-checking functions implement algorithms and how tests verify correctness.

````
# Lesson 11 — Full Rules

Goal: Implement and test full Klondike rules: foundations, legal multi-card moves, and auto-move to foundations.

How to run tests:

```bash
cd lessons/11-rules
python3 test_rules.py
```

Notes:
- This lesson focuses on the model and correctness; UI integration is left for lesson 12.
