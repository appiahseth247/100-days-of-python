"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 18 - Hirst Painting                                                                               *
*    Subject:  Turtle Graphics. Tuples and Importing Modules                                                *
*    Date: 2022-04-15                                                                                       *
*************************************************************************************************************
"""
import random
import turtle
from turtle import Turtle, Screen, pendown, penup

screen = Screen()

tim = Turtle()
# screen.register_shape("turtle.gif")  # to register my own turtle image
# tim.shape("turtle.gif")
tim.shape("turtle")
turtle.colormode(255)  # To use the RGB format of coloring


# Exercise 18.Challenge 5 - Spirograph
def rand_color():  # RGB
    r = random.randint(0, 255)  # The higher the number the deeper the color generated
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)  # A tuple: immutable list
    return random_color


for n in range(72):  # full circle (360) / tilt angle(5) = 72
    tim.speed(0)
    tim.color(rand_color())
    tim.circle(150)  # radius of 50
    tim.lt(5)  # Turn left by 5 degree

screen.exitonclick()
