import turtle

t = turtle.Turtle()
t.speed(0)
for i in range(8):
    for j in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.right(45)
turtle.done()