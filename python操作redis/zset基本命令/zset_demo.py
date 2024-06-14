from datetime import time
import redis
#连接redis
pool = redis.ConnectionPool(host='localhost',password=123456,port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

#1.zadd(name, *args, **kwargs)新增

r.zadd("zset1",{ 'n1':11, 'n2':22})
r.zadd("zset2", {'m1': 22, 'm2':44})
print(r.zcard("zset1")) # 集合长度
print(r.zcard("zset2")) # 集合长度
print(r.zrange("zset1", 0, -1))   # 获取有序集合中所有元素
print(r.zrange("zset2", 0, -1, withscores=True))   # 获取有序集合中所有元素和分数

#2.zcard(name).获取有序集合元素个数 类似于len
print(r.zcard("zset1")) # 集合长度

#3.r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)获取有序集合的所有元素
print(r.zrevrange("zset1", 0, -1))    # 只获取元素，不显示分数
print(r.zrevrange("zset1", 0, -1, withscores=True)) # 获取有序集合中所有元素和分数,分数倒序

for i in range(1, 30):
    element = 'n' + str(i)
    r.zadd("zset3", element, i)
print(r.zrangebyscore("zset3", 15, 25)) # # 在分数是15-25之间，取出符合条件的元素
print(r.zrangebyscore("zset3", 12, 22, withscores=True))    # 在分数是12-22之间，取出符合条件的元素（带分数）

#按照分数范围获取有序集合的元素并排序（默认从大到小排序）
print(r.zrevrangebyscore("zset3", 22, 11, withscores=True)) # 在分数是22-11之间，取出符合条件的元素 按照

#获取所有元素--默认按照分数顺序排序
print(r.zscan("zset3"))

#4.zcount(name, min, max)获取name对应的有序集合中分数 在 [min,max] 之间的个数
print(r.zrange("zset3", 0, -1, withscores=True))
print(r.zcount("zset3", 11, 22))

#5.zincrby(name, value, amount)自增
r.zincrby("zset3", "n2", amount=2)    # 每次将n2的分数自增2
print(r.zrange("zset3", 0, -1, withscores=True))

#6.zrank(name, value)获取值的索引号
print(r.zrank("zset3", "n1"))   # n1的索引号是0 这里按照分数顺序（从小到大）
print(r.zrank("zset3", "n6"))   # n6的索引号是1

print(r.zrevrank("zset3", "n1"))    # n1的索引号是29 这里安照分数倒序（从大到小）

#7.zrem(name, values).删除--指定值删除
r.zrem("zset3", "n3")   # 删除有序集合中的元素n3 删除单个
print(r.zrange("zset3", 0, -1))

#8.zremrangebyrank(name, min, max)删除--根据排行范围删除，按照索引号来删除
r.zremrangebyrank("zset3", 0, 1)  # 删除有序集合中的索引号是0, 1的元素
print(r.zrange("zset3", 0, -1))

#9.zremrangebyscore(name, min, max).删除--根据分数范围删除
r.zremrangebyscore("zset3", 11, 22)   # 删除有序集合中的分数是11-22的元素
print(r.zrange("zset3", 0, -1))

#10.zscore(name, value)获取值对应的分数
print(r.zscore("zset3", "n27"))   # 获取元素n27对应的分数27