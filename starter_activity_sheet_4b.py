# week 4 Loops

import turtle

# Initializing the turtle
t = turtle.Turtle()
    
def square():
    
    for counter in range(4):
        t.forward(100)
        t.right(90)

square()
t.left(45)
square()
