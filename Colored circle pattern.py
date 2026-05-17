import turtle
tom=turtle.Pen()

colors=["red", "green", "blue", "magenta", "orange"]
angles=[30, 45, 60, 75, 90]

for c in range(0,5):
    tom.begin_fill()
    tom.pencolor(colors[c])
    tom.circle(50)
    tom.fillcolor(colors[c])
    tom.left(angles[c])
    tom.end_fill()
