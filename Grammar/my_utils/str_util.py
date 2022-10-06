"""
    字符串处理相关的工具模块
"""


# 创建函数 str_reverse(s)，接收字符串，将字符串反转返回
def str_reverse(s):
    """
    功能：将字符串完成反转
    :param s:将被反转的字符串
    :return: 反转后的字符串
    """
    result = s[::-1]
    return result


# 创建函数 substr(s, x, y)，按照下标 x 和 y，对字符串进行切片
def substr(s, x, y):
    """
    功能：按照给定的下标完成给定字符串的切片
    :param s: 即将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("浙江农林大学"))
    print(substr("浙江农林大学", 1, 3))
