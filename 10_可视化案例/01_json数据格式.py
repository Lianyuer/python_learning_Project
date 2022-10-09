"""
    Json---不同语言中传输数据的一种中转数据格式
    ·{"name":"admin", "age":18} ------字典
    ·[{"name":"admin", "age":18},{"name":"root", "age":16},{"name":"张三", "age":20}] ------列表嵌套字典
"""

import json
# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name": "张三", "age": 15}, {"name": "王五", "age": 16}, {"name": "赵四", "age": 17}]
json_str = json.dumps(data, ensure_ascii=False)  # 通过 json.dumps(data) 把python数据转化为json数据
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为JSON
d = {"name": "周杰伦", "addr": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将JSON字符串转换为Python数据类型[{k: v, k: v}, {k: v, k: v}]
s = '[{"name": "张三", "age": 15}, {"name": "王五", "age": 16}, {"name": "赵四", "age": 17}]'
l = json.loads(s)
print(type(l))
print(l)

# 将JSON字符串转换为Python数据类型{k: v, k: v}
s = '{"name": "周杰伦", "addr": "台北"}'
d = json.loads(s)
print(type(d))
print(d)
