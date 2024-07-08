import turtle
import time
import random

# 設定遊戲畫面
screen = turtle.Screen()
screen.title("貪吃蛇遊戲")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # 停止畫面更新

# 設定蛇
snake = []
for _ in range(3):
    segment = turtle.Turtle("square")
    segment.color("white")
    segment.penup()
    snake.append(segment)

# 設定食物
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 設定蛇的移動方向
direction = "stop"


def move():
    if direction == "up":
        y = snake[0].ycor()
        snake[0].sety(y + 20)
    if direction == "down":
        y = snake[0].ycor()
        snake[0].sety(y - 20)
    if direction == "left":
        x = snake[0].xcor()
        snake[0].setx(x - 20)
    if direction == "right":
        x = snake[0].xcor()
        snake[0].setx(x + 20)


def go_up():
    global direction
    if direction != "down":
        direction = "up"


def go_down():
    global direction
    if direction != "up":
        direction = "down"


def go_left():
    global direction
    if direction != "right":
        direction = "left"


def go_right():
    global direction
    if direction != "left":
        direction = "right"


# 鍵盤控制
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# 遊戲主迴圈
while True:
    screen.update()

    # 移動蛇身
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)
    move()

    # 檢查是否吃到食物
    if snake[0].distance(food) < 20:
        # 移動食物到隨機位置
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # 增加蛇身長度
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        snake.append(new_segment)

    time.sleep(0.1)