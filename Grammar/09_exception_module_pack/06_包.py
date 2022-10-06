# 创建一个包
# 导入自定义的包中的模块，并使用
import Grammar.my_package.my_module1
import Grammar.my_package.my_module2

Grammar.my_package.my_module1.info_print1()
Grammar.my_package.my_module1.info_print2()
# ----------------------------------------------
from Grammar.my_package import my_module1
from Grammar.my_package import my_module2

my_module1.info_print1()
my_module1.info_print2()

# ----------------------------------------------
from Grammar.my_package.my_module1 import info_print1
from Grammar.my_package.my_module2 import info_print2

info_print1()
info_print2()

# 通过__all__变量，控制import *
from Grammar.my_package import *
my_module1.info_print1()
my_module2.info_print2()


