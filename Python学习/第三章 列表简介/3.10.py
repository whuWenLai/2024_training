dinner_users=["ting","xu","ye","an"]

#1.访问列表元素
for i in range(0,len(dinner_users)):
    print(dinner_users[i])

#2.插入
dinner_users.insert(0,"ting")
dinner_users.insert(2,"hua")
dinner_users.append("meng")

#3.删除
del dinner_users[0]
dinner_users.pop(0)
dinner_users.remove("meng")

#4.排序
dinner_users.sort()
dinner_users.sort(reverse=True)

#5.反向
dinner_users.remove()

#6.长度
print(len(dinner_users))