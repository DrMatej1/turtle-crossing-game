from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.start()

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def at_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def start(self):
        self.goto(STARTING_POSITION)