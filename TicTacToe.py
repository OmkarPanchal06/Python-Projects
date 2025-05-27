import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Pro Edition")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.current_player = "X"
        self.score = {"X": 0, "O": 0}

        self.create_widgets()
        self.reset_board()

    def create_widgets(self):
        self.status_label = tk.Label(self.root, text="Player X's Turn", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.status_label.pack(pady=10)

        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.frame, text="", font=("Arial", 36), width=5, height=2,
                                bg="#ffffff", fg="#333", relief="raised",
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn

        self.score_label = tk.Label(self.root, text="X: 0    O: 0", font=("Arial", 14), bg="#f0f0f0")
        self.score_label.pack(pady=5)

        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Arial", 12, "bold"),
                                        bg="#4CAF50", fg="white", padx=10, pady=5,
                                        command=self.reset_board)
        self.restart_button.pack(pady=10)

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col]["fg"] = "#D32F2F" if self.current_player == "X" else "#1976D2"

            if self.check_winner():
                self.score[self.current_player] += 1
                self.update_score()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        # Check diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def is_draw(self):
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def update_score(self):
        self.score_label.config(text=f"X: {self.score['X']}    O: {self.score['O']}")

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
                self.buttons[row][col]["fg"] = "#333"
        self.current_player = "X"
        self.status_label.config(text="Player X's Turn")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
