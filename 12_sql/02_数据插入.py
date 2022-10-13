from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",  # 主机名
    port=3306,         # 端口
    user="root",       # 账户
    password="123456", # 密码
    autocommit=True    # 设置自动提交事务
)
# print(conn.get_server_info)
# 执行非查询性质SQL
cursor = conn.cursor()  # 获取游标对象
# 选择数据库
conn.select_db("school")
# 执行sql
cursor.execute("insert into student values(10012, '李荣浩', 38, '男');")
# # 通过commit确认
# conn.commit()
# 关闭链接
cursor.close()
