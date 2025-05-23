import turtle as t

def input_data():
    x, y = map(int, input("-종류(3이상) 한변(5이상)").split())
    while True:
        if x < 3 or y < 5:
            print("잘못된 입력입니다.")
            continue
        else:
            return x, y

def moving():
    a, b = map(int, input("이동할 좌표를 입력하세요").split())
    t.penup()
    t.goto(a, b)
    t.pendown()

def polygon():
    n, a = input_data()
    for i in range(n):
        t.forward(a)
        t.right(360 / n)

print("== 도형 그리기 ==")
while True:
    moving()
    polygon()

    con = int(input("계속하시겠습니까? (1: 예, n: 아니오) "))
    if con != 1:
        break

t.exitonclick()