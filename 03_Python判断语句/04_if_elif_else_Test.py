"""
    ①03_Python判断语句                     满足①将不会理会②和③
    ②elif                   满足②，将不会理会③（上一个elif满足后，后面的就不会判断了）
    ③elif                   ①②③均不满足，进入else
    ④else                   else也可以省略不写，效果等同于3个独立的if判断
"""

#案例：猜猜心里数字
num = 10
if int(input("请猜想一个数字：")) == num:
    print("恭喜你第一次就猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，最后再猜一次：")) == num:
    print("恭喜你，最后一次猜对了")
else:
    print("很遗憾，你全部猜错了")