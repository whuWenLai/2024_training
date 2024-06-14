from datetime import time
import redis
#连接redis
pool = redis.ConnectionPool(host='localhost',password=123456,port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

#1.delete(*names)删除
r.delete("gender")  # 删除key为gender的键值对

#2.exists(name)检查名字是否存在
print(r.exists("zset1"))

#3.keys(pattern='')模糊匹配
print(r.keys("foo*"))

#4.expire(name ,time)设置超时时间
r.lpush("list5", 11, 22)
r.expire("list5", time=3)
print(r.lrange("list5", 0, -1))
time.sleep(3)
print(r.lrange("list5", 0, -1))

#5.rename(src, dst)重命名
r.lpush("list5", 11, 22)
r.rename("list5", "list5-1")