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


def draw_circle(radius):
    rgb = (random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    radius = 100
    tim.pensize(width=1
    tim.speed("fastest")
    tim.circle(radius)
    tim.right(10)


for num_circles in range(36):
    draw_circle(num_circles)  # , extent=0, steps=1)


# for shape_sides_n in range(3, 41):
#     draw_shapes(shape_sides_n)

def random_walk(num_steps):
    rgb=(random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    tim.pensize(width=10)
    tim.speed("fastest")
    direction=[0, 90, 180, 270, 360]
    for _ in range(num_steps):
        tim.forward(30)
        tim.setheading(random.choice(direction))


# for walk_steps_n in range(3, 201):
#     random_walk(walk_steps_n)


def square():
    rgb=(random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def pentagon():
    rgb=(random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(5):
        tim.forward(100)
        tim.right(360/5)


def hexagon():
    rgb=(random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(6):
        tim.forward(100)
        tim.right(360/6)


def heptagon():
    rgb=(random.random(), random.random(), random.random())
    tim.pencolor(rgb)
    for _ in range(7):
        tim.forward(100)
        tim.right(360/7)


def octagon():
    rgb=(random.random(), random.random(), random.random())
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


screen=Screen()
screen.exitonclick()
