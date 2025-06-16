import random

def genPass():
    chr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for i in range(random.randint(8, 15)): # 변경점: 비밀번호 길이를 8~15로 랜덤하게 설정
        password += random.choice(chr)
    return password

for i in range(3):
    result = genPass()
    print(f'암호 {i+1} : \033[31m{result} \033[00m')