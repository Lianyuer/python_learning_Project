from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 基本地图对象
map = Map()
# 准备数据
data = [
    ("北京", 99),
    ("浙江", 199),
    ("江苏", 299),
    ("广东", 399),
    ("深圳", 499),
]
# 添加数据
map.add("测试地图", data, "china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  #是否分段
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"},
        ]
    )
)
# 绘图
map.render()

