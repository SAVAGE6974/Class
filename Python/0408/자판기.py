juice = 800
money = None
change = None
i = 5

while True:
    if i == 0:
        print('주스가 매진되었습니다.')
    else:
        print('='*20)
        money = int(input('돈을 넣어주세요: '))
        if money == juice:
            print('맛있는 커피 드세요.')
        else:
            change = money - juice
            if money > juice:
                print(f'잔돈은 {change}원입니다.')
        i -= 1