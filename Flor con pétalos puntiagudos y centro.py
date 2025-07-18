import turtle

t = turtle.Turtle()
t.speed(0)
t.color("pink")
for i in range(12):
    t.begin_fill()
    for j in range(2):
        t.forward(100)
        t.left(45)
        t.forward(30)
        t.left(135)
    t.end_fill()
    t.left(30)
t.color("yellow")
t.penup()
t.goto(0,-20)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
turtle.done()