# 수강신청 프로그램

# list_a = ['홍길동', '일지매']

# new = input('추가할 학생 이름: ')
# list_a.append(new)

# print(f'{new} 학생의 신청이 완료되었습니다.')
# print(f'현재 이 과목의 최종 신청자는 {list_a}입니다.')

list_a = ['홍길동', '일지매', '전우치']

# delet = input('철회할 학생 이름: ')
# list_a.remove(delet)
# # list_a.pop(list_a.index(delet))

# print(f'{delet} 학생의 철회가 완료되었습니다.')
# print(f'현재 이 과목의 최종 신청자는 {list_a}입니다.')

change = input('변경 전 이름: ')
change2 = input('변경 후 이름: ')
list_a[list_a.index(change)] = change2
print(f'요청하신 대로 {change} 학생의 이름이 {change2}로 변경되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {list_a}입니다')