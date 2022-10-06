"""
    ·读取文件
    ·将文件写出到bill.txt.bak文件作为备份
    ·同时，将文件内标记为测试的数据行丢弃
"""
"""
    实现思路：
    ·open和r模式打开一个文件对象，并读取文件
    ·open和w模式打开另一个文件对象，用于文件写出
    ·for循环内容，判断是否是测试不是测试就write写出，是测试就continue跳过
    将2个文件对象均close()
"""
# 打开文件得到文件对象，准备读取
fr = open("E:/bill.txt", "r", encoding="UTF-8")
# 打开文件得到文件对象，准备写入
fw = open("E:/bill.txt.bak", "w", encoding="UTF-8")
# for循环读取文件
for line in fr:
    line = line.strip()
    # 判断内容，将满足条件的内容写出
    if line.split("，")[4] == "测试":
            continue  # continue进入下一次循环，这一次后面的内容就跳过了
    # 将内容写出去
    fw.write(line)
    # 由于前面对内容进行了strip()操作，所以要手动的写出换行符
    fw.write("\n")
# close2个文件对象
fr.close()
fw.close()