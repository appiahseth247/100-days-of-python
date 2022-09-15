from turtle import Turtle
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.move_speed = 0.9
        self.segments = []
        self.x_cor = 0
        self.y_cor = 0
        self.colors = ["red", "orange", "yellow", "blue", "green", "purple"]
        self.create_snake()
        self.head = self.segments[0]  # the first segment is designated as the head of the snake

    def create_snake(self):
        """ Creates the snake """
        for n in range(3):  # Creates 3 segments for now
            self.create_segment(n)

    def create_segment(self, n):
        """ Creates a new segment to be added to the snake """
        new_segment = Turtle("square")
        new_segment.color(random.choice(self.colors))
        new_segment.penup()
        new_segment.goto(self.x_cor, self.y_cor)
        self.x_cor -= 20  # Reduce the x_cor but maintain the y so all the segments will be on the same horizontal
        # but different vertical axis
        self.segments.append(new_segment)

    def extend_snake(self):
        """ Adds a segment to the snake whenever the snake touches the food."""
        self.create_segment(self.segments[-1].position())  # adds the new segment at the position of the last segment
    #     which is self.segments[-1]. Remember the position() returns the coordinate position of an object
    #     self.color("")
        self.move_speed *= 0.8  # Increase the speed of the snake when the snake extends

    def move(self):
        """ Move all the segments forward """
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start =2(the last segment), stop=0 and step=-1
            new_x = self.segments[seg_num - 1].xcor()  # x-coordinate of segment indexed 1
            new_y = self.segments[seg_num - 1].ycor()  # y-coordinate of segment indexed 1
            self.segments[seg_num].goto(new_x, new_y)  # segment indexed 2 goes to segment indexed 1's position
        self.head.forward(MOVE_DISTANCE)  # And segment indexed 0 (the head) moves forward by some MOVE-DISTANCE

    def up(self):
        """Changes snake direction to UP"""
        if self.head.heading() != DOWN:  # To prevent the snake from moving in direct reverse
            self.head.setheading(UP)

    def down(self):
        """ Changes snake direction to DOWN"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ Changes snake direction to LEFT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ Changes snake direction to RIGHT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
