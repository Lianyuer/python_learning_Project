# 设计一个闹钟类
class Clock:
    id = None  # 序列化
    price = None  # 价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "2022109"
clock1.price = 20
print(f"闹钟id：{clock1.id}，价格：{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "2022110"
clock2.price = 50
print(f"闹钟id：{clock2.id}，价格：{clock2.price}")
clock2.ring()
