"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 24 -  US States Game                                                                              *
*    Subject:  Intro to CSV and Pandas                                                                      *
*    Date: 2022-05-06                                                                                       *
*************************************************************************************************************
"""

# Day 25 project - US States Learning Game

import turtle
from turtle import Turtle, Screen

import pandas

screen = Screen()
screen.title("U.S. States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)  # This allows for any image of choice in gif format
turtle.shape(image)


# TODO: Get the coordinates of each state on the image
# def get_mouse_on_click_coordinates(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_on_click_coordinates)  # To get coord of a point on the screen
# turtle.mainloop() # to get the screen open until we close it manually unlike exitonclick()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_states = []

score = 0
game_on = True
while game_on:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]  # applying Day 26
        # lesson: List comprehension instead of the 4 lines of code below
        # missed_states = []
        # for t in states_list:
        #     if t not in guessed_states:
        #         missed_states.append(t)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn")
        # TODO: placed the missed_states on the map too
        for state in missed_states:
            m_coordinates = data[data.state == state]
            writer = turtle.Turtle()
            writer.penup()
            writer.hideturtle()
            writer.color("red")
            writer.goto(int(m_coordinates.x), int(m_coordinates.y))
            writer.write(state, move=False, font=("Arial", 10, "normal"))
        break
    for us_state in states_list:
        if us_state == answer:
            states = data[data.state == answer]
            x_cor = int(states.x)
            y_cor = int(states.y)
            writer = Turtle()
            writer.penup()
            writer.hideturtle()
            writer.goto(x_cor, y_cor)
            writer.write(answer, align="left")  # , align="center", font=("Courier", 5, "normal")
            if answer in guessed_states:
                print(f"You have already guessed {answer}")
            else:
                guessed_states.append(answer)
                score += 1
        if len(guessed_states) > 50:
            game_on = False


screen.exitonclick()
