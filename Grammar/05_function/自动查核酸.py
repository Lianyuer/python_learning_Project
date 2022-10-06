# def autocheck():
#     print("欢迎光临！")
#     print("请出示您的健康吗以及72小时核酸证明！")
#
# autocheck()

"""
    升级版自动查核酸  定义函数，接受一个体温参数
"""

def autocheck(temperature):
    print("请出示您的健康吗以及72小时核酸证明，并配合测量体温！")
    if temperature <= 37.5:
        print(f"体温测量中，您的体温是：{temperature}度，体温正常请进")
    else:
        print(f"体温测量中，的您体温是：{temperature}度，需要隔离")

autocheck(37.7)
