# 定义列表
age_list = [21, 25, 21, 23, 22, 20]

# 追加数字31
age_list.append(31)
print(f"追加数字31后 结果是：{age_list}")

# 追加一个新列表[29, 33, 30]
new_list = [29, 33, 30]
age_list.extend(new_list)
print(f"追加一个新列表[29, 33, 30]后，结果是：{age_list}")

# 取出第一个元素（应是：21）
first_element = age_list[0]
print(f"取出的第一个元素是：{first_element}")

# 取出最后一个元素（应是：30）
last_element = age_list[-1]
print(f"取出的第一个元素是：{last_element}")

# 查找元素31，在列表中的下标位置
index = age_list.index(31)
print(f"元素31在列表中的下标位置是：{index}")