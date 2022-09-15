from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.update_score()

    def update_scoreboard(self):
        """ Writes the current score on the screen"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Writes GAME OVER at the center of the screen"""
        self.goto(0, 0)
        self.write("GAME OVER.\nThis game was made by Seth teacher\nThank for playing!", align="center", font=FONT)

    def update_score(self):
        """ Increases scores by 1 whenever the snake touches the food"""
        self.clear()
        self.update_scoreboard()
        self.score += 1
