sum_numbers = 0.0
count = 0

while True:

    number = float(input("실수형 숫자를 입력하세요 (음수 입력 시 종료): "))

    if number < 0:
        average = sum_numbers / count
        print(f"입력된 숫자의 합계: {sum_numbers}")
        print(f"입력된 숫자의 평균: {average}")
        break

    sum_numbers += number
    count += 1