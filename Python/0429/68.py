class MemberInfo:
    def __init__(self, idx, passwd, name):
        self.idx = idx
        self.passwd = passwd
        self.name = name
    def getMember(self):
        return f"회원번호: {self.idx}, 비밀번호: {self.passwd}, 이름: {self.name}"

my_member = MemberInfo('king', '123456', '홍길동')
print(my_member.getMember())