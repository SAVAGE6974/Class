answer = int(input('Enter a number: '))

for i in range(50, 101):
    if i % answer == 0:
        print(i)