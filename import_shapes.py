import shapes
import turtle
from turtle import *
# shapes.draw_star()
# shapes.draw_octagon()
# shapes.draw_circle()
# shapes.draw_hex()
# shapes.draw_pentagon()
# shapes.draw_square()
# shapes.draw_triangle()

coord_list = [(-100, -100), (100, 100), (-100, 100), (100, -100)]

for coord in coord_list:
    if coord_list == 0:
        up()
        home()
        x, y = coord
        setheading(0)
        forward(x)
        setheading(90)
        forward(y)
        down()
        shapes.draw_square()
    if coord_list == 1:
        up()
        home()
        x, y = coord
        setheading(0)
        forward(x)
        setheading(90)
        forward(y)
        down()
        shapes.draw_star()
    if coord_list == 2:
        up()
        home()
        x, y = coord
        setheading(0)
        forward(x)
        setheading(90)
        forward(y)
        down()
        shapes.draw_octagon()
    if coord_list == 3:
        up()
        home()
        x, y = coord
        setheading(0)
        forward(x)
        setheading(90)
        forward(y)
        down()
        shapes.draw_circle()

mainloop()
