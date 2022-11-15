# imported turtle module
import turtle

wind = turtle.Screen()  # initialize screen
wind.title("Ping Bong By Mahmoud")  # set the title of the window
wind.bgcolor("black")  # set the background color of the window
wind.setup(width=800, height=600)  # set the width and the height of the window
wind.tracer(0)  # stop the window from updating automatically

# hitter1
hitter1 = turtle.Turtle()  # initializes turtle object(shape)
hitter1.speed(0)  # set the speed of the animation
hitter1.shape("square")  # set the shape of the object
hitter1.color("blue")  # set the color of the shape
hitter1.shapesize(stretch_wid=5, stretch_len=1)  # stretches the shape to meet the size
hitter1.penup()  # stop the object from drawing lines
hitter1.goto(-350, 0)  # set the position of the object

# hitter2
hitter2 = turtle.Turtle()
hitter2.speed(0)
hitter2.shape("square")
hitter2.color("red")
hitter2.penup()
hitter2.shapesize(stretch_wid=5, stretch_len=1)
hitter2.goto(350, 0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


# functions
def hitter1_up():
    y = hitter1.ycor()  # get the y coordinate of the hitter1
    y += 30  # set the y to increase be 20
    hitter1.sety(y)  # set the y of the hitter1 to the new y coordinate


def hitter1_down():
    y = hitter1.ycor()
    y -= 30  # set the y to decrease be 20
    hitter1.sety(y)


def hitter2_up():
    y = hitter2.ycor()
    y += 30
    hitter2.sety(y)


def hitter2_down():
    y = hitter2.ycor()
    y -= 30
    hitter2.sety(y)


# keyboard bindings
wind.listen()  # tell the window to expect keyboard input
wind.onkeypress(hitter1_up, "w")  # when pressing w the function hitter1_up is invoked
wind.onkeypress(hitter1_down, "s")

wind.onkeypress(hitter2_up, "Up")
wind.onkeypress(hitter2_down, "Down")
# main game loop
while True:
    wind.update()  # updates the screen everytime the loop run

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # ball starts  at 0 and everytime loops run-->+0.4 x_axis
    ball.sety(ball.ycor() + ball.dy)  # ball starts  at 0 and everytime loops run-->+0.4 y_axis

    # border check ,top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290:  # if ball is at top border
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse direction, make +0.4-->-0.4

    if ball.ycor() < -290:  # if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # if ball is at right border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # if ball is at left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # collision hitter and ball
    if 340 < ball.xcor() < 350 and (hitter2.ycor() + 40 > ball.ycor() > hitter2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if -350 < ball.xcor() < -340 and (hitter1.ycor() + 40 > ball.ycor() > hitter1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1