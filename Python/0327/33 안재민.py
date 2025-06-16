while True:
    test = int(input())
    
    if test == 0:
        break
    elif test % 5 == 0:
        print('5의 배수')
    else:
        print('5의 배수 아님')