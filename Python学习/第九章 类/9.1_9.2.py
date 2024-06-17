class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('restaurant_name:', self.restaurant_name)
        print('cuisine_type:', self.cuisine_type)
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
#9.1
re1=Restaurant("dog餐厅",'Chinese')
print(f"restaurant_name:{re1.restaurant_name} cuisine_type:{re1.cuisine_type}")
re1.describe_restaurant()
re1.open_restaurant()

#9.2
re2=Restaurant("ting餐厅",'USA')
re3=Restaurant("ye餐厅",'kkk')
re1.describe_restaurant()
re2.describe_restaurant()
re3.describe_restaurant()