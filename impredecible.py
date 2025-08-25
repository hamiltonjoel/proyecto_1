import turtle
import random
import time

turtle.bgcolor("black")
turtle.title("tortuga impredecible")
t = turtle.Turtle()
t.speed(0)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    turtle.colormode(255)   # muy importante para que acepte valores RGB 0–255
    t.pencolor(r, g, b)

    t.fd(random.randint(20, 100))
    t.right(random.randint(0, 360))

turtle.done()