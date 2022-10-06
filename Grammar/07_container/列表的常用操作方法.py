"""
    在python中，如果将函数定义为class（类）的成员，那么函数称之为：方法
    方法和函数功能一样， 有传入参数，有返回值，只是方法的使用格式不同
    函数的使用: num = add(1, 2)
    方法的使用: student = Student()
              num = student.add(1, 2)
"""

mylist = ["python", "java", "c++"]
# 1.1 查找某元素在列表内的下标索引
index = mylist.index("python")
print(f"python在列表中的下标索引值是：{index}")
# 1.2 如果被查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"python在列表中的下标索引值是：{index}")

# 2. 修改特定下标索引的值
mylist[0] = "大众传媒"
print(f"列表被修改元素值后，结果是：{mylist}")

# 3. 在指定下标位置插入新元素
mylist.insert(1, "best")
print(f"列表插入元素后，结果是：{mylist}")

# 4. 在列表的尾部追加‘’‘单个’‘’新元素
mylist.append("农林程序员")
print(f"列表在追加了元素后，结果是：{mylist}")

# 5. 在列表的尾部追加‘’‘一批’‘’新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表在追加了一个新的列表后，结果是：{mylist}")

# 6. 删除指定下标索引的元素（2中方式）
mylist = ["python", "java", "c++"]

# 6.1 方式1：del 列表[下标]
del mylist[2]
print(f"列表删除元素后，结果是：{mylist}")
# 6.2 方式2：列表.pop[下标]
mylist = ["python", "java", "c++"]
element = mylist.pop(2)
print(f"通过pop方法取出元素后列表内容：{mylist}, 去除的元素是：{element}")

# 7. 删除某元素在列表中的第一个匹配项
mylist = ["java", "c++", "java", "c++", "python"]
mylist.remove("java")
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

# 8. 清空列表
mylist.clear()
print(f"列表被清空，结果是：{mylist}")

# 9. 统计列表内某元素的数量
mylist = ["java", "c++", "java", "c++", "python"]
count = mylist.count("java")
print(f"列表中java的数量是：{count}个")

# 10. 统计列表中全部的元素数量
mylist = ["java", "c++", "java", "c++", "python"]
count = len(mylist)
print(f"列表的元素数量总共有：{count}个")
