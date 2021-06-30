import _tkinter
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
# r = random.random()
# b = random.random()
# g = random.random()
# rgb = (random.random(), random.random(), random.random())


def draw_shapes(num_sides):
    angle = 360/num_sides
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(num_sides):
        tim.forward(30)
        tim.right(angle)


# for shape_sides_n in range(3, 41):
#     draw_shapes(shape_sides_n)

def random_walk(num_steps):
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    tim.pensize(width=10)
    tim.speed(speed=6)
    direction = [0, 90, 180, 270, 360]
    for _ in range(num_steps):
        tim.forward(30)
        tim.right(random.choice(direction))


for walk_steps_n in range(3, 20):
    random_walk(walk_steps_n)


def square():
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def pentagon():
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(5):
        tim.forward(100)
        tim.right(360/5)


def hexagon():
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(6):
        tim.forward(100)
        tim.right(360/6)


def heptagon():
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(7):
        tim.forward(100)
        tim.right(360/7)


def octagon():
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(8):
        tim.forward(100)
        tim.right(360/8)


def dashed_line():
    for _ in range(15):
        tim.color("red")
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# dashed_line()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()


screen = Screen()
screen.exitonclick()
