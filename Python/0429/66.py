class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고, 학년은 {self.grade}학년 입니다.")

my_student = Student("홍길동", 2)
my_student.introduce()