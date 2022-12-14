"""
    是否支持下标索引
    ·支持：列表、元组、字符串 - 序列类型
    ·不支持：集合、字典 - 非序列类型
    --------------------------------
    是否支持重复元素
    ·支持：列表、元组、字符串 - 序列类型
    ·不支持：集合、字典 - 非序列类型
    --------------------------------
    是否支持修改
    ·支持：列表、集合、字典
    ·不支持：元组、字符串
"""

"""
                 列表        元组         字符串         集合          字典 
    元素数量     支持多个     支持多个      支持多个       支持多个       支持多个
    元素类型     任意        任意          仅字符        任意          Key:Value Key:除字典外任意类型 Value:任意类型
    重复元素     支持        支持          支持          不支持        不支持
    可修改性     支持        不支持        不支持         支持          支持
    数据有序     支持        不支持        不支持         支持          支持
"""

"""
    使用场景：   列表：一批数据，可修改、可重复的存储场景
               元组：一批数据，不可修改、可重复的场景
               字符串：一串字符串的存储场景
               集合：一批数据，去重存储场景
               字典：一批数据，可用Key检索Value的存储场景
"""