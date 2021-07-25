from turtle import Turtle
from random import randint, choice


class Enemy:

    lst = []
    def __init__(self):

        self.danger = Turtle("square")
        self.danger.color("red")
        self.danger.shapesize(1.3, 3)
        self.danger.setheading(0)
        self.danger.penup()
        self.enemy_random_y_pos()

    def enemy_spawn(self):
        pass

    def enemy_move_forward(self):
        self.danger.forward(-10)

    def enemy_random_y_pos(self):
        self.danger.goto(self.danger.xcor()+310, self.random_num())

    def random_num(self):
        ynum = randint(-240, 240)
        return ynum

    def current_pos(self):
        return self.danger.xcor()

    def clrs(self, colors):
        return self.danger.color(colors)
