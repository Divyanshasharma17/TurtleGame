import turtle
import random
import time

# --- Setup ---
screen = turtle.Screen()
screen.title("Turtle Dodge Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# --- Player ---
player = turtle.Turtle()
player.shape("turtle")
player.color("lime")
player.penup()
player.goto(0, -250)
player.setheading(90)

# --- Score display ---
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)

# --- Enemies ---
enemies = []

def create_enemy():
    e = turtle.Turtle()
    e.shape("square")
    e.color("red")
    e.penup()
    e.goto(random.randint(-270, 270), 300)
    enemies.append(e)

# --- Movement ---
def move_left():
    x = player.xcor()
    if x > -270:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 270:
        player.setx(x + 20)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# --- Game loop ---
score = 0
speed = 4
enemy_spawn_interval = 30
frame = 0
game_over = False

def show_game_over():
    go = turtle.Turtle()
    go.hideturtle()
    go.color("white")
    go.penup()
    go.goto(0, 0)
    go.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
    go.goto(0, -50)
    go.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

while not game_over:
    time.sleep(0.016)  # ~60fps
    screen.update()
    frame += 1
    score += 1

    # Increase difficulty over time
    if score % 300 == 0:
        speed += 0.5
        enemy_spawn_interval = max(10, enemy_spawn_interval - 2)

    # Spawn enemies
    if frame % enemy_spawn_interval == 0:
        create_enemy()

    # Move enemies
    for e in enemies[:]:
        e.sety(e.ycor() - speed)
        # Remove if off screen
        if e.ycor() < -320:
            e.hideturtle()
            enemies.remove(e)
        # Collision check
        if abs(e.xcor() - player.xcor()) < 25 and abs(e.ycor() - player.ycor()) < 25:
            game_over = True

    # Update score
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

show_game_over()
turtle.done()
