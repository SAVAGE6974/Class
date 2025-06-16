n = 5
# n개의 0으로 초기화된 리스트
result = [0 for i in range(n)]
print(result)

# 0 ~ n으로 초기화된 리스트
result = [i for i in range(n)]
print(result)

# array 리스트의 값을 그대로 복사
array = [i for i in range(10, 16)]
result = [i for i in array]
print(result)

# array의 제곱값을 구하는 리스트
array = [i for i in range(10, 20, 2)]
result = [n ** 2 for n in array]
print(result)

# 리스트의 각 문자열의 길이를 저장하는 리스트
arra = ['list', 'comprehension', 'pthon']
result = [len(i) for i in arra]
print(result)

# 정수로만으로 구성된 리스트
old_list = ['1', '2', 'A', False, 3]
result = [i for i in old_list if type(i) == int]
print(result)

# 범위 내 짝수만 저장하는 리스트
result = [i for i in range(1, 10) if i % 2 == 0]
print(result)

# 배열에서 양수만 저장하는 리스트
array = [-1, 0, -4, 24, 5, -10, 2]
result = [i for i in array if i > 0]
print(result)