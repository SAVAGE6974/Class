a, b = map(int, input().split())

try:
    c = a / b
except ZeroDivisionError:
    print('0으로 못나눔')
else:
    print(c)