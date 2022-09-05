"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 18 - Hirst Painting                                                                               *
*    Subject:  Turtle Graphics. Tuples and Importing Modules                                                *
*    Date: 2022-04-15                                                                                       *
*************************************************************************************************************
"""

# Day 18 project - Hirst Dot Painting

# import colorgram  # Use to extract the colors from the image downloaded
#
# rgb_colors = []
# colors = colorgram.extract('Day_18_Hirst_Painting_image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)  # .rgb gives the rgb format of the colors extracted
#     r = color.rgb.r  # This .r will give the red value of the colors extracted in the rgb format
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_tuple = (r, g, b)
#     rgb_colors.append(colors_tuple)
# print(rgb_colors)

# The first two color tuples in the list below was deleted because the were just background white colors
# when calculated at https://www.w3schools.com/colors/colors_rgb.asp

import turtle
from turtle import Turtle, Screen
import random


def move_right():
    """ Turns the turtle right and upwards"""
    tim.right(90)
    tim.fd(50)
    tim.right(90)
    tim.fd(50)


def move_left():
    """ Turns the turtle left and upwards"""
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(50)


def draw_dot():
    """ Draws dots"""
    tim.penup()
    tim.dot(20, random.choice(color_list))
    tim.fd(50)


turtle.colormode(255)
tim = Turtle()
# tim.shape("turtle")
tim.hideturtle()
tim.speed(0)
tim.seth(230)
tim.penup()
tim.fd(290)
tim.seth(0)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
              # obtained from the color extraction above

for i in range(5):  # Going forward and backward 5 times
    for n in range(10):  # draw 10 dots each time
        draw_dot()
    move_left()
    for n in range(10):
        draw_dot()
    move_right()

screen = Screen()
screen.exitonclick()
