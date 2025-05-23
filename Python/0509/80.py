f = open('data_2.txt', 'r')

lines = f.readlines()
print(lines)

for line in lines:
    line = f.strip()
    print(line)

f.close()