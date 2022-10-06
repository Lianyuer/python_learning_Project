"""
    发工资案例
"""
import random
#账户余额10000元
balance = 10000
#外层循环给20个员工发工资
for i in range(1, 21):
    perfomance = random.randint(1, 10)
    if perfomance >= 5:
        balance -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{balance}元,")
    else:
        print(f"员工{i}，绩效分{perfomance}，低于5分，不发工资，下一位")
        continue
    if balance == 0:
        print("工资发完了，下个月再领取吧")
        break