'''print('n각형 만들기')
n=int(input('n각형을 입력하세요 : '))
d=int(input('한 변의 길이 : '))

angle=360/n

for i in range(n):
      fd(d)
      lt(angle)

exitonclick()'''


from turtle import *
import random

shape('turtle')
cr_lst=['red','orange','yellow','green','blue','navy','puple','black']
cr= random.choice(cr_lst)
color(cr)

n=int(input('몇 각형?: '))
d= int(input('한 변의 길이: '))
      
angle=360/n
      
for i in range(n):
      fd(100)
      lt(angle)