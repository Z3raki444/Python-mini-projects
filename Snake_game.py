from tkinter import *
import random

# =========================
# Game configuration
# =========================
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 25
INITIAL_SPEED = 120
BODY_PARTS = 3

SNAKE_COLOR = "#00FF00"
HEAD_COLOR = "#7CFC00"
FOOD_COLOR = "#FF4C4C"
BACKGROUND_COLOR = "#000000"
TEXT_COLOR = "#FFFFFF"

# Directions
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Start snake in the center of the board
        start_x = (GAME_WIDTH // 2 // SPACE_SIZE) * SPACE_SIZE
        start_y = (GAME_HEIGHT // 2 // SPACE_SIZE) * SPACE_SIZE

        for i in range(BODY_PARTS):
            self.coordinates.append([start_x, start_y + i * SPACE_SIZE])

        for index, (x, y) in enumerate(self.coordinates):
            color = HEAD_COLOR if index == 0 else SNAKE_COLOR
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=color, outline="black", tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self, snake_coordinates):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

            if [x, y] not in snake_coordinates:
                self.coordinates = [x, y]
                break

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, outline="", tag="food"
        )


def draw_grid():
    for x in range(0, GAME_WIDTH, SPACE_SIZE):
        canvas.create_line(x, 0, x, GAME_HEIGHT, fill="#111111", tag="grid")
    for y in range(0, GAME_HEIGHT, SPACE_SIZE):
        canvas.create_line(0, y, GAME_WIDTH, y, fill="#111111", tag="grid")


def update_score():
    score_label.config(text=f"Score: {score}")


def change_direction(new_direction):
    global direction, paused, game_running

    if not game_running:
        return

    if new_direction == LEFT and direction != RIGHT:
        direction = new_direction
    elif new_direction == RIGHT and direction != LEFT:
        direction = new_direction
    elif new_direction == UP and direction != DOWN:
        direction = new_direction
    elif new_direction == DOWN and direction != UP:
        direction = new_direction


def toggle_pause(event=None):
    global paused
    if not game_running:
        return
    paused = not paused
    if not paused:
        next_turn()


def next_turn():
    global snake, food, score, speed, game_running, paused, after_id

    if not game_running or paused:
        return

    x, y = snake.coordinates[0]

    if direction == UP:
        y -= SPACE_SIZE
    elif direction == DOWN:
        y += SPACE_SIZE
    elif direction == LEFT:
        x -= SPACE_SIZE
    elif direction == RIGHT:
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])

    new_head = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE,
        fill=HEAD_COLOR, outline="black", tag="snake"
    )
    snake.squares.insert(0, new_head)

    # Change previous head to body color
    if len(snake.squares) > 1:
        canvas.itemconfig(snake.squares[1], fill=SNAKE_COLOR)

    # Check if food is eaten
    if [x, y] == food.coordinates:
        score += 1
        update_score()
        canvas.delete("food")
        food = Food(snake.coordinates)

        # Slightly increase speed as score increases
        if speed > 50:
            speed = max(50, speed - 2)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions():
        show_game_over()
    else:
        after_id = window.after(speed, next_turn)


def check_collisions():
    x, y = snake.coordinates[0]

    # Wall collision
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Self collision
    for body_part in snake.coordinates[1:]:
        if [x, y] == body_part:
            return True

    return False


def show_start_screen():
    global game_running, paused
    game_running = False
    paused = False

    canvas.delete(ALL)
    draw_grid()

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 - 60,
        text="SNAKE GAME",
        fill=TEXT_COLOR,
        font=("Consolas", 36, "bold")
    )

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2,
        text="Press ENTER to Start",
        fill="#AAAAAA",
        font=("Consolas", 20)
    )

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 + 40,
        text="Arrow keys = Move | P = Pause | R = Retry",
        fill="#777777",
        font=("Consolas", 14)
    )


def show_game_over():
    global game_running, paused, after_id

    game_running = False
    paused = False

    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None

    retry_button.place(
        x=(GAME_WIDTH // 2) - 70,
        y=(GAME_HEIGHT // 2) + 70,
        width=140,
        height=40
    )

    canvas.create_rectangle(
        80, 220, GAME_WIDTH - 80, GAME_HEIGHT - 180,
        fill="#111111", outline="red", width=2, tag="gameover"
    )

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 - 40,
        text="GAME OVER",
        fill="red",
        font=("Consolas", 40, "bold"),
        tag="gameover"
    )

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 + 10,
        text=f"Final Score: {score}",
        fill=TEXT_COLOR,
        font=("Consolas", 22),
        tag="gameover"
    )

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 + 120,
        text="Press R to Retry",
        fill="#AAAAAA",
        font=("Consolas", 16),
        tag="gameover"
    )


def start_game(event=None):
    reset_game()


def reset_game(event=None):
    global snake, food, direction, score, speed, game_running, paused, after_id

    if after_id is not None:
        try:
            window.after_cancel(after_id)
        except:
            pass
        after_id = None

    canvas.delete(ALL)
    draw_grid()

    retry_button.place_forget()

    score = 0
    speed = INITIAL_SPEED
    direction = RIGHT
    game_running = True
    paused = False

    update_score()

    snake = Snake()
    food = Food(snake.coordinates)

    next_turn()


# =========================
# Main window setup
# =========================
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
speed = INITIAL_SPEED
direction = RIGHT
game_running = False
paused = False
after_id = None

# Top score label
score_label = Label(
    window,
    text="Score: 0",
    font=("Consolas", 24, "bold"),
    bg="black",
    fg="white",
    padx=10,
    pady=5
)
score_label.pack(fill=X)

# Canvas
canvas = Canvas(
    window,
    bg=BACKGROUND_COLOR,
    height=GAME_HEIGHT,
    width=GAME_WIDTH,
    highlightthickness=0
)
canvas.pack()

# Retry button
retry_button = Button(
    window,
    text="Retry",
    font=("Consolas", 14, "bold"),
    command=reset_game,
    bg="#222222",
    fg="white",
    activebackground="#444444",
    activeforeground="white"
)

window.update()

# Center window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Key bindings
window.bind("<Left>", lambda event: change_direction(LEFT))
window.bind("<Right>", lambda event: change_direction(RIGHT))
window.bind("<Up>", lambda event: change_direction(UP))
window.bind("<Down>", lambda event: change_direction(DOWN))
window.bind("<p>", toggle_pause)
window.bind("<P>", toggle_pause)
window.bind("<r>", reset_game)
window.bind("<R>", reset_game)
window.bind("<Return>", start_game)

show_start_screen()

window.mainloop()