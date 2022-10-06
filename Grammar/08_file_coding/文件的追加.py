# 打开文件，不存在的文件, r, w, a
f = open("E:/word.txt", "a", encoding="UTF-8")
# write
f.write("Hello World!!!")  #将内容写入到内存中
# flush刷新
f.flush()
# close关闭
f.close()  #close方法内置了flush的功能


# 打开一个存在的文件，w会把存在的内容清空然后写
f = open("E:word.txt", "a", encoding="UTF-8")
# write写入、flush刷新
f.write("\n浙江农林大学")
# close关闭
f.close()