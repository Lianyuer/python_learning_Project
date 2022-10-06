# 导入自定义模块使用
# import my_module1
# my_module1.test(1, 2)
# from my_module1 import test
# test(1, 2)

# 导入不同模块的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1, 2)

# __main__变量
# from my_module1 import test

# __all__变量
# from my_module1 import *
# test_a(1, 2)
# test_b(2, 1)


"""
my_module1.py
# __all__ = ['test_a']
#
#
# def test_a(a, b):
#     print(a + b)
#
#
# def test_b(a, b):
#     print(a - b)

my_module2.py
# def test(a, b):
#     print(a - b)
"""