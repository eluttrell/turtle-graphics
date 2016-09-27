from turtle import *
import turtle

# Circle

def draw_circle():
    for i in range(360):
        forward(1)
        left(1)

# Hexagon

def draw_hex():
    for i in range(6):
        forward(100)
        left(60)

# Octagon

def draw_octagon():
    for i in range(8):
        forward(100)
        left(45)

# Pentagon

def draw_pentagon():
    for i in range(5):
        forward(100)
        left(72)

# Square

def draw_square():
    for i in range(4):
        forward(100)
        left(90)

# Star

def draw_star():
    left(36)
    for i in range(5):
        forward(200)
        left(144)

# Triangle

def draw_triangle():
    for i in range(3):
        forward(100)
        left(120)

    # Module Declaration

    # if __name__ == '__main__':
    #     draw_triangle()
    #     draw_star()
    #     draw_square()
    #     draw_hex()
    #     draw_pentagon()
    #     draw_octagon()
    #     draw_circle()
    #     mainloop()
    #
    # # Mainloop
    #
    # mainloop()
