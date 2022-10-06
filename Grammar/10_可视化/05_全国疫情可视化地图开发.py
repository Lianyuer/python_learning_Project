import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

# 读取数据文件
f = open("D:/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部数据
# 关闭文件
f.close()
# 取到各省数据
# 将字符串 json 转换为python的字典
data_dict = json.loads(data)  # 基础数据字典
# 从字典中取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并各个省的人数都封装在列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[

            {"min": 1, "max": 99, "lable": "1~99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999", "color": "#FF9966"},
            {"min": 5000, "max": 6999, "lable": "5000~6999", "color": "#FF6666"},
            {"min": 10000, "max": 89999, "lable": "10000~89999", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#C990033"}
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")
