"""
    容器转换  ！！！容器不能转字典
"""
my_list = {1, 2, 3, 4, 5}
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

#len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串min元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max最大元素
print(f"列表 元素个数有：{max(my_list)}")
print(f"元组 元素个数有：{max(my_tuple)}")
print(f"字符串元素个数有：{max(my_str)}")
print(f"集合 元素个数有：{max(my_set)}")
print(f"字典 元素个数有：{max(my_dict)}")

# min最小元素
print(f"列表 元素个数有：{min(my_list)}")
print(f"元组 元素个数有：{min(my_tuple)}")
print(f"字符串元素个数有：{min(my_str)}")
print(f"集合 元素个数有：{min(my_set)}")
print(f"字典 元素个数有：{min(my_dict)}")

# 类型转换：容器转列表
print(f"列表 转列表的结果是：{list(my_list)}")
print(f"元组 转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合 转列表的结果是：{list(my_set)}")
print(f"字典 转列表的结果是：{list(my_dict)}")

# 类型转换：容器转元组
print(f"列表 转元组的结果是：{tuple(my_list)}")
print(f"元组 转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合 转元组的结果是：{tuple(my_set)}")
print(f"字典 转元组的结果是：{tuple(my_dict)}")

# 类型转换：容器转字符串
print(f"列表 转字符串的结果是：{str(my_list)}")
print(f"元组 转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合 转字符串的结果是：{str(my_set)}")
print(f"字典 转字符串的结果是：{str(my_dict)}")

# 类型转换：容器转集合
print(f"列表 转集合的结果是：{set(my_list)}")
print(f"元组 转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合 转集合的结果是：{set(my_set)}")
print(f"字典 转集合的结果是：{set(my_dict)}")

"""
    进行容器的排序，对容器的排序都会变成list对象
"""
my_list = {9, 2, 6, 4, 3}
my_tuple = (9, 2, 6, 4, 3)
my_str = "hdabcefg"
my_set = {9, 2, 6, 4, 3}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}

print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")

print(f"列表对象的反向排序结果：{sorted(my_list, reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple, reverse=True)}")
print(f"字符串对象的反向排序结果：{sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict, reverse=True)}")