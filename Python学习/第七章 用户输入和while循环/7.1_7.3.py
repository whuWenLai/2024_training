#1
car=input("你想要什么car?")
print(f"{car}这辆车我们有！")

#2
user=int(input("有多少人来就餐？"))
if user>8:
    print("没有位置啦！")
else:
    print("还有位置！")

#3
number=int(input("请输入一个数："))
if number%10==0:
    print("是十的倍数")
else:
    print("不是十的倍数")