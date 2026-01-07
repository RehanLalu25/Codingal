import turtle 
Pattern = turtle.Screen()
Pattern.bgcolor("light blue")
Pattern.title("turtle")
mypen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        mypen.fd(size + 1)
        mypen.left(90)
        size = size - 5 
    size = size + 1
        