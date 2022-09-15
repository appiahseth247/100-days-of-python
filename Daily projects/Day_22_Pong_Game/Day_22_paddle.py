from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
PADDLES_POSITION = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, position):  # must provide the position to create the paddle when calling this class
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30  # Get the ycor() and increase it by 20 in order to go up
        self.goto(self.xcor(), new_y)  # Remember the method .xcor() returns the x coordinate of an object

    def go_down(self):
        new_y = self.ycor() - 30  # And to go down, reduce the y cor and go there.
        self.goto(self.xcor(), new_y)
