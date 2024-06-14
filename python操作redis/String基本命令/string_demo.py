from datetime import time

import redis
#连接redis
pool = redis.ConnectionPool(host='localhost',password=123456,port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
'''
set(name, value, ex=None, px=None, nx=False, xx=False)
在 Redis 中设置值，默认，不存在则创建，存在则修改。
参数：
ex - 过期时间（秒）
px - 过期时间（毫秒）
nx - 如果设置为True，则只有name不存在时，当前set操作才执行
xx - 如果设置为True，则只有name存在时，当前set操作才执行
'''
#1.ex - 过期时间（秒） 这里过期时间是8秒，3秒后p，键food的值就变成None
r.set('food', 'mutton', ex=8)    # key是"food" value是"mutton" 将键值对存入redis缓存
print(r.get('food'))  # mutton 取出键food对应的值

#2.px - 过期时间（豪秒） 这里过期时间是3豪秒，3毫秒后，键foo的值就变成None
r.set('food2', 'beef', px=3)
print(r.get('food2'))

#3.nx - 如果设置为True，则只有name不存在时，当前set操作才执行 （新建）
print(r.set('fruit', 'watermelon', nx=True))    # True--不存在
# 如果键fruit不存在，那么输出是True；如果键fruit已经存在，输出是None

#4.xx - 如果设置为True，则只有name存在时，当前set操作才执行 （修改）
print((r.set('fruit', 'watermelon', xx=True)))   # True--已经存在
# 如果键fruit已经存在，那么输出是True；如果键fruit不存在，输出是None

#5.setnx(name, value)设置值，只有name不存在时，执行设置操作（添加）
print(r.setnx('fruit1', 'banana'))  # fruit1不存在，输出为True

#6.setex(name, time, value)time - 过期时间（数字秒 或 timedelta对象）
r.setex("fruit2", 5, "orange")
time.sleep(5)
print(r.get('fruit2'))  # 5秒后，取值就从orange变成None

#7.mset(*args, **kwargs)批量设置值
r.mget({'k1': 'v1', 'k2': 'v2'})
r.mset(k1="v1", k2="v2") # 这里k1 和k2 不能带引号，一次设置多个键值对
print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
print(r.mget("k1"))

#8.getset(name, value)
print(r.getset("food", "barbecue"))  # 设置的新值是barbecue 设置前的值是beef
