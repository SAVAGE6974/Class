# 원리합계 계산 프로그램

print("#" * 25)
print("원리합계 계산 프로그램")
print("#" * 25)

money = int(input("예금 금액(원): "))
per = float(input("예금 이율(%): "))
date = int(input("예금 기간(년): "))
print("#" * 25)

val = int(money + (money * per * 0.01 * date))

print(f'{money}원을 {per:.1f}% 이율로 {date}년간 예치후 원리합계는 {val}원')