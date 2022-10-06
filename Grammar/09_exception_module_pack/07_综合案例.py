# 创建my_utils 包， 在包内创建：str_util.py 和 file_util.py 2个模块，并提供相应的函数

import Grammar.my_utils.str_util
from Grammar.my_utils import file_util

print(Grammar.my_utils.str_util.str_reverse("浙江农林大学"))
print(Grammar.my_utils.str_util.substr("浙江农林大学", 1, 3))


# file_util.print_file_info("E:/test.txt")
file_util.append_to_file("E:/test.txt", "省重点建设高校")
file_util.print_file_info("E:/test.txt")
