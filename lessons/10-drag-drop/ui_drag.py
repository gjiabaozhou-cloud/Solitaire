import tkinter as tk
from tkinter import font
from game_model import setup_game, move_tableau_to_tableau
from deck import card_str
from typing import Tuple


def suit_color(suit: str) -> str:
    return 'red' if suit in ('♥', '♦') else 'black'


class DragUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Drag & Drop Demo')
        self.state = setup_game()
        self.selected = None  # (src_idx, depth)

        btn = tk.Button(self, text='Restart', command=self.restart)
        btn.pack(pady=6)

        self.area = tk.Frame(self)
        self.area.pack(padx=8, pady=8)
        self.card_font = font.Font(size=11, weight='bold')
        # capture releases anywhere so drop works when mouse moves
        self.bind('<ButtonRelease-1>', self.on_global_release)
        # track motion to move transient drag visual
        self.bind('<B1-Motion>', self.on_motion)
        self.drag_widget = None
        self.draw()

    def restart(self):
        self.state = setup_game()
        self.selected = None
        self.draw()

    def draw(self):
        for w in self.area.winfo_children():
            w.destroy()

        # title row
        for col in range(7):
            pile = self.state['tableau'][col]
            title = tk.Label(self.area, text=f'Pile {col+1}\n({len(pile)})')
            title.grid(row=0, column=col, padx=6)

        # cards as grid so layout matches other lessons
        for col in range(7):
            pile = self.state['tableau'][col]
            # if user is dragging from this column, hide the moving stack
            hide_from_depth = None
            if self.selected and self.selected[0] == col:
                hide_from_depth = self.selected[1]

            if not pile:
                empty = tk.Label(self.area, text='(empty)', width=8, height=3, bd=1, relief='ridge')
                empty.grid(row=1, column=col, padx=6, pady=8)
                empty.bind('<Button-1>', lambda e, c=col: self.on_press(e, c, 0))
            else:
                for depth, card in enumerate(pile):
                    # skip drawing cards that are part of the moving stack
                    if hide_from_depth is not None and depth >= hide_from_depth:
                        continue
                    lbl = tk.Label(self.area, text=card_str(card), fg=suit_color(card[1]), bd=1, relief='raised', width=8)
                    lbl.grid(row=1+depth, column=col, padx=6, pady=2)
                    lbl.bind('<Button-1>', lambda e, c=col, d=depth: self.on_press(e, c, d))

    def on_press(self, event, col: int, depth: int):
        # select stack starting at depth
        self.selected = (col, depth)
        try:
            event.widget.config(relief='sunken')
        except Exception:
            pass
        print(f"pressed: src={col}, depth={depth}")
        # create transient drag visual representing the moving stack
        src_pile = self.state['tableau'][col]
        moving_stack = src_pile[depth:]
        if moving_stack:
            top = moving_stack[0]
            text = card_str(top)
            if len(moving_stack) > 1:
                text = f"{text} (+{len(moving_stack)-1})"
            if self.drag_widget:
                try:
                    self.drag_widget.destroy()
                except Exception:
                    pass
            self.drag_widget = tk.Label(self, text=text, fg=suit_color(top[1]), bd=2, relief='raised')
            x = event.x_root - self.winfo_rootx()
            y = event.y_root - self.winfo_rooty()
            self.drag_widget.place(x=x, y=y)
            # redraw to hide original moving stack
            self.draw()

    def on_release(self, event, dst_col: int):
        if not self.selected:
            return
        src_col, depth = self.selected
        print(f"release over col={dst_col} (src={src_col}, depth={depth})")
        if src_col == dst_col:
            self.selected = None
            # remove drag visual if present
            if self.drag_widget:
                try:
                    self.drag_widget.destroy()
                except Exception:
                    pass
                self.drag_widget = None
            self.draw()
            return
        # attempt move
        new_state = move_tableau_to_tableau(self.state, src_col, depth, dst_col)
        if new_state == self.state:
            print("move not allowed")
            # snap back: remove transient visual
            if self.drag_widget:
                try:
                    self.drag_widget.destroy()
                except Exception:
                    pass
                self.drag_widget = None
        else:
            print(f"moved from {src_col} to {dst_col}")
            self.state = new_state
            # remove transient visual
            if self.drag_widget:
                try:
                    self.drag_widget.destroy()
                except Exception:
                    pass
                self.drag_widget = None
        self.selected = None
        self.draw()

    def on_global_release(self, event):
        # Determine which pile/frame the pointer is over when mouse released
        if not self.selected:
            return
        # If the transient drag widget is under the pointer, temporarily hide
        # it so we can detect the underlying pile/frame.
        tmp_pos = None
        widget = self.winfo_containing(event.x_root, event.y_root)
        if widget is self.drag_widget:
            try:
                tmp_pos = (self.drag_widget.winfo_x(), self.drag_widget.winfo_y())
                self.drag_widget.place_forget()
                widget = self.winfo_containing(event.x_root, event.y_root)
            except Exception:
                widget = None
        if widget is None:
            self.selected = None
            self.draw()
            return
        # climb to the child of self.area (pile frame)
        frame = widget
        while frame and getattr(frame, 'master', None) is not self.area:
            frame = getattr(frame, 'master', None)
        if not frame:
            # restore drag visual if we hid it
            if tmp_pos and self.drag_widget:
                try:
                    self.drag_widget.place(x=tmp_pos[0], y=tmp_pos[1])
                except Exception:
                    pass
            self.selected = None
            self.draw()
            return
        info = frame.grid_info()
        col = info.get('column') if info else None
        if col is None:
            if tmp_pos and self.drag_widget:
                try:
                    self.drag_widget.place(x=tmp_pos[0], y=tmp_pos[1])
                except Exception:
                    pass
            self.selected = None
            self.draw()
            return
        # call existing release handler
        # restore drag visual position briefly so on_release can destroy it
        if tmp_pos and self.drag_widget:
            try:
                self.drag_widget.place(x=tmp_pos[0], y=tmp_pos[1])
            except Exception:
                pass
        self.on_release(event, col)

    def on_motion(self, event):
        # update transient drag visual position
        if not self.drag_widget:
            return
        try:
            x = event.x_root - self.winfo_rootx()
            y = event.y_root - self.winfo_rooty()
            self.drag_widget.place(x=x, y=y)
            try:
                self.drag_widget.lift()
            except Exception:
                pass
        except Exception:
            pass


def main():
    app = DragUI()
    app.geometry('900x300')
    app.mainloop()


if __name__ == '__main__':
    main()
