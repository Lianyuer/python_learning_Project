class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象：name:{self.name}, age:{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("李连杰", 35)
stu2 = Student("林俊杰", 32)
stu3 = Student("周杰伦", 38)
print(stu1 == stu3)
print(stu1 >= stu3)
