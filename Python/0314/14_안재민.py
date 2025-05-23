stu1 = {'학반':105, '번호':20, '이름':'홍길동'}
print(stu1)

stu1['연락처'] = '010-1234-5678'
print(stu1)

stu1['동아리'] = '파이썬 동아리'
print(stu1)

del stu1['연락처']
print(stu1)

stu1['동아리'] = '연극 동아리'
print(stu1)