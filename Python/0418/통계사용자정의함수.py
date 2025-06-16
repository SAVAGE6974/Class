import math
lst = list(range(1,11))
print(lst)

def average(lst):
    return sum(lst) / len(lst)

def variance(lst):
    mean = average(lst)
    variance = 0
    for num in lst:
        variance += (num - mean) ** 2
    return variance / len(lst)

def std_dev(lst):
    return math.sqrt(variance(lst))

def gcd(lst):
    return math.gcd(*lst)
def lcm(lst):
    return math.lcm(*lst)

print(f'평균 {average(lst)}')
print(f'분산 {variance(lst)}')
print(f'표준편차 {std_dev(lst)}')
print(f'최대공약수 {gcd(lst)} 최소공배수 {lcm(lst)}')
