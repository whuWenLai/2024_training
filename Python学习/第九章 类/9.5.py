class User:
    def __init__(self, name, age, sex):
        self.first_name = name[0]
        self.last_name = name[1]
        self.age = age
        self.sex=sex
        self.login_attempts = 0
    def describe_user(self):
        print(f"im {self.first_name} {self.last_name} and {self.age} years old,last im {self.sex}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1=User(['lai','dog'],22,'man')
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
