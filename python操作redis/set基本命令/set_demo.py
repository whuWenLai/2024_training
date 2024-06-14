import redis
#连接redis
pool = redis.ConnectionPool(host='localhost',password=123456,port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

#1.sadd(name,values)新增
r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素


#2.scard(name)获取元素个数 类似于len
print(r.scard("set1"))  # 集合的长度是4

#3.smembers(name)获取集合中所有的成员
print(r.smembers("set1"))   # 获取集合中所有的成员

#4.sdiff(keys, *args)差集
#在第一个name对应的集合中且不在其他name对应的集合的元素集合
r.sadd("set2", 11, 22, 33)
print(r.smembers("set1"))   # 获取集合中所有的成员
print(r.smembers("set2"))
print(r.sdiff("set1", "set2"))   # 在集合set1但是不在集合set2中
print(r.sdiff("set2", "set1"))   # 在集合set2但是不在集合set1中

#5.sdiffstore(dest, keys, *args)差集--差集存在一个新的集合中
r.sdiffstore("set3", "set1", "set2")    # 在集合set1但是不在集合set2中
print(r.smembers("set3"))   # 获取集合3中所有的成员

#6.sinter(keys, *args)交集
print(r.sinter("set1", "set2")) # 取2个集合的交集

#7.sinterstore(dest, keys, *args)交集--交集存在一个新的集合中
print(r.sinterstore("set3", "set1", "set2")) # 取2个集合的交集
print(r.smembers("set3"))

#并集操作:sunion(keys, *args) 并集--并集存在一个新的集合: sunionstore(dest,keys, *args)

#8.sismember(name, value)判断是否是集合的成员 类似in
print(r.sismember("set1", 33))  # 33是集合的成员
print(r.sismember("set1", 23))  # 23不是集合的成员

#9.srem(name, values)删除--指定值删除
print(r.srem("set2", 11))   # 从集合中删除指定值 11
print(r.smembers("set2"))