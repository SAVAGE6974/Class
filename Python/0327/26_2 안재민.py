import random
win_or_lose = None # 1일 경우 win 2일 경우 lose 3일경우 비김

com = random.randint(1, 3) 
user = int(input('입력(1: 가위 2: 바위 3:보): '))

reduce = user - com

if com == 1: com = '가위'
elif com == 2: com = '바위'
else: com = '보'

if user == 1: user = '가위'
elif user == 2: user = '바위'
else: user = '보'

if reduce == 0: win_or_lose = 3
elif reduce == 1: win_or_lose = 1
else: win_or_lose = 2

if win_or_lose == 1:
    print(f'user: {user}  com: {com} --> 이김')
elif win_or_lose == 2:
    print(f'user: {user}  com: {com} --> 짐')
else:
    print(f'user: {user}  com: {com} --> 비김')