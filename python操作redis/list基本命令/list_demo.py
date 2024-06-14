from datetime import time

import redis
#连接redis
pool = redis.ConnectionPool(host='localhost',password=123456,port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

#1.lpush(name,values) r.rpush(name,values)增加（--没有就新建
r.lpush("list1", 11, 22, 33)#类似于list的append，只是这里是从左边新增加）
print(r.lrange('list1', 0, -1))

r.rpush("list2", 11, 22, 33)  # 表示从右向左操作
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, 3))  # 切片取出值，范围是索引号0-3

#2.linsert(name, where, refvalue, value))新增（固定索引号位置插入元素）
r.linsert("list2", "before", "11", "00")   # 往列表中左边第一个出现的元素"11"前插入元素"00"
print(r.lrange("list2", 0, -1))   # 切片取出值，范围是索引号0-最后一个元素

#3.r.lset(name, index, value)修改（指定索引号进行修改）
r.lset("list2", 0, -11)    # 把索引号是0的元素修改成-11
print(r.lrange("list2", 0, -1))

#4.r.lrem(name, value, num)删除（指定值进行删除）
r.lrem("list2", "11", 1)    # 将列表中左边第一次出现的"11"删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", "99", -1)    # 将列表中右边第一次出现的"99"删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", "22", 0)    # 将列表中所有的"22"删除
print(r.lrange("list2", 0, -1))

#5.lpop(name)删除并返回
r.lpop("list2")    # 删除列表最左边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))
r.rpop("list2")    # 删除列表最右边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))

#6.lindex(name, index)取值（根据索引号取值）
print(r.lindex("list2", 0))  # 取出索引号是0的值

#7.rpoplpush(src, dst)移动 元素从一个列表移动到另外一个列表
r.rpoplpush("list1", "list2")
print(r.lrange("list2", 0, -1))

#8.blpop(keys, timeout)一次移除多个列表
r.lpush("list10", 3, 4, 5)
r.lpush("list11", 3, 4, 5)
while True:
    r.blpop(["list10", "list11"], timeout=2)
    print(r.lrange("list10", 0, -1), r.lrange("list11", 0, -1))