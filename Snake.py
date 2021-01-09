import turtle
import time
import random

#timer
postpone = 0.1

#score
score = 0
hi_score = 0

#Window Setup
win = turtle.Screen()
win.title('juego de snake')
win.bgcolor('black')
win.setup(600, 600)
win.tracer()

#Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
snake.color('white')

#Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.penup()
food.goto(0, 50)
food.color('green')

#Snake Body
snakeBody = []

#Score 
scoreText = turtle.Turtle()
scoreText.speed(0)
scoreText.color("purple")
scoreText.penup()
scoreText.hideturtle()
scoreText.goto(0,260)
scoreText.write("Score: 0      hi_score: 0", align = "center", font = ("Comic Sans MS", 20, "normal"))

#functions
def up():
    snake.direction="up"
def down():
    snake.direction="down"
def left():
    snake.direction="left"
def right():
    snake.direction="right"

def mov():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y + 20)
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y - 20)
    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x - 20)
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x + 20)

#Keyboard
win.listen()
win.onkey(up, "Up")
win.onkey(down, "Down")
win.onkey(left, "Left")
win.onkey(right, "Right")

while True:
    win.update()

    #colicion bordes

    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        time.sleep(1)
        snake.goto (0,0)
        snake.direction = "stop"

        # Borrar los snakeBody.
        for segmento in snakeBody:
            segmento.hideturtle()
        snakeBody.remove(nuevo_segmento)

        #Limpiar lista de snakeBody
        snakeBody.clear()

        #resetear marcador
        score = 0
        scoreText.clear()
        scoreText.write("Score: {}      hi_score: {}".format(score, hi_score), align = "center", font = ("Comic Sans MS", 24, "normal"))



    #colicion food

    if snake.distance(food) <20:
        #pocicion random
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        #nuevo segmento

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,0)
        nuevo_segmento.direction = 'stop'
        nuevo_segmento.color('cyan')
        snakeBody.append(nuevo_segmento)

        #Aumentar marcador
        score += 10

        if score > hi_score:
            hi_score = score
           
            #colores
            if score >= 0:
                scoreText.color("purple")
            if score >= 50:
                scoreText.color("red")
            if score >= 100:
                scoreText.color("brown")
            if score >= 200:
                scoreText.color("gray")
            if score >= 300:
                scoreText.color("yellow")

        scoreText.clear()
        scoreText.write("Score: {}      hi_score: {}".format(score, hi_score), align = "center", font = ("Comic Sans MS", 24, "normal"))

    #movimiento del cuerpo

    totalSeg = len(snakeBody)
    for index in range(totalSeg -1, 0, -1):
        x = snakeBody[index - 1].xcor()
        y = snakeBody[index - 1].ycor()
        snakeBody[index].goto(x,y)

    if totalSeg > 0:
        x = snake.xcor()
        y = snake.ycor()
        snakeBody[0].goto(x,y)

    mov()

    #colision cuerpo

    for segmento in snakeBody:
        if segmento.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            #borrar snakeBody
            for segmento in snakeBody:
                segmento.hideturtle()
            snakeBody.remove(nuevo_segmento)
            #limpiar snakeBody
            snakeBody.clear()

            #resetear marcador
            score = 0
            scoreText.clear()
            scoreText.write("Score: {}      hi_score: {}".format(score, hi_score), align = "center", font = ("Comic Sans MS", 24, "normal"))



    time.sleep(postpone)