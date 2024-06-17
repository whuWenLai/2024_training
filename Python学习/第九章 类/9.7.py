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

class Admin(User):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex)
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        print('admin‘s privileges:',self.privileges)

admin=Admin(['lai','dog'],22,'man')
admin.show_privileges()