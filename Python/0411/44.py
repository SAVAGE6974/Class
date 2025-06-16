col = int(input('열 입력: '))
row = int(input('행 입력: '))

list_a = [[i * j for j in range(1, row + 1)] for i in range(1, col + 1)]
# for i in range(1, row + 1)은 바깥쪽에 있는 for문
# for j in range(1, col + 1)은 안쪽에 있는 for문
# 왜 i * j로 사용했냐? 저렇게 해야지 행 * 열의 형식으로 출력이 되기 때문

for i in list_a:
    for j in range(len(i)):
        print(f'{i[j]}', end=' ')
    print()