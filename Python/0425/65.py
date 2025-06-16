class Dog:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind
    def bark(self):
        print(f"{self.name} says Woof!")
        
    def bark(self):
        print(f'{self.name}가 미쳐 날뛰듯이 짓고 있습니다. 멍먹먹먹멍멍멍멍멍!!!!!')
    def sit(self):
        print(f'{self.name}가 앉았습니다.')

my_dog = Dog("승아", 3, "진돗개")
my_dog.bark()
