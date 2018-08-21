import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='fbo',passwd='fbo',db='web')
cur = conn.cursor()

sql = """
create table userinfo(
    id int primary key,
    name varchar(32),
    password varchar(32)
)
"""

cur.execute(sql)

conn.commit()

cur.close()
conn.close()