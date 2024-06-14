import sqlalchemy
from sqlalchemy import Table


engine = sqlalchemy.create_engine('mysql://root:123456@localhost/kitchen-admin')
conn = engine.connect()
metadata = sqlalchemy.MetaData()

user=sqlalchemy.Table(
    'user',metadata,
    sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column('name',sqlalchemy.String(128),nullable=False,unique=True),
    sqlalchemy.Column('email',sqlalchemy.String(128),nullable=False),
)
metadata.create_all(engine)


