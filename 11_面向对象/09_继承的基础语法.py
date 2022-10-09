"""
继承的语法：
        class 类名(父类名):
            类内容体
"""


# 演示单继承
class Phone:
    IMEI = None  # 序列号
    producer = "ZAFU"  # 厂商

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"  # 面部识别ID

    def call_by_5g(self):
        print("2022新功能：5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "A&F"

    def read_card(self):
        print("NFC读卡...")

    def write_card(self):
        print("NFC写卡...")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

# 演示多继承下，父类成员名一致的场景：按照最左边的参数来
print(phone.producer)
