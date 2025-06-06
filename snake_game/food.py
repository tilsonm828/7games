from turtle import Turtle
import random
import helper


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        #****** the color of food  ******
        self.color(helper.random_color())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        #****** the color of food  ******
        self.color(helper.random_color())
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
