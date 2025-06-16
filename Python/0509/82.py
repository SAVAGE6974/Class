with open('attendance.txt') as f:
    for i in range(5):
        name = input(f'{i+1}번: ')
        f.write(f'{name}\n')