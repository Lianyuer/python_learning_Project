
# 给定义的字符串
my_str = "python and java"

# 统计字符串内有多少个"a"字符
num = my_str.count("a")
print(f"字符串{my_str}中有{num}个a")

# 将字符串内的空格，全部替换为字符"|"
new_str = my_str.replace(" ", "|")
print(f"将字符串{my_str}中的空格全部替换为|后，内容为：{new_str}")

# 并按照"|"进行字符串分割，得到列表
new_str = new_str.split("|")
print(f"将字符串{my_str}按'|'进行分割，结果是：{new_str}")