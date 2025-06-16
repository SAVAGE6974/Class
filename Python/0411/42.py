# 오름차순 약수 구하기
number = int(input('Enter a number: '))
for i in range(number):
    if number % (i+1) == 0:
        print(i+1)

# 내림차순 약수 구하기
number = int(input('Enter a number: '))
for i in range(number, 0, -1):
    if number % i == 0:
        print(i)