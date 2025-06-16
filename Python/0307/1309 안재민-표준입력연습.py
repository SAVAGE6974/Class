# 체질량 지수 계산 프로그램

print('* ===================== *')
print('*  체질량 지수 계산 프로그램  *')
print('* ===================== *')

weight = int(input("체중을 입력하세요 (kg단위): "))
hight = int(input("키를 입력하세요 (cm단위): "))

hight = hight / 100
bmi = weight / (hight ** 2)

print(f'BMI: {bmi:.2f}')

# if bmi < 18.5:
#     print("저체중 입니다")
# elif bmi 