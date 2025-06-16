# 숫자 리스트를 입력받음.
# for 문을 이용해 큰 숫자를 오른쪽으로 이동시키며 정렬.
# 한 번의 반복이 끝날 때마다 가장 큰 숫자가 정렬됨.
# 완전히 정렬되면 최종 리스트를 출력.


list_a = list(map(int, input('수를 입력하세요: ').split()))

for i in range(len(list_a)-1): # 맨 마지막 수는 정렬할 필요가 없음
    for j in range(len(list_a)-1-i):
        if list_a[j] > list_a[j+1]: # list_a[j]가 클 경우 자리를 바꿔줌
            list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

find = int(input('찾을 숫자번수를 입력하세요: '))
if find in list_a:
    print(f'{list_a.index(find)+1}번째에 있습니다.')
else:
    print('찾는 숫자가 없습니다.')


# list_a = list(map(int, input('수를 입력하세요: ').split()))

# list_a.sort()

# if find in list_a:
#     print(f'{list_a.index(find)+1}번째에 있습니다.')
# else:
#     print('찾는 숫자가 없습니다.')