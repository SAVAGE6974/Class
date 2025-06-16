from turtle import *
import random as r

x_min = -5; x_max = 5
y_min = -5; y_max = 5

space = 0.1

func_list = ["x*x", "abs(x)", "0.5*x + 1", "0.5*x**2 + 1", "x**3 - 2*x**2 + 1", "x**4 - 2*x**3 + x**2 - 1"]
color_list = ['red', 'blue', 'green', 'orange', 'purple']

setworldcoordinates(x_min, y_min, x_max, y_max)
speed(0)
pensize(3)

def draw_line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# x, y축 그리기
draw_line(x_min, 0, x_max, 0)
draw_line(0, y_min, 0, y_max)

def draw_func(func):
    penup()
    x = x_min
    first_point = True  
    while x <= x_max:
        y = eval(func) 
        if first_point:
            goto(x, y)  
            pendown() 
            first_point = False  
        else:
            goto(x, y) 
        x += space
    penup()

def draw_func_list(func_list):
    for func in func_list:
        color(r.choice(color_list))
        draw_func(func)
    penup()

draw_func_list(func_list)
