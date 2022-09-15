"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 23 - Turtle Car Crossing Game                                                                     *
*    Subject:  Turtle Graphics: Capstone Project                                                            *
*    Date: 2022-04-25                                                                                       *
*************************************************************************************************************
"""
# Day 23 project - Turtle Car Crossing Game
import time
from turtle import Screen
from Day_23_player import Player
from Day_23_car_manager import CarManager
from Day_23_scorebaord import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Welcome To My Car Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_north, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # The code is the while loop is going to be refreshed every 0.1 second
    screen.update()
    car_manager.make_cars()
    car_manager.move_car()

    # Detect player collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # When playing reaches the finishing line
    if player.ycor() >= 280:
        player.goto_starting_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
