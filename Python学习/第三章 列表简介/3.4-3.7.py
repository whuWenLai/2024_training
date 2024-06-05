#3.4
dinner_users=["ting","xu","ye","an"]
for i in dinner_users:
    print(f"欢迎参加：{i}")

#3.5
print(f"无法参加：{dinner_users[0]}")
dinner_users[0]="ying"
for i in dinner_users:
    print(f"欢迎参加：{i}")

#3.6
print("找到大餐桌啦！")
dinner_users.insert(0,"ting")
dinner_users.insert(2,"hua")
dinner_users.append("meng")
for i in dinner_users:
    print(f"欢迎参加：{i}")

#3.7
print("只能邀请两位：")
for i in range(0,len(dinner_users)-2):
    print(f"sorry,{dinner_users.pop(0)}you can't come")
for i in dinner_users:
    print(f"{i}you stay!")

del dinner_users[0]
del dinner_users[0]
print(dinner_users)