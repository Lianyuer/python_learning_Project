"""
    信息去重
"""

my_list = ["浙江农林大学", "浙江大学", "浙江农林大学", "清华大学", "python", "java", "c++", "python"]

# 定义一个空集合
my_set_empty = set()

# 通过for循环遍历列表，并将列表的元素添加至集合
for x in my_list:
    my_set_empty.add(x)
print(f"列表的内容是：{my_list}")
print(f"去重后的集合为：{my_set_empty}")