with open('attendance.txt') as f:
    print('출석한 학생들')
    for line in f:
        print(line.strip())