from datetime import time
import redis
#连接redis
pool = redis.ConnectionPool(host='localhost',password=123456,port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

#1.hset(name, key, value)单个增加--修改(单个取出)--没有就新增，有的话就修改
r.hset("hash1", "k1", "v1")
r.hset("hash1", "k2", "v2")
print(r.hkeys("hash1")) # 取hash中所有的key
print(r.hget("hash1", "k1"))    # 单个取hash的key对应的值
print(r.hmget("hash1", "k1", "k2")) # 多个取hash的key对应的值
r.hsetnx("hash1", "k2", "v3") # 只能新建
print(r.hget("hash1", "k2"))

#2.hmset(name, mapping)批量增加（取出）
print(r.hget("hash2", "k2"))  # 单个取出"hash2"的key-k2对应的value
print(r.hmget("hash2", "k2", "k3"))  # 批量取出"hash2"的key-k2 k3对应的value --方式1
print(r.hmget("hash2", ["k2", "k3"]))  # 批量取出"hash2"的key-k2 k3对应的value --方式2

#3.hgetall(name)取出所有的键值对
print(r.hgetall("hash1"))

#4.hlen(name)得到所有键值对的格式 hash长度
print(r.hlen("hash1"))

#5.hkeys(name)得到所有的keys（类似字典的取所有keys）
print(r.hkeys("hash1"))

#6.hvals(name)得到所有的value（类似字典的取所有value）
print(r.hvals("hash1"))

#7.hdel(name,*keys)删除键值对
print(r.hgetall("hash1"))
r.hset("hash1", "k2", "v222")   # 修改已有的key k2
r.hset("hash1", "k11", "v1")   # 新增键值对 k11
r.hdel("hash1", "k1")    # 删除一个键值对
print(r.hgetall("hash1"))

