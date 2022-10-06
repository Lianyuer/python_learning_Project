# 定义一个元组，记录学生信息（姓名、年龄、爱好）
student_info = ("周杰伦", 11, ["football", "music"])
# 查询年龄所在下标位置
index = student_info.index(11)
print(f"年龄所在下标{index}")

# 查询学生的姓名
name = student_info[0]
print(f"学生的姓名是：{name}")

# 删除学生爱好中的football
del student_info[2][0]
print(f"删除学生爱好中的football后，元组内容是{student_info}")

# 增加爱好：coding到爱好list内
student_info[2].append("coding")
print(f"增加爱好：coding到爱好list中后，结果是：{student_info}")