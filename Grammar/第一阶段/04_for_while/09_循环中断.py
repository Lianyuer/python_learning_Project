"""
    continue的作用：
    中断所在循环的当次执行，直接进入下一次

    break的作用：
    直接结束所在的循环
    
     ** continue和break在for和while中的作用一致
        在嵌套循环中，只能作用在所在的循环上，无法对上层循环起作用
"""
# 演示循环中断语句 continue
# for i in range(1, 6):
#     print("语句1")
#     continue
#     print("语句2")

#演示continue的嵌套应用
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#
#     print("语句4")

# 演示循环中断语句 break
# for i in range(1, 101):
#     print("语句1")
#     break
#     print("语句2")
#
# print("语句3")

#演示break的嵌套应用
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        break
        print("语句3")

    print("语句4")