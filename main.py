import turtle
import random

pen = turtle.Turtle()

colors = [
    "violet", 
    "indigo", 
    "blue", 
    "green", 
    "yellow", 
    "orange", 
    "red"
]

pen.pensize(10)

for x in range(6):
    pen.color(random.choice(colors))
    pen.forward(100)
    if x == 2:
        pen.right(180)
    else:
        pen.right(90)
        
pen.penup()
pen.goto(200, 0)

pen.color(random.choice(colors))
pen.pendown()
pen.left(180)
pen.forward(200)

turtle.done()
