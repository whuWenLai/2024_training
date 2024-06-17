class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('restaurant_name:', self.restaurant_name)
        print('cuisine_type:', self.cuisine_type)
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor_type = ['vanilla','chocolate','Strawberry']

    def describe_flavor(self):
        for i in self.flavor_type:
            print(i)

ice=IceCreamStand("IceDog","Chinese")
ice.describe_restaurant()
ice.describe_flavor()