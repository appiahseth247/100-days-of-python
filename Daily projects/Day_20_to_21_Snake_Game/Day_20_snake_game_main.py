"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 20 and Day 21 - Snake Game                                                                        *
*    Subject:  Turtle Graphics: Slicing  and class inheritance                                              *
*    Date: 2022-04-19                                                                                       *
*************************************************************************************************************
"""
# Day 20 and Day 21 project - Snake Game

from turtle import Screen  # Turtle
import time

from Day_20_snake import Snake
from Day_21_food import Food
from Day_21_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # .bgcolor is used to change the background
screen.title("Welcome To My Snake Game")
screen.tracer(0)  # Setting the tracer to 0 turns off the screen  and nothing will be seen until it is updated()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()  # This is used to turn on the screen
    time.sleep(snake.move_speed)
    snake.move()

    # Detecting collision with food.
    if snake.head.distance(food) < 15:  # The distance() method returns the distance between two turtles
        # (the snake.head and food in this case)
        food.refresh()
        snake.extend_snake()
        scoreboard.update_score()

    # Detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        # When any of snake head's coordinates (x or y) is over 380 in either sides, it means it has touched the wall
        game_on = False
        print("You hit the wall")
        scoreboard.game_over()

    # Detecting collision with the snake's tail
    for segment in snake.segments[1:]:  # all segments aside the head indexed 0.
        if snake.head.distance(segment) < 10:
            # there is touch with the tail whenever the distance between the head and any segment is less than 10
            game_on = False
            print("You bite your own tail")
            scoreboard.game_over()

screen.exitonclick()
