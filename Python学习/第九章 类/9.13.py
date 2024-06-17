
from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,self.sides))
mydie1=Die()
print("Throw the dice 10 times")
for i in range(1,11):
    mydie1.roll_die()
mydie2=Die(10)
print("Throw the dice 10 times")
for i in range(1,11):
    mydie2.roll_die()
mydie3=Die(20)
print("Throw the dice 10 times")
for i in range(1,11):
    mydie3.roll_die()