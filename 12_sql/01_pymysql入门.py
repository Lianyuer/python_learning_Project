from  pymysql import Connection

# 构建到MySQL数据库的链接
coon = Connection(
    host="localhost",  # 主机名（IP）
    port=3306,         # 端口
    user="root",       # 账户
    password="123456"  # 密码
)

# print(coon.get_server_info())
# 执行非查询性质SQL
cursor = coon.cursor()     # 获取到游标对象
# 选择数据库
coon.select_db("school")
# 执行sql
# cursor.execute("create table test_pymysql(id int);")

# 执行查询性质SQL
cursor.execute("select * from student")
result = cursor.fetchall()
for row in result:
    print(row)

# 关闭链接
coon.close()