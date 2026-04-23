"""
Solitaire Mini — Drag & Drop (fixed2)
-------------------------------------
Robust version that prevents stale UI widgets from showing after a move.

Key fixes:
- Exactly one Button per card name (button_by_name).
- Destroy any Button for a card that is no longer present in piles before placing current cards.
- Use pile center distances to pick drop target (more robust).
- Safety checks when removing/appending slices to avoid UI/data mismatch.

Run: python solitaire-mini-dragdrop_fixed2.py
"""

import tkinter as tk
import random

# ----------------------------
# CONFIG
# ----------------------------
FONT_CARD = ("Consolas", 18, "bold")
WINDOW_W, WINDOW_H = 1100, 650
X0, Y0 = 70, 110            # top-left origin for first pile
PILE_SPACING = 140
FAN_HIDDEN = 12
FAN_VISIBLE = 40
CARD_WIDTH = 6
CARD_HEIGHT = 3

# ----------------------------
# BUILD A FULL DECK (52)
# ----------------------------
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['H','D','S','C']
deck = [s + r for s in suits for r in ranks]
random.shuffle(deck)

root = tk.Tk()
root.title("Solitaire Mini — Drag & Drop (fixed2)")
root.geometry(f"{WINDOW_W}x{WINDOW_H}")
root.configure(bg="seagreen")

# ----------------------------
# DATA MODEL
# ----------------------------
def deal_piles(deck):
    """Deal 7 piles; last card in each pile is face-up."""
    piles = []
    idx = 0
    for n in range(1, 8):
        pile = []
        for i in range(n):
            pile.append({"name": deck[idx], "visible": i == n - 1})
            idx += 1
        piles.append(pile)
    return piles, deck[idx:]

piles, rest = deal_piles(deck.copy())

# Exactly one Button per card name
button_by_name = {}  # name -> tk.Button

# Keep controls so we don't accidentally destroy them in cleanup
controls = []

# ----------------------------
# UTIL: color
# ----------------------------
def card_color(name, visible):
    if not visible:
        return ("white", "gray25")
    if name[0] in ("H", "D"):
        return ("red", "mistyrose")
    return ("black", "white")

# ----------------------------
# REDRAW (safe, destroys stale buttons)
# ----------------------------
def redraw():
    """
    1) Collect current card names in the piles.
    2) Destroy any Buttons in button_by_name that are not in current cards (stale widgets).
    3) Ensure Buttons exist for current cards (one per name), update text/colors, and place them.
    4) Bind dragging only to first visible card in each pile (start of the visible tail).
    """
    # 1) current card names set
    current_names = set()
    for pile in piles:
        for c in pile:
            current_names.add(c["name"])

    # 2) destroy stale buttons (those that exist but are not in current_names)
    for name in list(button_by_name.keys()):
        if name not in current_names:
            try:
                button_by_name[name].destroy()
            except Exception:
                pass
            del button_by_name[name]

    # 3) create/update/place buttons for current cards
    for pile_idx, pile in enumerate(piles):
        # find first visible in pile (start of visible tail) or None
        first_visible = None
        for i, c in enumerate(pile):
            if c["visible"]:
                first_visible = i
                break

        for pos, card in enumerate(pile):
            name = card["name"]
            visible = card["visible"]

            # create one Button per card name (if missing)
            if name not in button_by_name:
                btn = tk.Button(root, text="", width=CARD_WIDTH, height=CARD_HEIGHT,
                                font=FONT_CARD, relief="raised", bd=4)
                button_by_name[name] = btn
            btn = button_by_name[name]

            fg, bg = card_color(name, visible)
            btn.config(fg=fg, bg=bg)
            btn.config(text=name if visible else "")

            # compute y with fan logic
            if first_visible is None or pos < first_visible:
                y = Y0 + pos * FAN_HIDDEN
            else:
                y = Y0 + (first_visible * FAN_HIDDEN) + ((pos - first_visible) * FAN_VISIBLE)
            x = X0 + pile_idx * PILE_SPACING
            btn.place(x=x, y=y)
            btn.lift()

            # reset binding & disable; we'll enable the correct one below
            btn.config(state="disabled", cursor="arrow")
            btn.unbind('<Button-1>')
            btn.unbind('<B1-Motion>')
            btn.unbind('<ButtonRelease-1>')

    # 4) bind drag only on the first visible card in each pile
    for pile_idx, pile in enumerate(piles):
        first_visible = None
        for i, c in enumerate(pile):
            if c["visible"]:
                first_visible = i
                break
        if first_visible is not None:
            name = pile[first_visible]["name"]
            btn = button_by_name.get(name)
            if btn:
                btn.config(state="normal", cursor="hand2")
                btn.bind('<Button-1>', lambda e, pi=pile_idx, po=first_visible: start_drag(e, pi, po))
                btn.bind('<B1-Motion>', dragging)
                btn.bind('<ButtonRelease-1>', stop_drag)

    info_label.config(text="Drag the first visible card of a pile to move the visible stack. "
                           "When a face-down card is exposed it flips automatically.")

