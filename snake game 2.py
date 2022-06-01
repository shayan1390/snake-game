from tkinter import *
import random

GAME_WIDTH = 1280
GAME_HEIGHT = 680
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 5
SNAKE_COLOR = ["#fffc9f", "#1e00ff", "#00ffff", "#ff0090"]
FOOD_COLOR = ["#ff0000", "#5cff75", "#5cffff", "#85002f", "#3fccbc", "#8f547e", "#3e7d00", "#ffffff", "#ffa600", "#ffa600"]
BACKGROUND = "#000000"
COLOR_SCORE = ["red", "yellow", "blue", "green", "orange"]
CHENG_COLOR_SCORE = 0
CHENG_COLOR_FOOD = 0


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR[0], tags="snake")
            self.squares.append(square)

class Food:

    def __init__(self):
        global CHENG_COLOR_FOOD

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 11) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 11) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR[CHENG_COLOR_FOOD], tags="food")
        if CHENG_COLOR_FOOD == 9:
            CHENG_COLOR_FOOD = 0
        else:
            CHENG_COLOR_FOOD += 1
def next_turn(snake, food):

    global SNAKE_COLOR

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR[0])
    elif direction == "down":
        y += SPACE_SIZE
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR[1])
    elif direction == "left":
        x -= SPACE_SIZE
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR[2])
    elif direction == "right":
        x += SPACE_SIZE
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR[3])

    snake.coordinates.insert(0, (x, y))

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        global CHENG_COLOR_SCORE
        global SPEED
        global rond

        k = 0
        if score == 9:
            k = score
            score = "!!BOSS!!"
            SPEED -= 20
            k += 1
        elif score == "!!BOSS!!":
            score = k
            rond += 1
            SPEED += 20
        else:
            score += 1
            SPEED -= 1



        label.config(text="Round:{}[Score:{}]".format(rond, score), bg=COLOR_SCORE[CHENG_COLOR_SCORE])
        if CHENG_COLOR_SCORE == 4:
            CHENG_COLOR_SCORE = 0
        else:
            CHENG_COLOR_SCORE += 1
        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:

        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER1")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER2")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER3")
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tags="gameover")



window = Tk()
window.title("Snake game")
window.resizable(False, False)

rond = 0
score = 0

direction = 'down'

label = Label(window, text="Round:{}[Score:{}]".format(rond, score), bg="grey", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()



