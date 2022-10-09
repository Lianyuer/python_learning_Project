#range 语法1 range(num)
for x in range(10):
    print(x)

#range 语法2 range(num1, num2)
for x in range(5, 10):
    #从5开始不包含10本身的一个数字序列
    print(x)

#range 语法3 range(num1, num2, step)
for x in range(5, 10, 2):
    # 从5开始不包含10本身的一个数字序列,步长为2
    print(x)