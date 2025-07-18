import turtle

t = turtle.Turtle()
t.speed(0)
for i in range(6):
    t.circle(100,60)
    t.left(120)
    t.circle(100,60)
    t.left(120)
    t.right(60)
turtle.done()