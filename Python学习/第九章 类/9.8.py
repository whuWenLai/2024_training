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

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print(self.privileges)
class Admin(User):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex)
        self.privileges=Privileges()

admin=Admin(['lai','dog'],22,'man')
admin.privileges.show_privileges()