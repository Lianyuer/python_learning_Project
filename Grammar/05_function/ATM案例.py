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
name = input("你的姓名是：")
# 定义查询余额函数
def query():
    print("--------------------查询余额---------------------")
    print(f"{name}您好，您的银行卡还有{money}元")
    return menu()
# 定义存款函数
def cunkuan(In):
    global money
    In = int(In)
    money += In
    print("--------------------存款---------------------")
    print(f"{In}元存入成功")
    print(f"你的余额还有{money}")
    return menu()
# 定义取款函数
def qukuan(out):
    global money
    print("--------------------取款---------------------")
    out = int(out)
    money -= out
    if money >= out:
        print("取款成功")
    else:
        print("取款失败")
    print(f"你的余额还有{money}")
    return menu()
# 定义主菜单函数
def menu():
    print("--------------------主菜单--------------------")
    print("您好，欢迎来到天地银行ATM机。")
    print("查询余额【输入1】")
    print("存款【输入2】")
    print("取款【输入3】")
    print("退出【输入4】")
    select = int(input(f"{name}，请输入您的选择："))
    if select == 1:
        query()
    elif select == 2:
        In = input("请输入您要存入的金额数：")
        cunkuan(In)
    elif select == 3:
        out = input("请输入您要存入的金额数：")
        qukuan(out)
    else:
        quit()

menu()
