from turtle import *
turtle.Turtle()
turtle.goto(-45, -45)
def draw_octagon():
    for i in range(8):
        forward(100)
        left(45)

draw_octagon()

mainloop()
