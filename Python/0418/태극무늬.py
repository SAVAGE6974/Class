# 정석
import turtle
t = turtle.Turtle()


color_list = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', 'pink', 'white', 'cyan', 'magenta', 'gray', 'lightblue']

screen = turtle.Screen()
screen.bgcolor('black')

t.speed(0)

for i in range(2000):
    t.pencolor(color_list[i % len(color_list)])
    t.fd(i)
    t.left(6969)

screen.exitonclick()

# # 편안
# from turtle import *

# color_list = ['red', 'blue', 'yellow']

# bgcolor('black')
# speed(0)

# for i in range(200):
#     pencolor(color_list[i % 3])
#     fd(i)
#     left(119)
# exitonclick()
