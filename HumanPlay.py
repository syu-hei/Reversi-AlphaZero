# パッケージのインポート
from Game import State
from MonteCarloTreeSearch import pv_mcts_action
from tensorflow.keras.models import load_model
from pathlib import Path
from threading import Thread
import tkinter as tk


model = load_model('./model/best.h5')

# ゲームUIの定義
class GameUI(tk.Frame):
    def __init__(self, master=None, model=None):
        tk.Frame.__init__(self, master)
        self.master.title('リバーシ')

        self.state = State()

        self.next_action = pv_mcts_action(model, 0.0)

        self.c = tk.Canvas(self, width = 400, height = 400, highlightthickness = 0)
        self.c.bind('<Button-1>', self.turn_of_human)
        self.c.pack()

        self.on_draw()


    def turn_of_human(self, event):
        if self.state.is_done():
            self.state = State()
            self.on_draw()
            return

        if not self.state.is_first_player():
            return

        x = int(event.x/50)
        y = int(event.y/50)
        if x < 0 or 7 < x or y < 0 or 7 < y:
            return
        action = x + y * 8

        # 合法手でない時
        legal_actions = self.state.legal_actions()
        if legal_actions == [64]:
            action = 64 # パス
        if action != 64 and not (action in legal_actions):
            return

        self.state = self.state.next(action)
        self.on_draw()

        self.master.after(1, self.turn_of_ai)

    def turn_of_ai(self):
        if self.state.is_done():
            return

        action = self.next_action(self.state)

        self.state = self.state.next(action)
        self.on_draw()


    def draw_piece(self, index, first_player):
        x = (index%8)*50+4
        y = int(index/8)*50+4
        if first_player:
            self.c.create_oval(x, y, x+40, y+40, width = 1.0, outline = '#000000', fill = '#C2272D')
        else:
            self.c.create_oval(x, y, x+40, y+40, width = 1.0, outline = '#000000', fill = '#FFFFFF')


    def on_draw(self):
        self.c.delete('all')
        self.c.create_rectangle(0, 0, 400, 400, width = 1.0, fill = '#C69C6C')
        for i in range(1, 8):
            self.c.create_line(0, i*50, 400, i*50, width = 1.0, fill = '#000000')
            self.c.create_line(i*50, 0, i*50, 400, width = 1.0, fill = '#000000')
        for i in range(64):
            if self.state.pieces[i] == 1:
                self.draw_piece(i, self.state.is_first_player())
            if self.state.enemy_pieces[i] == 1:
                self.draw_piece(i, not self.state.is_first_player())

f = GameUI(model=model)
f.pack()
f.mainloop()
