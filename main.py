from turtle import Turtle
from screens import MyScreen
from main_turtle import CrossingTurtle
from enemy import Enemy
from random import choice
from scoreboard import MyText

scr = MyScreen()
my_trtl = CrossingTurtle()
enm = Enemy()
my_text = MyText()
game_on = True

clrs = ["red", "blue", "yellow", "black", "green", "pink"]
lst = []

scr.key_listen()
scr.on_key_press(my_trtl.move_up, "Up")
scr.on_key_press(my_trtl.move_down, "Down")
scr.on_key_press(my_trtl.move_left, "Left")
scr.on_key_press(my_trtl.move_right,  "Right")


while game_on:
    scr.screen_update()
    enm.clrs(choice(clrs))
    enm = Enemy()
    lst.append(enm)
    for item in lst:
        item.enemy_move_forward()

    for item in lst:
        if my_trtl.ypos() == enm.danger.ycor():
            print("Collided")
        else:
            print("No collision")



scr.main_loop()
