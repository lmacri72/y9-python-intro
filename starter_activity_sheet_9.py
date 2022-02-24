# using easygui
# easygui gives a windows environment for Python with simple commands
# here are some example programs using easygui - try them out!


from easygui import *

def example_1():
    msgbox("Hello Everyone!")

def example_2():
    msgbox('Hello Everyone!','Buttons program')

def example_3():
    msgbox('Hello Everyone!','Buttons program','Click here!')

def example_4():
    ynbox("Do you like bananas? ", image="bananas.jpg")

def example_5():
    answer = ynbox("Do you like bananas? ", image="bananas.jpg")
    if answer == True:
        msgbox("Me too! ")
    else:
        msgbox("Don't forget your five a day!!")    

def example_6():
    question = "What is the name of this fruit? "
    reply = buttonbox(question,image="bananas.jpg",choices=["apple","banana","plum"])
    if reply == "banana":
        msgbox("Correct")
    else:
        msgbox("Incorrect")

example_1()
#example_2()
#example_3()
#example_4()
#example_5()
#example_6()
