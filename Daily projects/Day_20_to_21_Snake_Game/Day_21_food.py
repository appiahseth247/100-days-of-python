from turtle import Turtle
import random


class Food(Turtle):  # inheriting from the Turtle() class
    def __init__(self):
        super().__init__()  # initializing all the attributes and methods associated with the supper class (Turtle)
        self.shape("turtle")
        self.penup()
        # self.shapesize(stretch_len=2, stretch_wid=2)  # Reduced the original size by half
        self.color("pink")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """ Moves the food to a new random location """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
