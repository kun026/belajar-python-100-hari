from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self) -> None:
        self.level += 1
        self.update_score()

    def game_over(self) -> None:
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
