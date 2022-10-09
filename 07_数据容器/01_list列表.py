"""、
    列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
"""

# 定义一个列表list
my_list = ['python', 'java', 'c++']
print(my_list)
print(type(my_list))

my_list = ['python', 666, True]
print(my_list)
print(type(my_list))

# 嵌套列表的定义
my_list = [[1, 2 , 3], [4, 5 , 6]]
print(my_list)
print(type(my_list))

# 列表的下标索引
my_list = ["Tom", "Lily", "Rose"]
# 列表[下标索引]，从前向后0开始，每次+1，从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])   # 注意下标索引越界

# 通过下标索引取出数据（倒序取出）
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])


