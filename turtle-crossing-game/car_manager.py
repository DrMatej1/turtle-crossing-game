from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT
        super().__init__()
        self.hideturtle()

    def movel(self):
        for i in self.all_cars:
            i.setx(i.xcor() - 5)

    def create(self):
        random_ch = random.randint(1, 6)
        if random_ch == 1:
            new = Turtle("square")
            new.penup()
            new.color(random.choice(COLORS))
            new.shapesize(stretch_len=2)
            new.setx(300)
            new.sety(random.randint(-250, 250))
            self.all_cars.append(new)

    def sinc(self):
        self.car_speed += MOVE_INCREMENT

