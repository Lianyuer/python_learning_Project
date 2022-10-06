"""
    函数嵌套执行流程：
    函数A中执行到调用函数B的语句，会将函数B全部执行完成后，继续执行函数A的剩余内容
"""
# 定义函数func_b
def func_b():
    print("---2---")
# 定义函数func_a，并在内部调用func_b
def func_a():
    print("---1---")
    # 调用函数func_b
    func_b()

    print("---3---")

# 调用函数func_a
func_a()