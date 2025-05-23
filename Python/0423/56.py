# 두 점을 입력받는 함수
def get_data():
    a1, b1 = map(int, input("첫 번째 점 (x, y): ").split(','))
    a2, b2 = map(int, input("두 번째 점 (x, y): ").split(','))
    return a1, b1, a2, b2

# 직선의 기울기와 y절편을 구하는 함수
def get_line(a1, b1, a2, b2):
    if a1 == a2:
        rst = f'x = {a1}'  # 수직선
    else:
        slp = (b2 - b1) / (a2 - a1)
        y_i = b1 - (slp * a1)
        rst = f'y = {slp}x + ({y_i})'
    return rst

# 메인 실행
x1, y1, x2, y2 = get_data()
line = get_line(x1, y1, x2, y2)
print('--' * 20)
print("직선의 방정식:", line)