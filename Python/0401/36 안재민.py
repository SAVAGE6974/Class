# while True:
#     try:
#         a, b = map(float, input().split())
#         sum1 = a + b
#         avg = sum1 / 2
#     except ValueError:
#         break

#     print(f'sum is {sum1}')
#     print(f'avg is {avg}')

lst = []
while True:
    try:
        score = float(input('점수: '))
    except ValueError:
        break
    else:
        list.append(score)


print('=' * 10)
print(f'합계: {sum(list):.1f}')
print(f'평균: {sum(lst)/len(lst):.1f}')