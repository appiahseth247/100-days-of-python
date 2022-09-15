from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        # screen.register_shape("turtle.gif")
        # self.shape("turtle.gif")
        self.penup()
        self.color("purple")
        self.goto_starting_position()
        self.seth(90)

    def move_north(self):
        """Moves the player upwards"""
        self.fd(MOVE_DISTANCE)
    
    def goto_starting_position(self):
        """Moves back the player to its original position"""
        self.goto(STARTING_POSITION)
    
