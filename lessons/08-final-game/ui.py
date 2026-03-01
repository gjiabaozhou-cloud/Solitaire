import tkinter as tk
from tkinter import font, messagebox
from game_model import setup_game, deal_from_stock, move_waste_to_tableau, move_waste_to_foundation, move_tableau_to_tableau, move_tableau_to_foundation, is_won
from deck import card_str


class FinalUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Klondike — Final (Simple)')
        self.state = setup_game()
        self.undo_stack = []
        self.selected = None  # ('waste') or ('tableau', idx, depth)

        top = tk.Frame(self)
        top.pack(pady=6)
        btn_frame = tk.Frame(top)
        btn_frame.pack()
        tk.Button(btn_frame, text='Deal', command=self.deal).pack(side='left', padx=4)
        tk.Button(btn_frame, text='Undo', command=self.undo).pack(side='left', padx=4)
        tk.Button(btn_frame, text='Restart', command=self.restart).pack(side='left', padx=4)

        self.canvas = tk.Frame(self)
        self.canvas.pack(padx=8, pady=8)

        self.card_font = font.Font(size=10, weight='bold')
        self.draw()

    def push_undo(self):
        # shallow copy is fine for this simple model
        self.undo_stack.append({
            'tableau': [p[:] for p in self.state['tableau']],
            'foundations': {k: v[:] for k, v in self.state['foundations'].items()},
            'stock': self.state['stock'][:],
            'waste': self.state['waste'][:]
        })

    def undo(self):
        if not self.undo_stack:
            return
        self.state = self.undo_stack.pop()
        self.draw()

    def restart(self):
        self.state = setup_game()
        self.undo_stack = []
        self.selected = None
        self.draw()

    def deal(self):
        self.push_undo()
        self.state = deal_from_stock(self.state)
        self.draw()

    def on_select_waste(self):
        if not self.state['waste']:
            return
        self.selected = ('waste',)
        self.draw()

    def on_select_tableau(self, idx, depth):
        self.selected = ('tableau', idx, depth)
        self.draw()

    def attempt_move_to_tableau(self, dst_idx):
        if not self.selected:
            return
        if self.selected[0] == 'waste':
            self.push_undo()
            self.state = move_waste_to_tableau(self.state, dst_idx)
        elif self.selected[0] == 'tableau':
            _, src_idx, depth = self.selected
            self.push_undo()
            self.state = move_tableau_to_tableau(self.state, src_idx, depth, dst_idx)
        self.selected = None
        self.draw()

    def attempt_move_to_foundation_from_waste(self):
        if not self.state['waste']:
            return
        self.push_undo()
        self.state = move_waste_to_foundation(self.state)
        self.selected = None
        self.draw()

    def attempt_move_tableau_to_foundation(self, idx):
        self.push_undo()
        self.state = move_tableau_to_foundation(self.state, idx)
        self.selected = None
        self.draw()

    def draw(self):
        for w in self.canvas.winfo_children():
            w.destroy()

        # stock
        stock_lbl = tk.Label(self.canvas, text=f'Stock: {len(self.state["stock"])}', width=12)
        stock_lbl.grid(row=0, column=0, padx=6)
        # waste
        waste_text = card_str(self.state['waste'][-1]) if self.state['waste'] else '(empty)'
        waste_lbl = tk.Label(self.canvas, text=waste_text, relief='raised', width=8)
        waste_lbl.grid(row=0, column=1, padx=6)
        waste_lbl.bind('<Button-1>', lambda e: self.on_select_waste())

        # foundations
        for i, s in enumerate(['♠','♥','♦','♣']):
            f = self.state['foundations'][s]
            text = card_str(f[-1]) if f else s
            lbl = tk.Label(self.canvas, text=text, relief='groove', width=6)
            lbl.grid(row=0, column=3+i, padx=6)

        # tableau
        for col in range(7):
            pile = self.state['tableau'][col]
            for row, card in enumerate(pile):
                lbl = tk.Label(self.canvas, text=card_str(card), relief='ridge', width=8)
                lbl.grid(row=1+row, column=col, padx=4, pady=2)
                depth = row
                lbl.bind('<Button-1>', lambda e, c=col, d=depth: self.on_select_tableau(c, d))

        # highlight selection
        if self.selected:
            sel_lbl = tk.Label(self.canvas, text=f'Selected: {self.selected}', fg='blue')
            sel_lbl.grid(row=10, column=0, columnspan=3, pady=8)

        # win check
        if is_won(self.state):
            messagebox.showinfo('You win!', 'Congratulations, all foundations complete!')


def main():
    app = FinalUI()
    app.geometry('920x480')
    app.mainloop()


if __name__ == '__main__':
    main()
