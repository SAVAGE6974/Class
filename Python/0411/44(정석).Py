row = int(input('열 입력: '))
col = int(input('행 입력: '))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        print(f'{i * j:>2}', end=' ')
    print()