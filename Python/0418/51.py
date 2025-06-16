# 51-1
def sum_fac(n):
    sum_1 = 0
    for i in range(1, n+1):
        sum_1 += i
    print(f'1부터 {n}까지의 합: {sum_1}')

sum_fac(10)
sum_fac(100)
sum_fac(1000)

# 51-2
def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(f'{n}! = {factorial}')

factorial(5)
factorial(5)
