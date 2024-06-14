import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:123456@localhost/kitchen-admin')
conn = engine.connect()

query = sqlalchemy.text('select * from chef')

result = conn.execute(query)

for row in result:
    print(row)

conn.close()
engine.dispose()