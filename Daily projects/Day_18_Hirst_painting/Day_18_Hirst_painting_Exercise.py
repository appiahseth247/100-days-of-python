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
from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()
# screen.register_shape("turtle.gif")  # to register my own turtle image
# tim.shape("turtle.gif")
tim.shape("turtle")
turtle.colormode(255)

# Exercise 18.1 - Draw a Square and Dots
for i in range(4):
    tim.forward(100)
    tim.right(90)

# Drawing the dots
tim.fd(100)  # move 100 paces away from the square above
for i in range(10):
    tim.penup()
    tim.fd(50)
    tim.dot(20, "blue")  # dot size and color
tim.fd(100)
screen.exitonclick()
