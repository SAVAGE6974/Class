f = open("data_2.txt", 'r')

while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()