my_foods=['pizza',"falafel","carrot cake"]
friend_foods=my_foods[:]
my_foods.append("rice")
friend_foods.append("big rice")

print("my foods are:")
for food in my_foods:
    print(food,end="\t")

print()
print("friend foods are:")
for food in friend_foods:
    print(food,end="\t")