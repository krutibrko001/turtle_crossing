from turtle import Turtle, Screen


class MyScreen:

    def __init__(self):
        self.screens = Screen()
        self.screens.setup(600, 600)
        self.screens.tracer(0)


    def screen_update(self):
        self.screens.update()

    def key_listen(self):
        self.screens.listen()

    def main_loop(self):
        self.screens.exitonclick()

    def on_key_press(self, funks, keyboard):
        self.screens.onkeypress(funks, keyboard)
