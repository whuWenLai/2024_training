message=""
user=[]

#1.
print("输入quit退出！")
while message!='quit':
    message=input("喜欢的女孩:")
    user.append(message)

#2.
active=True
while active:
    message=input("喜欢的女孩:")
    if message=='quit':
        active=False
    user.append(message)
#3.

while True:
    message=input("喜欢的女孩:")
    if message=='quit':
        break
    user.append(message)