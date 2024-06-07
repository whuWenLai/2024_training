print("买票啦！")

while True:
    age=int(input("你家孩子多大："))
    if age<3:
        print("免费！")
    elif age<12:
        print("10美刀")
    else:
        print("15美刀")