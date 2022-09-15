"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 22 - Pong Game                                                                                    *
*    Subject:  Turtle Graphics: Slicing  and class inheritance                                              *
*    Date: 2022-04-23                                                                                       *
*************************************************************************************************************
"""
# Day 22 project - Pong Game
import turtle
from turtle import Screen
from Day_22_paddle import Paddle
from Day_22_ball import Ball
from Day_22_scorebaord import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome To My Pong Game")
screen.tracer(0)  # This turn off the animations during the movement of the paddle to the 350,0 position

# Central dashed line
turtle.pencolor("white")
turtle.hideturtle()
turtle.penup()
turtle.setheading(270)
turtle.backward(300)

for i in range(15):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)

right_paddle = Paddle((350, 0))  # Creates paddle at this location
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)  # Controlling the speed of the ball
    screen.update()  # Turn on the screen as it was turned off by tracer(0) above
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:  # if the ball goes past these values, there's hit the wall hence bounce
        ball.bounce_on_y_axis()

    # Detect collision with paddle
    """ If the distance between the ball and either paddle is less than 63 and the x.cor() of the ball over 330, 
    it means the ball has hit a wall
    """
    # if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
    # ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    if (ball.xcor() == 330 and ball.distance(right_paddle) < 70) or \
            (ball.xcor() == -330 and ball.distance(left_paddle) < 70):
        ball.bounce_on_x_axis()

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_points()

    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_points()

screen.exitonclick()
