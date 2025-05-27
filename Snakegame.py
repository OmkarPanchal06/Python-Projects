import tkinter as tk
import random

GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100
SPACE_SIZE = 20
INITIAL_BODY = 3
SNAKE_COLOR = "#4CAF50"
FOOD_COLOR = "#FF5722"
BG_COLOR = "#222222"
TEXT_COLOR = "#ffffff"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Pro Edition")
        self.root.resizable(False, False)
        self.direction = "right"
        self.score = 0

        self.setup_ui()
        self.start_game()

    def setup_ui(self):
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 16), bg=BG_COLOR, fg=TEXT_COLOR)
        self.score_label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, bg=BG_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.canvas.pack()

        self.restart_button = tk.Button(self.root, text="Restart", font=("Arial", 12, "bold"),
                                        bg="#607D8B", fg="white", command=self.restart_game)
        self.restart_button.pack(pady=10)
        self.restart_button.config(state="disabled")

        self.root.bind("<Left>", lambda e: self.change_direction("left"))
        self.root.bind("<Right>", lambda e: self.change_direction("right"))
        self.root.bind("<Up>", lambda e: self.change_direction("up"))
        self.root.bind("<Down>", lambda e: self.change_direction("down"))

    def start_game(self):
        self.snake_coords = [[SPACE_SIZE * i, 0] for i in range(INITIAL_BODY)][::-1]
        self.snake_squares = [self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR) for x, y in self.snake_coords]
        self.spawn_food()
        self.game_loop()

    def game_loop(self):
        if self.check_collision():
            self.end_game()
            return

        x, y = self.snake_coords[0]
        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake_coords.insert(0, [x, y])
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake_squares.insert(0, square)

        if [x, y] == self.food_coords:
            self.canvas.delete("food")
            self.spawn_food()
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.delete(self.snake_squares[-1])
            self.snake_squares.pop()
            self.snake_coords.pop()

        self.after_id = self.root.after(SPEED, self.game_loop)

    def change_direction(self, new_dir):
        opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if new_dir != opposite.get(self.direction):  # prevent reversing into self
            self.direction = new_dir

    def spawn_food(self):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            if [x, y] not in self.snake_coords:
                break
        self.food_coords = [x, y]
        self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

    def check_collision(self):
        x, y = self.snake_coords[0]
        # Wall_collision
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True
        # Self_collision
        return [x, y] in self.snake_coords[1:]

    def end_game(self):
        self.canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, text="GAME OVER", fill="red", font=("Arial", 36, "bold"))
        self.restart_button.config(state="normal")
        self.root.after_cancel(self.after_id)

    def restart_game(self):
        self.canvas.delete("all")
        self.direction = "right"
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.restart_button.config(state="disabled")
        self.start_game()

#Run_Game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
