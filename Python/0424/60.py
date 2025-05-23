from turtle import *

d = 10
def turn_right():
    setheading(heading(0))
    fd(d)
def turn_up():
    setheading(heading(90))
    fd(d)
def turn_left():
    setheading(heading(180))
    fd(d)
def turn_down():
    setheading(heading(270))
    fd(d)

def blank():
    clear()

def keyboard():
    onkey(turn_right, "Right")
    onkey(turn_up, "Up")
    onkey(turn_left, "Left")
    onkey(turn_down, "Down")
    onkey(blank, "space")
    listen()

def mouse():
    speed(0)
    pensize(2)
    ondrag(goto)
    onkeypress(blank, "Escape")
    listen()

# main
select = input("키보드(1) 마우스(2) : ")
if select == "1":
    keyboard()
elif select == "2":
    mouse()