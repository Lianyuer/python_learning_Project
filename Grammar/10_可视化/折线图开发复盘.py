import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, ToolboxOpts

# 处理数据
f_us = open("D:/美国.txt", "r", encoding="UTF-8")
f_jp = open("D:/日本.txt", "r", encoding="UTF-8")
f_in = open("D:/印度.txt", "r", encoding="UTF-8")
f_us_data = f_us.read()
f_jp_data = f_jp.read()
f_in_data = f_in.read()
# 去掉不合JSON规范的开头
f_us_data = f_us_data.strip("jsonp_1629344292311_69436(")
f_jp_data = f_jp_data.strip("jsonp_1629350871167_29498(")
f_in_data = f_in_data.strip("jsonp_1629350745930_63180(")
# 去掉不合JSON规范的结尾
f_us_data = f_us_data[:-2]
f_jp_data = f_jp_data[:-2]
f_in_data = f_in_data[:-2]
# JSON转Python字典
us_dict = json.loads(f_us_data)
jp_dict = json.loads(f_jp_data)
in_dict = json.loads(f_in_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][0: 314]
jp_x_data = jp_trend_data['updateDate'][0: 314]
in_x_data = in_trend_data['updateDate'][0: 314]
# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][1]['data'][0:314]
jp_y_data = jp_trend_data['list'][1]['data'][0:314]
in_y_data = in_trend_data['list'][1]['data'][0:314]

# 生成图表
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data)
# 添加y轴数据
line.add_yaxis("美国新冠治愈人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本新冠治愈人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度新冠治愈人数", in_y_data, label_opts=LabelOpts(is_show=False))
# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts("2020年美日印三国新冠治愈人数折线对比图", pos_left="center", pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(pos_left="80%")
)
# 调用render方法，生成图表
line.render()
# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()
