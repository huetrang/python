import turtle
t = turtle.Turtle()
t.pensize(5)
t.color("blue","red")
t.begin_fill()
t.circle(100)
t.end_fill()

t.goto(-40,120)
t.color("red","blue")
t.begin_fill()
t.circle(100)
t.end_fill()