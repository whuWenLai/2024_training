users=["admin","jack","rose","ting","wenlai"]
if users:
    for user in users:
        if user == "admin":
            print("hello admin,你好帅管理员")
        else:
            print(f"hello {user},你个普通用户")
else:
    print("我们需要用户！")