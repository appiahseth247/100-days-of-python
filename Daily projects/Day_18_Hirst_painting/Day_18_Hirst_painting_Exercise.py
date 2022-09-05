"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 18 - Hirst Painting                                                                               *
*    Subject:  Turtle Graphics. Tuples and Importing Modules                                                *
*    Date: 2022-04-15                                                                                       *
*************************************************************************************************************
"""

import turtle
from turtle import Turtle, Screen, pendown, penup

screen = Screen()

tim = Turtle()
# screen.register_shape("turtle.gif")  # to register my own turtle image
# tim.shape("turtle.gif")
tim.shape("turtle")
turtle.colormode(255)

# Exercise 18.2 -  Draw dashed Lines
for i in range(20):
    tim.pendown()
    tim.fd(10)
    tim.penup()
    tim.fd(10)

screen.exitonclick()
