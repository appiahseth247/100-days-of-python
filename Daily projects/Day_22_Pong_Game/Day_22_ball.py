from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10  # To move the ball by 10 on the x-axis
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball by increasing both the x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)  # Kind of goes upper tight diagonal direction

    def bounce_on_x_axis(self):
        """Reverses the direction of the ball when it hits the upper or bottom wall"""
        self.x_move *= -1  # multiplying by -1 will do the reverse
        self.move_speed *= 0.7  # Increase the speed by 0.7 anytime the ball touches the paddle

    def bounce_on_y_axis(self):
        """ Reverses the direction of the ball when it hits the left or right paddle """
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_on_x_axis()  # This will let the other opponent have a turn if there is a miss
        self.move_speed = 0.1
