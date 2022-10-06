import time
# 打开文件
f = open("E:/test.txt", "r", encoding="UTF-8")  #位置传参＋关键字传参,encoding之前省略了bufgfering=-1，位置不是第三所以用关键字传参
print(type(f))

# 读取文件 - read()
print(f"读取8个字节的结果：{f.read(8)}")
print(f"read方法读取全部内容的结果：{f.read()}") #如果调用多次read，下一个read会在上一个read读取的内容后面继续读取

# 读取文件 - readLines()
lines = f.readlines()  # 读取文件的全部行，封装到列表中
print(f"line对象的类型是：{type(lines)}")
print(f"lines对象的内容是：{lines}")

# 读取文件 - readLine()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")

# for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")

# 文件的关闭
f.close()
time.sleep(500000)

# with open 语法操作打开文件，可以自动关闭
with open("E:/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

time.sleep(500000)