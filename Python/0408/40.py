import random

while True:
    start = random.randint(1, 10)
    end = random.randint(1, 10)
    sum_1 = 0
    if start == end:
        print(f'{start}부터 {end}까지의 합: {start}')
        break
    else:
        if start > end:
            start, end = end, start
        for i in range(start, end+1):
            sum_1 += i
        print(f'{start}부터 {end}까지의 합: {sum_1}')
        