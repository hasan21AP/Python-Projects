from turtle import *

window = Screen()
window.bgcolor("black")
window.title("Ping Pong")
window.setup(width=600,height=600)
window.tracer(0)

paddle1 = Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.penup()
paddle1.goto(-250,0)
paddle1.shapesize(stretch_len=1,stretch_wid=5)

paddle2 = Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.penup()
paddle2.goto(250,0)
paddle2.shapesize(stretch_len=1,stretch_wid=5)

ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball_dx = 0.5
ball_dy = 0.5

score1 = 0
score2 = 0

score = Turtle()
score.speed(0)
score.color("white")
score.hideturtle()
score.penup()
score.goto(0,260)
score.write(f"Player 1: {score1}   Player 2: {score2}",align="center",font=("Courier",25,"normal"))


def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)
    if y >= 250:
        paddle1.sety(250)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)
    if y <= -250:
        paddle1.sety(-250)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)
    if y >= 250:
        paddle2.sety(250)
    elif y <= -250:
        paddle2.sety(-250)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)
    if y <= -250:
        paddle2.sety(-250)



window.listen()
window.onkeypress(paddle1_up,"w")
window.onkeypress(paddle1_down,"s")
window.onkeypress(paddle2_up,"Up")
window.onkeypress(paddle2_down,"Down")




while True:
    window.update()
    
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1
    if ball.xcor() > 290:
        ball.goto(0,0)
        ball_dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1}   Player 2: {score2}",align="center",font=("Courier",25,"normal"))
    elif ball.xcor() < -290:
        ball.goto(0,0)
        ball_dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1: {score1}   Player 2: {score2}",align="center",font=("Courier",25,"normal"))
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(240)
        ball_dx *= -1
    elif (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-240)
        ball_dx *= -1