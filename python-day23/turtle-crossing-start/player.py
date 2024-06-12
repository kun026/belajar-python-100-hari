from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.seth(90)
        self.go_to_start()

    def go_up(self) -> None:
        self.fd(MOVE_DISTANCE)

    def go_to_start(self) -> None:
        self.setpos(STARTING_POSITION)

    def is_finish(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
