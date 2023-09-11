import turtle
screen = turtle.Screen()
screen.setup(500,600,startx=0, starty= 0)
squary = turtle.Turtle()
squary.speed(10)

for i in range(600):
    squary.forward(i)
    squary.left(91)
