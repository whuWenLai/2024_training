from sqlalchemy学习.创建表和增加记录.create_new_table import user, conn
#更新操作

#1.更新所有
update_query=user.update().values(name='tingting')
conn.execute(update_query)
conn.commit()

#2.更新指定条件记录
update_query=user.update().values(name='tingting').where(user.c.id==3)
conn.execute(update_query)
conn.commit()