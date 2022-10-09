# 定义集合
my_set = {"python", "java", "c++", "农林大学", "python", "java", "c++", "农林大学"}
my_set_empty = set()   # 定义空集合
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty},类型是：{type(my_set_empty)}")

# 添加新元素
set = {1, 2, 3}
set.add(4)
print(f"添加4后的set集合为：{set}")

# 移除元素
set = {1, 2, 3, 4, 5}
set.remove(3)
print(f"remove set集合中的3后集合为{set}")

# 随机取出一个元素
set = {10, 3, 5, 2, 4}
num = set.pop()
print(f"从集合中随机取一个元素，为：{num}")

# 清空集合
set = {1, 2, 3, 4}
new_set = set.clear()
print(f"清空集合后，集合为：{new_set}")

# 取2个集合的差集
set1 = {1, 3, 5}
set2 = {1, 4, 6}
difference = set1.difference(set2)
print(f"两个集合的差集是:{difference}")

# 消除2个集合的交集(集合1更新为差集)
set1 = {1, 3, 5}
set2 = {1, 4, 6}
set1.difference_update(set2)
print(f"消除交集后，集合1结果是：{set1}")
print(f"消除交集后，集合2结果是：{set2}")

# 2个集合合并为1个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"合并后{set3}")
print(f"合并后{set2}")
print(f"合并后{set1}")

# 统计集合元素数量len()
set = {1, 2, 3, 4, 1, 2, 3, 4}
lenth = len(set)
print(f"集合的长度是：{lenth}")

# 集合的遍历
# 集合不支持下标索引，不能用同while循环
for x in set:
    print(f"集合的元素有：{x}")