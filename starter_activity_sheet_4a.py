# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

import turtle
# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python


def mystery():
    t = turtle.Turtle()
    t.fillcolor("Green")
    t.begin_fill()
    t.pencolor("Red")
    t.forward (100) 
    t.right (90)
    t.end_fill()
    t.forward (100) 
    t.right (90) 
    t.forward (100) 
    t.right (90) 
    t.forward (100) 

mystery()
