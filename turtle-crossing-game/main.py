import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
test = CarManager()
player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    test.create()
    test.movel()

    for i in test.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            score.gameover()

    if player.at_finish():
        player.start()
        test.sinc()
        score.increase()



screen.exitonclick()
