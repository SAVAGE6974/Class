from turtle import *

shape('turtle')
color('green')
pensize(3)

for i in range(4):
    fd(100)
    left(90)
    
color('red')

for i in range(3):
    fd(100)
    left(120)
    
color('blue')
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()

exitonclick()