# ----------------------------
# DRAG & DROP HANDLERS
# ----------------------------
drag_data = {
    "widgets": [],
    "offsets": [],
    "from_pile": None,
    "from_pos": None,
    "cards_moved": []
}

def start_drag(event, pile_idx, card_pos):
    """Gather the visible run starting at card_pos and record widget offsets."""
    pile = piles[pile_idx]
    cards = []
    widgets = []
    offsets = []

    mx0 = event.x_root - root.winfo_rootx()
    my0 = event.y_root - root.winfo_rooty()

    for i in range(card_pos, len(pile)):
        c = pile[i]
        if not c["visible"]:
            break
        cards.append(c)
        btn = button_by_name[c["name"]]
        widgets.append(btn)
        bx, by = btn.winfo_x(), btn.winfo_y()
        offsets.append((bx - mx0, by - my0))

    drag_data["widgets"] = widgets
    drag_data["offsets"] = offsets
    drag_data["from_pile"] = pile_idx
    drag_data["from_pos"] = card_pos
    drag_data["cards_moved"] = cards
    for w in widgets:
        w.lift()

def dragging(event):
    """Move dragged widgets with the mouse."""
    if not drag_data["widgets"]:
        return
    mx = event.x_root - root.winfo_rootx()
    my = event.y_root - root.winfo_rooty()
    for idx, w in enumerate(drag_data["widgets"]):
        ox, oy = drag_data["offsets"][idx]
        w.place(x=mx + ox, y=my + oy)

def stop_drag(event):
    """On drop: find nearest pile center and move the cards in the model, then redraw."""
    if not drag_data["widgets"]:
        return

    mx = event.x_root - root.winfo_rootx()
    # compute nearest pile by comparing distance to each pile's center (robust)
    centers = [X0 + i * PILE_SPACING for i in range(7)]
    dmin = None
    pile_guess = None
    for i, cx in enumerate(centers):
        dist = abs(mx - cx)
        if dmin is None or dist < dmin:
            dmin = dist
            pile_guess = i

    from_pile = drag_data["from_pile"]
    from_pos = drag_data["from_pos"]
    cards_moved = drag_data["cards_moved"]

    # safety checks
    if from_pile is None or from_pos is None or not cards_moved:
        drag_data_update_clear()
        redraw()
        return

    if pile_guess == from_pile:
        # no model change, just snap back visually
        drag_data_update_clear()
        redraw()
        return

    # verify the model slice matches the cards_moved
    count = len(cards_moved)
    slice_names = [c["name"] for c in piles[from_pile][from_pos:from_pos+count]]
    moved_names = [c["name"] for c in cards_moved]
    if slice_names != moved_names:
        # something changed while dragging; abort and redraw to restore UI
        drag_data_update_clear()
        redraw()
        return

    # remove and append
    moved_slice = piles[from_pile][from_pos:from_pos+count]
    del piles[from_pile][from_pos:from_pos+count]
    piles[pile_guess].extend(moved_slice)

    # flip the card that is now exposed (the card immediately before from_pos)
    below_index = from_pos - 1
    if below_index >= 0 and below_index < len(piles[from_pile]):
        below_card = piles[from_pile][below_index]
        if not below_card["visible"]:
            below_card["visible"] = True

    drag_data_update_clear()
    redraw()

def drag_data_update_clear():
    drag_data["widgets"] = []
    drag_data["offsets"] = []
    drag_data["from_pile"] = None
    drag_data["from_pos"] = None
    drag_data["cards_moved"] = []

# ----------------------------
# CONTROLS
# ----------------------------
def reset_game():
    global piles, rest, button_by_name
    d = [s + r for s in suits for r in ranks]
    random.shuffle(d)
    piles, rest = deal_piles(d)
    # destroy any old Buttons to start clean: helps avoid leftover widgets between runs
    for b in list(button_by_name.values()):
        try:
            b.destroy()
        except Exception:
            pass
    button_by_name.clear()
    redraw()

info_label = tk.Label(root, text="", font=("Arial", 13), fg="white", bg="seagreen", justify="left")
info_label.place(x=70, y=20)
controls.append(info_label)

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 11), command=reset_game, bg="gold", fg="black")
reset_btn.place(x=900, y=20)
controls.append(reset_btn)

todo_label = tk.Label(root, text="""
TO DO for full Solitaire:
- Enforce legal moves (alternate colors, descending ranks; King on empty)
- Add foundation piles + draw/waste
- Win detection / animations
""", font=("Consolas", 10), bg="seagreen", fg="yellow", justify="left")
todo_label.place(x=900, y=60)
controls.append(todo_label)

redraw()
root.mainloop()
