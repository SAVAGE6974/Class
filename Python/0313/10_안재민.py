# a = list(range(0, 1001, 100))
# print(a)

data = [30, 10, 20]
print(f'현재 리스트: {data}')

print(f'리스트 데이터 개수: {len(data)}')
data.append(40)
print(f'40 추가 후의 리스트: {data}')
last = data[-1]
print(f'리스트 마지막 데이터: {data[last]}')
data.sort()
print(f'오름차순 정렬: {data}')
data.reverse()
print(f'내림차순 정렬: {data}')
data[data.index[20]]=222
print(f'20을 222로 변경: {data}')
data.remove(222)
print(f'222 삭제: {data}')
print(f'데이터 20의 위치(index): {data.index(20)}')
del data[2]
print(f'두 번째 데이터 삭제후 리스트: {data}')

data2 = [77, 88, 77]
data.extend(data2)
print(f'리스트 연결: {data}')
print(f'77의 개수: {data.count(77)}')
del data[2]
print(f'index 2 위치의 데이터 삭제후 리스트: {data}')