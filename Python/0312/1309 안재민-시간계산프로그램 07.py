('#' * 26)
print('분초 계산 프로그램')
print('#' * 26)

seond = int(input('초 입력: '))

print(f'{seond // 3600}시간 {(seond % 3600) // 60}분 {seond % 60}초')