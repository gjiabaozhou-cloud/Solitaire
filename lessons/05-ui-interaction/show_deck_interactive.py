import tkinter as tk
from tkinter import font
from deck import generate_deck, shuffle_deck, card_str, draw_top, deal_tableau
from typing import List, Tuple

Card = Tuple[str, str]


class InteractiveViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Deck Interactive')
        self.deck: List[Card] = generate_deck()
        self.waste: List[Card] = []
        self.tableau: List[List[Card]] = []
        self.selected = None  # tuple ('waste'|'tableau', card)

        self.header = tk.Label(self, text='Interactive Deck', font=(None, 14, 'bold'))
        self.header.pack(pady=6)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=4)
        tk.Button(btn_frame, text='Shuffle', command=self.shuffle).pack(side='left', padx=4)
        tk.Button(btn_frame, text='Deal', command=self.deal_one).pack(side='left', padx=4)
        tk.Button(btn_frame, text='Reset', command=self.reset).pack(side='left', padx=4)

        self.info = tk.Label(self, text='Click "Deal" to move top card to waste.')
        self.info.pack(pady=4)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)

        self.card_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.card_frame, anchor='nw')

        self.card_font = font.Font(size=12, weight='bold')
        self.setup_tableau()
        self.draw()

    def draw(self):
        for w in self.card_frame.winfo_children():
            w.destroy()

        # stock and waste info
        tk.Label(self.card_frame, text=f'Stock: {len(self.deck)}').grid(row=0, column=0, padx=8)
        tk.Label(self.card_frame, text='Waste:').grid(row=0, column=1, padx=8)

        if self.waste:
            lbl = tk.Label(self.card_frame, text=card_str(self.waste[-1]), relief='raised', bd=2,
                           width=6, height=3, font=self.card_font, bg='white')
            lbl.grid(row=1, column=1, padx=8)
            lbl.bind('<Button-1>', lambda e: self.on_select_waste())

        # tableau display
        for i, pile in enumerate(self.tableau):
            lbl_title = tk.Label(self.card_frame, text=f'Pile {i+1} ({len(pile)})')
            lbl_title.grid(row=2, column=i, padx=6, pady=(12, 0))
            if pile:
                top = pile[-1]
                lbl = tk.Label(self.card_frame, text=card_str(top), relief='groove', bd=2,
                               width=6, height=3, font=self.card_font, bg='white')
            else:
                lbl = tk.Label(self.card_frame, text='(empty)', relief='ridge', bd=2,
                               width=6, height=3, font=self.card_font, bg='lightgray')
            lbl.grid(row=3, column=i, padx=6, pady=6)
            lbl.bind('<Button-1>', lambda e, idx=i: self.on_click_pile(idx))
        self.card_frame.update_idletasks()

    def shuffle(self):
        self.deck = shuffle_deck(self.deck)
        self.draw()

    def reset(self):
        self.deck = generate_deck()
        self.waste = []
        self.setup_tableau()
        self.draw()

    def deal_one(self):
        try:
            top, self.deck = draw_top(self.deck)
        except IndexError:
            self.info.config(text='Stock empty — reset to continue')
            return
        self.waste.append(top)
        self.info.config(text=f'Dealt: {card_str(top)}')
        self.draw()

    def setup_tableau(self):
        # deal a fresh tableau from the deck (non-mutating: create new deck for deal)
        d = shuffle_deck(self.deck)
        piles, remaining = deal_tableau(d)
        self.tableau = piles
        # set deck to remaining so dealing doesn't duplicate
        self.deck = remaining

    # --- movement rules and handlers ---
    def rank_value(self, rank: str) -> int:
        RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return RANKS.index(rank)

    def color_of(self, suit: str) -> str:
        return 'red' if suit in ('♥', '♦') else 'black'

    def can_place_on(self, moving_card, target_card) -> bool:
        # moving_card placed onto target_card: target rank must be one higher and color opposite
        mr, ms = moving_card
        tr, ts = target_card
        try:
            return (self.rank_value(tr) == self.rank_value(mr) + 1) and (self.color_of(ms) != self.color_of(ts))
        except ValueError:
            return False

    def on_select_waste(self):
        if not self.waste:
            return
        self.selected = ('waste', self.waste[-1])
        self.info.config(text=f'Selected waste: {card_str(self.waste[-1])}')

    def on_click_pile(self, idx: int):
        pile = self.tableau[idx]
        if not self.selected:
            # optionally select top of pile
            if pile:
                self.selected = ('tableau', (idx, pile[-1]))
                self.info.config(text=f'Selected pile {idx+1} top: {card_str(pile[-1])}')
            return

        source, payload = self.selected
        if source == 'waste':
            moving = payload
            # attempt move waste -> tableau[idx]
            if not pile:
                # only king can be placed on empty tableau
                if moving[0] == 'K':
                    self.tableau[idx] = pile + [moving]
                    self.waste.pop()
                    self.info.config(text=f'Moved {card_str(moving)} to empty pile {idx+1}')
                else:
                    self.info.config(text='Only King can be placed on empty pile')
            else:
                target = pile[-1]
                if self.can_place_on(moving, target):
                    self.tableau[idx] = pile + [moving]
                    self.waste.pop()
                    self.info.config(text=f'Moved {card_str(moving)} onto pile {idx+1}')
                else:
                    self.info.config(text='Illegal move')
        # clear selection after attempt
        self.selected = None
        self.draw()


def main():
    app = InteractiveViewer()
    app.geometry('400x200')
    app.mainloop()


if __name__ == '__main__':
    main()
