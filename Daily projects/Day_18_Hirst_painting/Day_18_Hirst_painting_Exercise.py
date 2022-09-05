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
turtle.colormode(255)

# Exercise 18.3 - Draw Shapes(polygons)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for n in range(3, 11):
    angle = 360/n
    tim.color(random.choice(colors))
    for i in range(n):
        tim.right(angle)
        tim.fd(100)

screen.exitonclick()
