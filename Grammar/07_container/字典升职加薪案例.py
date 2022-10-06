info_dict = {
    "王力宏": {
            "部门": "科技部",
            "工资": 3000,
            "级别": 1,
    }, "周杰伦": {
            "部门": "市场部",
            "工资": 5000,
            "级别": 2,
    }, "林俊杰": {
            "部门": "市场部",
            "工资": 7000,
            "级别": 3,
    }, "张学友": {
            "部门": "科技部",
            "工资": 4000,
            "级别": 1,
    }, "刘德华": {
            "部门": "市场部",
            "工资": 6000,
            "级别": 2,
    }
}
print(f"员工在升职加薪之前的结果：{info_dict}")
for name in info_dict:
    # if条件判断符合条件员工
    if info_dict[name]["级别"] == 1:
        # 升职加薪操作
        # 获取员工的信息字典
        employee_info_dict = info_dict[name]
        # 修改员工信息
        employee_info_dict["级别"] = 2   #级别＋1
        employee_info_dict["工资"] += 1000  # 工资＋1000
        # 将员工的信息更新回info_dict
        info_dict[name] = employee_info_dict


print(f"对员工进行升职加薪的结果是：{info_dict}")
