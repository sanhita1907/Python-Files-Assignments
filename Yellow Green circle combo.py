import turtle
tom=turtle.Pen()

for c in range(1,5):
    if c<2:
        tom.fillcolor("yellow")
    else:
        tom.fillcolor("green")

    tom.begin_fill()
    tom.circle(50)
    tom.end_fill()

    tom.left(90)
