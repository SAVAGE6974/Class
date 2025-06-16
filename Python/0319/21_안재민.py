# 놀이기구 이용 가능 여부 판별

hight = float(input("키(cm): "))
weight = float(input("몸무게(kg): "))
print('#' * 10)

if hight >= 130 and hight < 190 and weight >= 25 and weight < 100:
    print('이용 가능')
else:
    print('이용 불가능')