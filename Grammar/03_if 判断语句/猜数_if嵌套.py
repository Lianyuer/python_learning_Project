"""
 案例需求：定义一个数字（1~10，随机产生），通过3此判断来猜出数字
"""
import random
num = random.randint(1,10)
guess_num = int(input("请输入你猜测的数字："))

if guess_num == num:
    print("恭喜你，你第一次就猜中了")
else:
    if guess_num > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")

    guess_num = int(input("请再次输入你猜测的数字："))
    if guess_num == num:
        print("恭喜你，你第二次猜中了")
    else:
        if guess_num > num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")

        guess_num = int(input("请第三次输入你猜测的数字："))
        if guess_num == num:
            print("恭喜你，你第三次猜中了")
        else:
            print("三次机会用完了，没有猜中")


