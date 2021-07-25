from turtle import Turtle


class MyText:

    def __init__(self):
        self.score = Turtle()
        self.score.color("black")
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(-250, 250)
        self.score.write("Level: 0", True, font = ("Arial", 15, "normal"))

