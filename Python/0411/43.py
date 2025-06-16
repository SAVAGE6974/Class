# :>2 는 2자리 정렬 >방향에 따라

for i in range(1, 9):
    print(f'== {i+1}단 ==')
    for j in range(9):
        print(f'{i+1} * {j+1} = {(i+1)*(j+1):>2}')
    print()