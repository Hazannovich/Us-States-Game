from turtle import Turtle

FONT = ('Arial', 20, 'bold')

END_FONT = ('Arial', 50, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(-200, 220)
        self.write(f"Score: {self.score}", True, "Left", FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(-200, 220)
        self.write(f"Score: {self.score}", True, "Left", FONT)

    def congrats(self):
        self.clear()
        self.goto(-150, 0)
        self.write("You Caught Them All!", True, "Left", END_FONT)

    def game_over(self):
        self.clear()
        self.goto(-150, 0)
        self.write(f"Game Over!\nEnd Score: {self.score}", True, "Left", END_FONT)