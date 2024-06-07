sandwich_orders=['s1','s2','s3']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f"{sandwich}已经做好啦！")
    finished_sandwiches.append(sandwich)
