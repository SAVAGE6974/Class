f = open("data_2.txt", "w")

for i in range(1, 11):
    line = i
    f.write(f'{i}\n')

f.close()
print('정상종료')