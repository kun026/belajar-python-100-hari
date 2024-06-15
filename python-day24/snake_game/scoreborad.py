from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        with open("./data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 16, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write("GAME OVER!", align="center", font=("Courier", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
