import turtle as w
screen =w.Screen()
screen.setup(500,600,startx=0,starty=100)
w.penup()
w.goto(-200.0,213.0)
w.pendown()
w.color("black","orange")
w.begin_fill()
for x in range(2):
    w.forward(100)
    w.right(90)
    w.forward(200)
    w.right(90)
w.end_fill()
w.forward(200)
w.color("black","green")
w.begin_fill()
for x in range(2):
    w.forward(100)
    w.right(90)
    w.forward(200)
    w.right(90)
w.end_fill()

w.color("black","red")
w.begin_fill()