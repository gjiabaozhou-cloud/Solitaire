````markdown
# Teaching Overview — Data Structures, Algorithms, MVC, and OOP

This central guide maps the core CS concepts to the Solitaire lessons and includes diagrams to visualize effects.

1. Data Structures (where to teach):
   - Lists: `deck` (ordered list), tableau piles (list of lists) — lessons 01–03, 06.
   - Tuples/records: `Card` as `(rank, suit)` or `(rank, suit, face_up)` — lessons 01, 09.
   - Stacks/queues: stock (stack from top), waste (push/pop) — lessons 02, 05.

2. Algorithms (where to teach):
   - Shuffle (randomization): `shuffle_deck()` — lesson 02.
   - Deal (iterative distribution): `deal_tableau()` — lessons 03, 06.
   - Move validation: `can_place_on_tableau()` and `can_move_to_foundation()` — lessons 06, 11.

3. MVC Mapping (visual):
   - Model: `game_model.py` functions (pure state transforms) — lessons 06, 11.
   - View: `ui.py`, `show_deck.py`, `ui_drag.py` — lessons 04, 05, 08, 10.
   - Controller: UI event handlers that call model functions and trigger redraws — lessons 05, 08, 10.

4. Intro to OOP (optional lesson add-on):
   - Why OOP? Show how a `Card` class or `Deck` class groups data+methods.
   - Mapping: For learners who later study classes, provide a short example converting `deck.py` pure functions to a small `Deck` class.

5. Visual Diagrams:
   - See `teaching/diagrams/mvc.mmd` (Mermaid) for an MVC flow diagram.

6. Teaching tips:
   - Use analogies: photos for snapshots (state), puppet stage for UI, conveyor for functions.
   - Hands-on: small exercises after each concept; always show before/after state prints.

````

7. Simple, intuitive explanations (quick reference)

- Card data structure (what it is):
   - Representation: a `Card` is a small tuple/record, for example `(rank, suit)` or `(rank, suit, face_up)`.
   - Attributes:
      - `rank`: one of `A,2,3,...,10,J,Q,K` (string or int).
      - `suit`: one of `♠, ♥, ♦, ♣` (string or short code like `'S','H','D','C'`).
      - `face_up` (optional): `True` if the card is visible; `False` if it's face-down.
   - How to use it (examples):
      - Access: `rank = card[0]`, `suit = card[1]` (or use helpers `card_rank(card)`).
      - Create: `('A', 'S')` or `('10', 'H', False)`.
      - Helpful functions to add: `is_red(card)`, `card_str(card)`, `flip(card)` (returns new card with `face_up` toggled).

- Why this is a data structure: A `Card` groups small related pieces of data; a `Deck` is a `list` of `Card`s (ordered). Tableaus are `list` of `list` of `Card`s. These are simple, concrete examples of lists and records.

- MVC explained simply (how to tell model vs view):
   - Model: pure game state and functions that take state -> new state (e.g. `setup_game()`, `move_waste_to_tableau(state)`). No drawing, no UI code.
   - View: code that draws pixels/widgets (e.g., `show_deck.py`, canvas drawing). No rule logic here — just rendering the state.
   - Controller: glue in the UI that responds to input and calls model functions, then tells the view to redraw. Example: button `on_click` handler calls `new_state = draw_from_stock(state)` then `render(new_state)`.

- Controlling card attribute change (practical pattern):
   - Keep card data immutable in model functions (return new card/stack). Example: `flip(card)` returns a new tuple with `face_up=True`.
   - Controller calls model functions to compute new state; view redraws based on returned state. This keeps logic testable and predictable.
   - Small code sketch:

```python
# model helper
def flip(card):
      rank, suit, face_up = card
      return (rank, suit, not face_up)

# controller (pseudocode)
def on_card_click(state, pile_index):
      new_state = flip_top_card_in_pile(state, pile_index)
      ui.render(new_state)
      return new_state
```

8. Diagrams (files):
   - `teaching/diagrams/card_struct.mmd` — simple box showing `rank`, `suit`, `face_up` fields.
   - `teaching/diagrams/mvc_simple.mmd` — minimal MVC flow (View -> Controller -> Model -> View).
   - `teaching/diagrams/card_state_flow.mmd` — small sequence showing `draw` -> `card moves from stock to waste` -> `flip`.

Use these small diagrams during lessons to quickly point at the model vs view and explain where data lives and where logic lives.
