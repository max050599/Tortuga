import turtle
t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(120):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.left(61)
turtle.done()