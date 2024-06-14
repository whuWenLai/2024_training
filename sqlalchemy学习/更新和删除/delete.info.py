from sqlalchemy学习.创建表和增加记录.create_new_table import user, conn
#删除操作

#1.删除所有
delete_query=user.delete()
conn.execute(delete_query)
conn.commit()

#2.删除指定条件记录
delete_query=user.delete().where(user.c.id==3)
conn.execute(delete_query)
conn.commit()