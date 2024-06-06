current_users=["admin","jack","rose","ting","wenlai"]
new_users=["newadmin","JACK","rosenew","newting","WenLai"]

current_users_new=[]
for user in current_users:
    current_users_new.append(user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_new:
        print(f"{new_user} 你重名啦！")