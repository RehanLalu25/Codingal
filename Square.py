import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")   # background colour

pen = turtle.Turtle()
pen.color("purple")           # square colour
pen.pensize(3)
pen.speed(3)

for i in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()
