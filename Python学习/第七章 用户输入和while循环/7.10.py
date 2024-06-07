responses=[]
print("这是一份调查：")
while True:
    response={}
    name=input("what is your name?\n")
    response['name']=name
    place=input("if you could visit one place in the world ,where would you go?\n")
    response['place']=place
    responses.append(response)
    flag=input("any one?(yes/no)")
    if flag=='no':
        break

print(responses)