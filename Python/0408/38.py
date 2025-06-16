# 38-1
n = int(input('어디까지 출력할까요: '))
for i in range(n):
    print(i+1)

# 38-2
n = int(input('어디까지 출력할까요: '))
for i in range(n, 0-1, -1):
    print(i)

# 38-3
n = int(input('몇 단: '))
print(f'{n}단')
for i in range(1, 10):
    print(f'{n} * {i} = {n*i :3}')