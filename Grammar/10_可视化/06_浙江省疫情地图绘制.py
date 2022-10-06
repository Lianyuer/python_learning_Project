import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

# 读取数据文件
f = open("D:/疫情.txt", "r", encoding="UTF-8")
f_data = f.read()
# 关闭文件
f.close()
# 获取浙江省数据
# JSON转换为python字典
f_dict = json.loads(f_data)
# 在各省数据列表遍历取出浙江省数据
# 组装浙江省份name和确诊人数为元组，都封装在列表内
zj_data_list = []
zj_district_confirm_list = []
province_data_list = f_dict["areaTree"][0]["children"]

for province in province_data_list:
    if province["name"] == "浙江":
        zj_data_list = province["children"]
# 取城市名和确诊人数
for cities in zj_data_list:
    city_name = cities["name"]+"市"  # 一定要和地图上的城市名称匹配！！！
    city_confirm = cities["total"]["confirm"]
    zj_district_confirm_list.append((city_name, city_confirm))
# 创建地图对象
map = Map()
# 添加地图数据
map.add("浙江省疫情确诊人数", zj_district_confirm_list, "浙江")
# 全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="浙江省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 0, "max": 29, "label": "0~29", "color": "#CCFFFF"},
            {"min": 30, "max": 59, "label": "30~59", "color": "#FFFF99"},
            {"min": 60, "max": 89, "label": "60~89", "color": "#FF9966"},
            {"min": 90, "max": 150, "label": "90~150", "color": "#FF6666"},
            {"min": 151, "max": 250, "label": "151~250", "color": "#CC3333"},
            {"min": 500, "label": "500+", "color": "#2f455b"},
        ]
    )
)
# 绘图
map.render("浙江省疫情地图.html")
