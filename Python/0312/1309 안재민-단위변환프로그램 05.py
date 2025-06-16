# 단위 변환 프로그램
# import math

print("^"*26)
print("km 변환기 (mile -> km)")
print("^"*26)

mile = float(input('볼 속도(mile): '))

change = 1.609344 * mile
print(f'{mile}mile = {change:.1f}km')