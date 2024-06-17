from random import choice
class Choice_Str:
    def __init__(self):
        self.str=[]
        self.win_str=[]
        for i in range(1,11):
            self.str.append(i)
        self.str.append('a')
        self.str.append('b')
        self.str.append('c')
        self.str.append('d')
        self.str.append('e')
    def win_lottery_str(self):
        for i in range(4):
            self.win_str.append(choice(self.str))
    def check_lottery(self,check_str):
        for i in range(4):
            if check_str[i]==self.win_str[i]:
                if i==3:
                    return True
            else:
                return False


lottery=Choice_Str()
lottery.win_lottery_str()
print("中奖号码为：",lottery.win_str)
my_ticket=[]

cnt=0
while True:
    cnt=cnt+1
    my_ticket=[]
    for i in range(4):
        my_ticket.append(choice(lottery.str))
    if lottery.check_lottery(my_ticket):
        print(f"中大奖啦，次数为：{cnt}")
        break
