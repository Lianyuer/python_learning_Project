"""
    要求：
    程序启动后要求输入客户姓名
    查询余额、存款、取款后都会返回主菜单
    存款、取款后，都应显示一下当前余额
    客户选择退出或者说输入错误，程序会退出，否则一直执行
"""
# 记录银行卡余额
money = 5000000
# 记录客户姓名（启动程序时输入）
name = None

name = input("请输入您的姓名：")


# 定义查询余额函数
def query(show_header):
    if show_header:
        print("--------------------查询余额---------------------")
    print(f"{name}您好，您的银行卡还有{money}元")


# 定义存款函数
def saving(num):
    global money
    money += num
    print("--------------------存款---------------------")
    print(f"{name}，您好，您存款{num}元成功")

    # 调用query函数查询余额
    query(False)


# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("--------------------取款---------------------")
    print(f"{name}，您好，您取款{num}元成功")

    # 调用query函数查询余额
    query(False)



# 定义主菜单函数
def main():
    print("--------------------主菜单--------------------")
    print(f"您好，{name}，欢迎来到天地银行ATM机。")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    return input("请输入您的选择：")


# 设置无限循环，确保程序不退出
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue    # 通过continue继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("程序退出啦")
        break    # 通过break退出循环