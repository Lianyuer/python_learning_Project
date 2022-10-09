"""
    lambda是关键字，表示定义匿名函数
    传入参数表示匿名函数的形式参数
    函数体，就是函数的执行逻辑，注意：只能写一行，无法写多行代码
"""
# 定义一个函数，接收其他函数输入
def test_func(compute):
    result = compute(1, 2)
    print(f"结果是：{result}")
# 通过lambda匿名函数的形式，将匿名函数作为参数输入
test_func(lambda x, y: x + y)

# def compute(x, y):
#     return x + y
# test_func(compute)