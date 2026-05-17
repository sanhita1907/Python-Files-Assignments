import turtle
tom = turtle.Pen()

colors = ["red", "green", "blue", "magenta", "orange"]

for c in range(1,5) :
       tom.pencolor(colors[c])
       tom.width(c)
       tom.forward(100)
       tom.left(90)
