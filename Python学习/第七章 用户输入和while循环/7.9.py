sandwich_orders=['s1','s2','pastrami','pastrami','pastrami']
finished_sandwiches=[]
print("不好意思，pastrami卖完啦！")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f"{sandwich}已经做好啦！")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)