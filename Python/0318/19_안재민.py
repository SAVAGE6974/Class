# 카드 요금을 이용하여 승차 가능 여부 판별 프로그램

fee = 850
card = int(input('카드 잔액: '))

if card >= fee:
    print('승차 가능')
else:
    print('승차 불가능')


fee = 850
card = int(input('카드 잔액: '))
if card <= fee:
    print('승차 불가능')
else:
    print('승차 가능')