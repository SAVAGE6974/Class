import random
count = 0

user = list(map(int, input('2개입력(1~6, 중복허용): ').split()))

com = [random.randint(1, 6) for _ in range(2)]

print(f'컴퓨터: {com}')

if com[0] == user[0] or com[0] == user[1]:
    count += 1

if com[1] == user[0] or com[1] == user[1]:
    count += 1

if count == 0:
    print('3등')
elif count == 1:
    print('2등')
elif count == 2:
    print('1등')

print(count)