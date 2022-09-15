import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # self.make_cars()
        # self.move_car()

    def make_cars(self):
        """Creates random cars on the y-axis"""
        chance_number = random.randint(1, 5)  # The higher the stop number(5), slower the rate at which cars are made
        if chance_number == 1:  # A new car is made only the randomly selected number is 1
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_car(self):
        """Moves the cars towards the left"""
        for car in self.all_cars:
            car.backward(self.car_speed)  # Backwards to cause the cars to move to the left on the screen

    def increase_speed(self):
        """Increases the speed of the cars"""
        self.car_speed += MOVE_INCREMENT
