number, type = map(int, input().split(','))

year = 2025
old = 0
sex = ''

if type == 1:
    old = year - (1900 + number[:2]) + 1
    sex = '남성'
elif type == 2:
    old = year - (2000 + number[:2]) + 1
    sex = '남성'
elif type == 3:
    old = year - (1900 + number[:2]) + 1
    sex = '여성'
elif type == 4:
    old = year - (2000 + number[:2]) + 1
    sex = '여성'

print(f'현재나이 : {old}세, 성별: {sex}')