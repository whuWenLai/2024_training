import sqlalchemy
from sqlalchemy学习.创建表和增加记录.create_new_table import user

engine = sqlalchemy.create_engine('mysql://root:123456@localhost/kitchen-admin')
conn = engine.connect()


user_insert=user.insert()

#插入一条记录
user_demo=user_insert.values(name='wenlai',email='111@qq.com')
conn.execute(user_demo)
conn.commit()

#插入多条记录
conn.execute(user_insert,[
    {'name':'xu','email':'222@qq.com'},
    {'name':'ting','email':'333@qq.com'},
    {'name':'ye','email':'555@qq.com'},
])
conn.commit()