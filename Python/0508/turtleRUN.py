from turtle import *
import random as r

tc = Turtle()
tc.shape("turtle")
tc.color('white')
tc.up()
tc.speed(0)

tv = Turtle()
tv.shape("turtle")
tv.color('red')
tv.up()
tv.speed(0)
tv.goto(0, 200)

tf = Turtle()
tf.shape("turtle")
tf.color('green')
tf.up()
tf.speed(0)
tf.goto(0, -200)

def turn_right():
    tc.setheading(0)

def turn_down():
    tc.setheading(270)

def turn_up():
    tc.setheading(90)

def turn_left():
    tc.setheading(180)

def start():
    global playing
    if playing == False:
        playing = True
        clear()
        play()

def play():
    tc.fd(10)
    ang = tv.towards(tc.pos())
    tv.setheading(ang)
    tv.fd(9)

    if tc.distaance(tf) < 12: # 주인공과 먹ㅣ 거가 가우ㄴ
        start_x = r.randint(-230, 230)
        start_y = r.randint(-230, 230)
        tf.goto(start_x, start_y) # 먹이를 다른곳으로 이동
    if tc.distance(tv) >= 12: # 주인공과 악당 거가 멀면
        ontimer(play, 100) # 0.1초 후에 play() 함수 호출
    
def ready():
    setup(500, 500)
    title("Turtle Run")
    bgcolor('orange')

def move():
    onkeypress(turn_right, "Right")
    onkeypress(turn_up, "Up")
    onkeypress(turn_down, "Down")
    onkeypress(turn_left, "Left")
    onkeypress(play, "space")

def msg(m1, m2):
    clear()
    tc.goto(0, 100)
    write(m1, False, "center", ("", 20))
    tc.goto(0, -100)
    write(m2, False, "center", ("", 15))
    home()
    
ready()
move()
listen()