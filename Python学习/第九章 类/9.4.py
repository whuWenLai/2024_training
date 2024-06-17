class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('restaurant_name:', self.restaurant_name)
        print('cuisine_type:', self.cuisine_type)
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, number_served):
        self.number_served += number_served

re1=Restaurant('dogRe','Chinese')
print(re1.number_served)
re1.number_served=10
print(re1.number_served)

re1.set_number_served(15)
print(re1.number_served)

re1.increment_number_served(5)
print(re1.number_served)