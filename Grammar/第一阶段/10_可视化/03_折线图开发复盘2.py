import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, ToolboxOpts
# 处理数据
f_in = open("D:/印度.txt", "r", encoding="UTF-8")
f_in_data = f_in.read()
# 去掉JSON开头多余的字符串
f_in_data = f_in_data.strip("jsonp_1629350745930_63180(")
# 去掉JSON结尾多余的字符串
f_in_data = f_in_data[:-2]
# JSON转Python字典
in_dict = json.loads(f_in_data)
# 取trend_key
trend_data = in_dict['data'][0]['trend']
# 取2020年日期数据（下标到269）
in_x_data = trend_data['updateDate'][0:269]
# 取印度2020年确诊人数数据（下标到269）
in_y_quezhen_data = trend_data['list'][0]['data'][0:269]
# 取印度2020年治愈人数数据（下标到269）
in_y_cure_data = trend_data['list'][1]['data'][0:269]
# 取印度2020年治愈人数数据（下标到269）
in_y_death_data = trend_data['list'][2]['data'][0:269]
# 取印度2020年治愈人数数据（下标到269）
in_y_xinzengqz_data = trend_data['list'][3]['data'][0:269]
# 生成图表
line = Line()
# 添加x轴数据
line.add_xaxis(in_x_data)
# 添加y轴数据
line.add_yaxis("印度确诊人数", in_y_quezhen_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度治愈人数", in_y_cure_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度死亡人数", in_y_death_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度新增确诊人数", in_y_xinzengqz_data, label_opts=LabelOpts(is_show=False))
# 全局选娘配置
line.set_global_opts(
    title_opts=TitleOpts("2020年印度新冠确诊，治愈，死亡新增确诊人数对比", pos_left="center", pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True)
)
# 使用render函数绘制图像
line.render()
# 关闭文件
f_in.close()