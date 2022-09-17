from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day_24_high_score_data.txt", mode="r") as highest_score:  # New name of the file
            self.high_score = int(highest_score.read())  # Reading value saved in Day_24_high_score_data.txt
            # (highest_score) and saving it as high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.reset_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        """Updates the scoreboard with the highest score """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day_24_high_score_data.txt", mode="w") as highest_score:  # Write the high score to
                # Day_24_high_score_data.txt
                highest_score.write(f"{self.high_score}")
        self.score = 0  # Have tp reset score back to zero
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # with open("Day_24_high_score_data.txt") as highest_score:
    #     highest_score.write(" you so much.\nI hope you love me ti")
    #
    # with open("Day_24_high_score_data.txt", mode="r") as highest_score:
    #     contents = highest_score.read()
    #     print(contents)
