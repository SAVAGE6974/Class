def average(a, b, c):
    return f'{(a + b + c) / 3:.2f}'

first, second, third = map(int, input().split())
print(f'평균: {average(first, second, third)}')