# 39-1
n = int(input('자연수 입력: '))
sum_1 = 0
for i in range(1, n+1):
    sum_1 += i
print(f'1부터 {n}까지의 합: {sum_1}')

# 39-2
n = int(input('자연수 입력: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f'{n}! = {factorial}')