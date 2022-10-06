"""
    有字符串"学农林，来浙江农林大学，我们欢迎您！"
    ·请使用任何学过的方式得到"浙江农林大学"
"""

my_str = "您迎欢们我，学大林农江浙来，林农学"

# 倒序字符串，切片取出
result1 = my_str[::-1][5: 11]
print(f"方式1结果：{result1}")

# 切片取出，然后倒序
result2 = my_str[6:12][::-1]
print(f"方式2结果：{result2}")

# split分隔"，" replace替换"来"为空，倒序字符串
result3 = my_str.split("，")[1].replace("来", "")[::-1]
print(f"方式3结果：{result3}")
