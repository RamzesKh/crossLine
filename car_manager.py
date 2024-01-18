import random
import time
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
    def createNewCar(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        random_y = random.randint(-280,260)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.penup()
        car.goto(300,random_y)
        self.cars.append(car)
    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def createCars(self,iteration):
        if iteration % 6 == 0:
            self.createNewCar()

    def reset(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE = 5
        self.clearCars()

    def nextLevel(self):
        self.clearCars()
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE = STARTING_MOVE_DISTANCE + MOVE_INCREMENT

    def clearCars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()




