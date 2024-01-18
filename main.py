import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


PLAYER = ""
SCREEN = ""
SCOREBOARD = ""

def setUp():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Cross the Street")
    screen.tracer(0)
    screen.listen()
    player = Player()
    screen.onkey(player.moveUp, "w")
    screen.onkey(player.moveUp, "Up")
    car = CarManager()
    game_is_On = True
    iteration = 0
    score = Scoreboard()

    return player, screen, game_is_On, iteration, score,car


def collision(cars, player):
    for car in cars:
        if player.distance(car) < 30:
            return True
    return False


def resetTheGame(player, scoreBoard, carManager):
    carManager.reset()
    player.reset()
    scoreBoard.reset()


def nextLevel(scoreBoard, player, carManager):
    scoreBoard.updateScore()
    player.reset()
    carManager.nextLevel()

def startTheGame():
    player, screen, game_is_on, iteration, scoreBoard, carManager = setUp()

    while game_is_on:
        carManager.createCars(iteration)
        iteration += 1
        carManager.move()

        # collision = game Over
        if collision(carManager.cars, player):
            resetTheGame(player, scoreBoard, carManager)
            iteration = 0
            continue

        # next Level
        if player.playerCrossLineY():
            nextLevel(scoreBoard, player, carManager)

        time.sleep(0.1)
        screen.update()
    screen.exitonclick()



startTheGame()





















