"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 19 - Turtle Racing and Etch-A-Sketch                                                              *
*    Subject:  Turtle Graphics: Event Listeners, State and Multiple Instances                               *
*    Date: 2022-04-15                                                                                       *
*************************************************************************************************************
"""
# Day 19 project - Turtle racing
from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
tim.hideturtle()

screen = Screen()
screen.setup(width=650, height=400)


race_on = False
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Choose from:  {colors}")
position = 0
x_cor = -300
y_cor = -100

contestants = []
for position in range(0, len(colors)):  # Creating as many instances as there are in "colors"
    new_turtle = Turtle(shape="turtle")

    new_turtle.color(colors[position])  # first turtle take color at index 0 and so forth
    position += 1
    new_turtle.penup()
    new_turtle.goto(x=x_cor, y=y_cor)  # move to the starting position
    y_cor += 50  # Increase the y. They start the same vertical (x) but different y
    contestants.append(new_turtle)


if user_bet:  # If user inputs something
    race_on = True

while race_on:
    for contestant in contestants:
        if contestant.xcor() > 280:  # x=230 is the finishing line
            race_on = False
            winning_color = contestant.pencolor()  # get the color of the turtle who exceeds the finishing line first
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost The {winning_color} turtle is the winner")
        random_steps = random.randint(0, 10)  # turtles move forward by randomly selected paces each time
        contestant.forward(random_steps)  # let them move forward randomly paced

screen.exitonclick()
