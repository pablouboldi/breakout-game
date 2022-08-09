from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        self.goto(0, -210)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def miss(self):
        self.goto(0, -210)
        self.move_speed = 0.05
        self.y_move *= -1
