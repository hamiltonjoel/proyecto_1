import turtle
ventana = turtle.Screen()
poper= turtle.Turtle()
poper.shape("turtle")
poper.color("red")

for i in range(8):
    poper.circle(100)
    poper.left(45)

poper.write("flor", font=("Arial", 30, "normal"))
turtle.done()