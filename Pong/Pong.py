import turtle

#Window
win = turtle.Screen()
win.title("Juego de Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
scoreA = 0
scoreB = 0

#First Player
playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("grey")
playerA.penup()
playerA.goto(-350,0)
playerA.shapesize(stretch_wid=5, stretch_len=1)

#Second Player
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("grey")
playerB.penup()
playerB.goto(350, 0)
playerB.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("grey")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.9
ball.dy = 0.9

#Field
field = turtle.Turtle()
field.color("grey")
field.goto(0, 400)
field.goto(0, -400)

#Score Markup
score = turtle.Turtle()
score.speed(0)
score.color("grey")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A = 0        Player B = 0", align="center", font=("Comic Sans MS", 20, "normal"))

#Funcions
def p1_up():
    y=playerA.ycor()
    y +=20
    playerA.sety(y)
def p1_down():
    y=playerA.ycor()
    y -=20
    playerA.sety(y)
def p2_up():
    y=playerB.ycor()
    y +=20
    playerB.sety(y)
def p2_down():
    y=playerB.ycor()
    y -=20
    playerB.sety(y)

win.listen()
win.onkey(p1_up, "w")
win.onkey(p1_down, "s")
win.onkey(p2_up, "Up")
win.onkey(p2_down, "Down")

while True:
    win.update()

    #Edge Collision
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1

    #horizontal edge collision
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        score.clear()
        score.write("Player A = {}        Player B = {}".format(scoreA,scoreB), align="center", font=("Comic Sans MS", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        score.clear()
        score.write("Player A = {}        Player B = {}".format(scoreA,scoreB), align="center", font=("Comic Sans MS", 20, "normal"))

    #range and collision of player navbars
    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < playerB.ycor() + 50
            and ball.ycor() > playerB.ycor() - 50)):
        ball.dx *= -1

    if ((ball.xcor() < -340 and ball.xcor() > -350)
            and (ball.ycor() < playerA.ycor() + 50
            and ball.ycor() > playerA.ycor() - 50)):
        ball.dx *= -1       

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)