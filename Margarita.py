import turtle

t = turtle.Turtle()
t.speed(0)
for i in range(12):
    t.circle(60,60)
    t.left(120)
    t.circle(60,60)
    t.left(120)
    t.right(30)
turtle.done()