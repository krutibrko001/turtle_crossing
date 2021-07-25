from turtle import Turtle

class CrossingTurtle:

    def __init__(self):

        self.my_turtle = Turtle("turtle")
        self.my_turtle.color("black")
        self.my_turtle.penup()
        self.my_turtle.goto(0, -270)
        self.my_turtle.setheading(90)

    def move_up(self):
        self.my_turtle.forward(10)

    def move_down(self):
        self.my_turtle.forward(-10)

    def move_left(self):
        self.my_turtle.goto(self.xpos()-10, self.ypos())

    def move_right(self):
        self.my_turtle.goto(self.xpos()+10, self.ypos())

    def distc_method(self, enemy):
        self.my_turtle.distance(enemy)

    def xpos(self):
        self.my_turtle.xcor()
        return self.my_turtle.xcor()

    def ypos(self):
        self.my_turtle.ycor()
        return self.my_turtle.ycor()
