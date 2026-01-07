import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
numside = 10
sidelen = 70
angle = 360.0/numside
for i in range(numside):
    polygon.forward(sidelen)
    polygon.right(angle)
turtle.done()    