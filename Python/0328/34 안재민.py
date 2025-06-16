na = []

while True:
    answer = input('과일 입력: ')

    if answer not in na:
        na.append(answer)
    else:
        print('리스트 안에 있음')
    
    if len(na) == 5:
        break