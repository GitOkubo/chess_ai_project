import tkinter as tk
from tkinter import messagebox
import chess
import chess.svg

# 駒の表示に使う文字（白は大文字、黒は小文字）
PIECE_SYMBOLS = {
    'P': 'P', 'N': 'N', 'B': 'B', 'R': 'R', 'Q': 'Q', 'K': 'K',
    'p': 'p', 'n': 'n', 'b': 'b', 'r': 'r', 'q': 'q', 'k': 'k',
}

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("チェス盤 GUI")
        self.board = chess.Board()
        self.selected_square = None

        self.square_size = 60
        self.canvas = tk.Canvas(master, width=8*self.square_size, height=8*self.square_size)
        self.canvas.pack()

        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)

        self.save_button = tk.Button(master, text="FEN形式で保存", command=self.save_fen)
        self.save_button.pack(pady=10)

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["#F0D9B5", "#B58863"]
        for rank in range(8):
            for file in range(8):
                x1 = file * self.square_size
                y1 = rank * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                color = colors[(rank + file) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                square_index = chess.square(file, 7 - rank)
                piece = self.board.piece_at(square_index)
                if piece:
                    text = PIECE_SYMBOLS[piece.symbol()]
                    self.canvas.create_text(
                        x1 + self.square_size / 2,
                        y1 + self.square_size / 2,
                        text=text,
                        font=("Consolas", 24)
                    )

    def on_click(self, event):
        file = event.x // self.square_size
        rank = 7 - (event.y // self.square_size)
        square = chess.square(file, rank)

        if self.selected_square is None:
            self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
            else:
                self.board.set_piece_at(square, self.board.piece_at(self.selected_square))
                self.board.remove_piece_at(self.selected_square)
            self.selected_square = None
            self.draw_board()

    def save_fen(self):
        fen = self.board.fen()
        with open("data/saved_position.fen", "w") as f:
            f.write(fen)
        messagebox.showinfo("保存完了", f"現在のFENを保存しました:\n{fen}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()
