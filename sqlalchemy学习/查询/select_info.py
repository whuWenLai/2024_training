from sqlalchemy import or_, and_

from sqlalchemy学习.创建表和增加记录.create_new_table import user, engine

conn=engine.connect()

#拿到所有数据
query=user.select()
result=conn.execute(query)

#1.拿到第一个数据
row=result.fetchone()

#2.结果转换为列表
relist=result.fetchall()

#3.条件查询
query=user.select().where(user.c.id==1)
result=conn.execute(query)

# and 和 or
query=user.select().where(
    or_(
        user.c.id==1,
        and_(
            user.c.name=='ting',
            user.c.id==3,
        )
    )
)
result=conn.execute(query)



