class User:
   def __init__(self, name, age,sex):
       self.first_name = name[0]
       self.last_name = name[1]
       self.age = age
       self.sex=sex
   def describe_user(self):
       print(f"im {self.first_name} {self.last_name} and {self.age} years old,last im {self.sex}")
   def greet_user(self):
       print(f"Hello {self.first_name} {self.last_name}!")


user1=User(['lai','dog'],21,'man')
user2=User(['ting','ye'],20,'woman')
user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()

