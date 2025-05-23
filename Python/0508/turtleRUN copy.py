                                
                                
# 버전2

from turtle import *
import random as r

score = 0 # 점수
playing = False # 플래그

# def show_title():
#     penup()
#     goto(0, 100)
#     color("white")
#     pendown()
#     write("Turtle Run")

# 주인공 거북(흰색)
tc = Turtle()
tc.shape('turtle') #거북 모양
tc.color('white') #색상
tc.up() # 펜 올리기
tc.speed(0) # 속도

#악당 거북(빨간색)
tv = Turtle()
tv.shape('turtle') #거북 모양
tv.color('red') #색상
tv.speed(0) #속도
tv.up() #펜올리기
tv.goto(0, 200) # 악당 시작 위치

# 먹이 객체 생성
tf = Turtle()
tf.shape('circle') #원 모양
tf.color('green') #색상
tf.speed(0) #속도
tf.up() #펜올리기
tf.goto(0, -200) # 먹이 시작 위치

# 움직임 정의
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
        palying = True
        clear()
        play()

#play 함수
def play():
    global score
    global playing

    tc.fd(10) # 주인공 앞으로 이동
    ang = tv.towards(tc.pos()) # 주인공 위치의 각도
    tv.setheading(ang) # 악당이 주인공 쪽을 바라보게
    tv.fd(9) # 악당 앞으로 이동

    if tc.distance(tv) < 12:
        text = (f'score: {score}')
        msg("Game Over", text)
        playing = False
        score = 0

    if tc.distance(tf) < 12:
        score +=1
        tc.write(score)
        start_x=r.randint(-230, 230)
        start_y= r.randint(-230, 230)
        tf.goto(start_x,start_y) # 먹이를 다른 곳으로 이동
    if playing:
        ontimer(play, 100)

    # if tc.distance(tv) >= 12: # 주인공과 악당 거리가 멀면
    #     ontimer(play,100) #0.1초 후 play 함수 실행(게임 계속)

def msg(m1, m2):
    hideturtle()
    clear()
    up()
    goto(0,100)
    down()
    write(m1, False, "center", ("", 20))
    up()
    goto(0,-100)
    down()
    write(m2, False, "center", ("",15))
    up()
    home()

#게임 준비
def ready():
        setup(500,500) # 화면 크기
        title("Turtle Run") # 창 제목
        bgcolor("orange") # 배경 색
        shape("turtle")
        speed(0)


def move():
    onkeypress(turn_right, "Right")
    onkeypress(turn_up, "Up")
    onkeypress(turn_left, "Left")
    onkeypress(turn_down, "Down")
    onkeypress(start, "space") # 스페이스키 눌러서 게임 시작

# 메인
ready() # 게임 준비
move() # 시작
listen() # 이벤트 감지
msg("Turtle Run", "[Space]")

exitonclick()
                            