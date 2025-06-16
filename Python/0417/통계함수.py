import math
lst = list(range(1,11))
print(lst)

# 평균
mean = sum(lst) / len(lst)
print(f'평균 {mean}')

# 분산
mean = sum(lst) / len(lst)  # 평균 계산
variance = 0

for num in lst:
    variance += (num - mean) ** 2  # 각 값에서 평균을 뺀 값의 제곱을 누적

variance /= len(lst)  # 누적된 값을 데이터 개수로 나눔
print(f'분산 {variance}')

# 표준편차
std_dev = math.std(lst)
print(f'표준편차 {std_dev}')

# 최대공약수, 최소공배수
gcd = math.gcd(*lst)
lcm = math.lcm(*lst)
print(f'최대공약수 {gcd} 최소공배수 {lcm}')