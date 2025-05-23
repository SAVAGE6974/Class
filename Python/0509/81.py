name = input('이름: ')
age = input('나이: ')
school = input('학교: ')

f = open("me.txt", "w")
f.write(f'{name}\n')
f.write(f'{age}\n')
f.write(f'{school}\n')

f.close()