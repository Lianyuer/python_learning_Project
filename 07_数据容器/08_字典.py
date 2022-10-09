# 字典
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}

# 定义空字典
my_dict2 = {}
my_dict3 = ()
print(f"字典1的内容是：{my_dict1}")
print(f"字典2的内容是：{my_dict2}")
print(f"字典3的内容是：{my_dict3}")

# 定义重复Key的字典
my_dict = {"王力宏": 99, "王力宏": 88, "林俊杰": 77}
print(f"重复Key的字典的内容是：{my_dict}")

# 从字典中基于Key获取Value
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
score = my_dict1["王力宏"]
print(f"王力宏的考试分数是：{score}")

# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "语文":87,
        "数学":89,
        "英语":78
    }, "周杰伦": {
        "语文":89,
        "数学":87,
        "英语":88
    }, "林俊杰": {
        "语文":66,
        "数学":78,
        "英语":90
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
# 看一下周杰伦的语文信息
score = stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文分数是：{score}")