import tkinter as tk
from tkinter import font
from deck import generate_deck, shuffle_deck, card_str, draw_top
from typing import List, Tuple

Card = Tuple[str, str]


class DeckViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("52-card Deck")
        self.deck: List[Card] = generate_deck()

        self.header = tk.Label(self, text="52-card Deck", font=(None, 16, 'bold'))
        self.header.pack(pady=6)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=4)

        tk.Button(btn_frame, text="Shuffle", command=self.shuffle).pack(side='left', padx=4)
        tk.Button(btn_frame, text="Reset", command=self.reset).pack(side='left', padx=4)
        tk.Button(btn_frame, text="Deal Top", command=self.deal_top).pack(side='left', padx=4)
        tk.Button(btn_frame, text="Quit", command=self.destroy).pack(side='left', padx=4)

        self.message = tk.Label(self, text="Click a card to inspect it.")
        self.message.pack(pady=4)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)

        self.card_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.card_frame, anchor='nw')

        self.card_font = font.Font(size=12, weight='bold')
        self.draw_cards()

        self.card_frame.bind('<Configure>', self._on_frame_configure)

    def _on_frame_configure(self, event=None):
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def draw_cards(self):
        for widget in self.card_frame.winfo_children():
            widget.destroy()

        cols = 13
        for i, card in enumerate(self.deck):
            r = i // cols
            c = i % cols
            fg = 'red' if card[1] in ('♥','♦') else 'black'
            lbl = tk.Label(self.card_frame, text=card_str(card), relief='raised', bd=2,
                           width=4, height=2, font=self.card_font, fg=fg, bg='white')
            lbl.grid(row=r, column=c, padx=3, pady=3)
            lbl.bind('<Button-1>', lambda e, card=card: self.on_card_click(card))

    def on_card_click(self, card: Card):
        self.message.config(text=f"Selected: {card[0]} of {card[1]}")

    def shuffle(self):
        self.deck = shuffle_deck(self.deck)
        self.draw_cards()

    def reset(self):
        self.deck = generate_deck()
        self.draw_cards()

    def deal_top(self):
        if not self.deck:
            self.message.config(text='Deck is empty')
            return
        top, self.deck = draw_top(self.deck)
        self.message.config(text=f"Dealt: {card_str(top)}")
        self.draw_cards()


def main():
    app = DeckViewer()
    app.geometry('900x300')
    app.mainloop()


if __name__ == '__main__':
    main()
