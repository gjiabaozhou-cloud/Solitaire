````markdown
# Lesson 05 — UI Interaction
````markdown
# Lesson 05 — UI Interaction

- **Subject:** Adding interactivity — click handlers, updating UI from model functions.
- **Core concepts:** mapping UI actions to pure model updates, keeping model & view separate, simple state updates.
- **How to explain to kids:** The model is the "truth" (a set of lists). The UI is a picture of the truth. When you click a button, we ask the model for a new truth and redraw the picture.
- **Activities:** Explore `show_deck_interactive.py`. Implement a button that draws a card to a waste pile and a click that moves waste → tableau.
- **Checks:** After clicking "draw", did the model return a smaller stock and a larger waste? Visual check + print model state to console to verify.

```bash
cd lessons/05-ui-interaction
python3 show_deck_interactive.py
```

- **Estimated time:** 45–75 minutes.

Exercises:
- Modify the UI to flip a dealt card face-up/face-down.
- Add a label showing number of cards remaining in the stock.

**Concept Mapping:** See [teaching overview](../../teaching/overview.md) for how controller events map to model updates and view redraws.

````
Files:
