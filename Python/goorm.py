import random as rnd

count_lst = [i for i in range(1, 21)]
computer_choice = rnd.choice(count_lst)

user_choice = int(input("1-20 사이의 숫자를 입력하세요: "))

while True:
    if user_choice < 1 or user_choice > 20:
        print("1-20 사이의 숫자를 입력하세요.")
        user_choice = int(input("다시 입력: "))
    elif user_choice < computer_choice:
        print("up")
        user_choice = int(input("다시 입력: "))
    elif user_choice > computer_choice:
        print("down")
        user_choice = int(input("다시 입력: "))
    else:
        print("correct")
        break
print("게임을 종료합니다.")