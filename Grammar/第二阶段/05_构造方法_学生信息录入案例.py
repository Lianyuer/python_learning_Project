"""
    设计一个类记录学生的姓名、年龄、地址
    要求：
    ·通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘输入
    ·输入完成后，使用print语句，完成信息的输入
"""


class Student:
    name = None
    age = None
    addr = None

    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr


print("当前录入第一位学生信息，总共录入十位学生信息")
i = 0
for i in range(0, 9):
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    addr = input("请输入学生地址：")
    stu = Student(name, age, addr)
    print(f"学生{i + 1}信息录入完成，信息为：【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.addr}】")
