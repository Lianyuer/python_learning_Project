f = open("E:/test.txt", "r", encoding="UTF-8")
# 方式1：读取全部内容，通过字符串count方法统计world单词数量
# content = f.read()
# count = content.count("world")
# print(f"world在文件中出现了{count}次")

# 方式2：读取内容，一行一行读取
count = 0
for line in f:
    line = line.strip()  # 去除开头和结尾的空格以及换行符
    words = line.split()
    for word in words:
        if word == "world":
            count += 1  # 如果单词是world，进行数量加1
# 判断单词出现次数并累积
print(f"world出现的次数是：{count}")

# 关闭文件
f.close()