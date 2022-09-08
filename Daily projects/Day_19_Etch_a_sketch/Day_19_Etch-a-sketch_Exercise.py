"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 19 - Turtle Racing and Etch-A-Sketch                                                              *
*    Subject:  Turtle Graphics: Event Listeners, State and Multiple Instances                               *
*    Date: 2022-04-15                                                                                       *
*************************************************************************************************************
"""

# Exercise 19.1 - Etch-a-sketch challenge
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=800, height=600)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()  # a function gets triggered when the screen "hears" the keyboard strokes and clicks

screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
