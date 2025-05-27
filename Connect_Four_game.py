import tkinter as tk
from tkinter import messagebox

#Constants
ROWS, COLS = 6, 7
CELL_SIZE = 100
PLAYER_COLORS = {"R": "#e63946", "Y": "#f1c40f", " ": "#1e1e2f"}  # red, yellow, dark background
BG_COLOR = "#1e1e2f"
HIGHLIGHT_COLOR = "#2a2a40"
CLICK_HIGHLIGHT_COLOR = "#393960"
GRID_LINE_COLOR = "#444"

#class
class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("🔴🟡 Connect Four - Modern UI")
        self.root.configure(bg=BG_COLOR)

        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE,
                                bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(pady=(10, 0))

        self.info_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg=BG_COLOR, fg="white")
        self.info_label.pack(pady=5)

        self.restart_button = tk.Button(root, text="🔁 Restart", command=self.restart_game,
                                        bg="#4b4b6e", fg="white", font=("Helvetica", 12), relief="flat", padx=10, pady=5)
        self.restart_button.pack(pady=10)

        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<Motion>", self.handle_hover)
        self.canvas.bind("<Leave>", self.clear_hover)

        self.hover_col = None
        self.init_game()

    def init_game(self):
        self.board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
        self.turn = 0
        self.game_over = False
        self.update_info()
        self.draw_board()

    def update_info(self):
        if self.game_over:
            return
        player = "Red 🔴" if self.turn % 2 == 0 else "Yellow 🟡"
        self.info_label.config(text=f"{player}'s Turn")

    def draw_board(self):
        self.canvas.delete("all")
        # Hover highlight if applicable
        if self.hover_col is not None and not self.game_over:
            x1 = self.hover_col * CELL_SIZE
            x2 = x1 + CELL_SIZE
            self.canvas.create_rectangle(x1, 0, x2, ROWS * CELL_SIZE, fill=HIGHLIGHT_COLOR, stipple='gray25', width=0)

        # Draw cells
        for row in range(ROWS):
            for col in range(COLS):
                self.draw_cell(row, col, self.board[row][col])

    def draw_cell(self, row, col, piece):
        x1 = col * CELL_SIZE + 8
        y1 = row * CELL_SIZE + 8
        x2 = x1 + CELL_SIZE - 16
        y2 = y1 + CELL_SIZE - 16

        self.canvas.create_oval(x1, y1, x2, y2, fill=PLAYER_COLORS[piece], outline=GRID_LINE_COLOR, width=2)

    def handle_click(self, event):
        if self.game_over:
            return

        col = event.x // CELL_SIZE
        row = self.get_next_open_row(col)

        if row is not None:
            # Highlight clicked column before placing
            self.canvas.create_rectangle(col * CELL_SIZE, 0, (col + 1) * CELL_SIZE,
                                         ROWS * CELL_SIZE, fill=CLICK_HIGHLIGHT_COLOR, width=0)
            self.root.update()

            piece = "R" if self.turn % 2 == 0 else "Y"
            self.board[row][col] = piece
            self.draw_board()

            if self.check_win(piece):
                winner = "Red 🔴" if piece == "R" else "Yellow 🟡"
                self.info_label.config(text=f"{winner} Wins!")
                messagebox.showinfo("🎉 Game Over", f"{winner} wins!")
                self.game_over = True
            elif self.is_draw():
                self.info_label.config(text="It's a Draw 🤝")
                messagebox.showinfo("Draw", "It's a draw!")
                self.game_over = True
            else:
                self.turn += 1
                self.update_info()

    def handle_hover(self, event):
        col = event.x // CELL_SIZE
        if 0 <= col < COLS:
            self.hover_col = col
            self.draw_board()

    def clear_hover(self, event):
        self.hover_col = None
        self.draw_board()

    def get_next_open_row(self, col):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == " ":
                return row
        return None

    def check_win(self, piece):
        # Horizontal check
        for row in range(ROWS):
            for col in range(COLS - 3):
                if all(self.board[row][col + i] == piece for i in range(4)):
                    return True

        # Vertical check
        for col in range(COLS):
            for row in range(ROWS - 3):
                if all(self.board[row + i][col] == piece for i in range(4)):
                    return True

        # Diagonal ↘ check
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if all(self.board[row + i][col + i] == piece for i in range(4)):
                    return True

        # Diagonal ↗ check
        for row in range(3, ROWS):
            for col in range(COLS - 3):
                if all(self.board[row - i][col + i] == piece for i in range(4)):
                    return True

        return False

    def is_draw(self):
        return all(self.board[0][col] != " " for col in range(COLS))

    def restart_game(self):
        self.init_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
