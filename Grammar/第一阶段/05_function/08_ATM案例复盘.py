"""
    要求：
    程序启动后要求输入客户姓名
    查询余额、存款、取款后都会返回主菜单
    存款、取款后，都应显示一下当前余额
    客户选择退出或者说输入错误，程序会退出，否则一直执行
"""

money = 5000000
name = input("请输入你的姓名：")
show_header = True

def query(show_header):
    if show_header:
        print("-------------查询余额---------------")
    print(f"{name}您好，您的余额剩余{money}元")

def saving(num):
    print("-------------存款---------------")
    global money
    money += num
    print(f"{name}您好，您的{num}元存入成功")

    query(False)


def get_money(sum):
    print("-------------存款---------------")
    global money
    if money > sum:
        money -= sum
        print(f"{name}您好，您的{sum}元取出成功")
    else:
        print(f"{name}您好，余额不足，您的{sum}元取出失败")

    query(False)


def main():
    print("-------------主菜单---------------")
    print("查询余额【输入1】")
    print("存款【输入2】")
    print("取款【输入3】")
    print("退出【输入4】")

    return input(f"{name}您好，欢迎来到天地银行ATM机，请进行您的选择：")

while True:
    select = main()
    if select == "1":
        query(True)
    elif select == "2":
        saving(int(input("请输入您要存入的金额")))
    elif select == "3":
        get_money(int(input("请输入您要取出的金额")))
    else:
        print("程序退出啦")
        break

