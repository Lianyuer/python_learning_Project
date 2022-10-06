# 需求：统计字符串的长度，不使用内置函数len()
str1 = "python"
str2 = "java"
str3 = "c++"

# 定义一个计数的变量
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}长度为：{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}长度为：{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}长度为：{count}")


# 可以使用函数，来优化这个过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}长度为：{count}")

my_len(str1)
my_len(str2)
my_len(str3)
