import random

class Person:
    
    
    def __init__(self, name, age, gender):
        self.id = ""
        self.role = "User"
        self.name = name
        self.age = age
        self.gender = gender

        for i in range(6):
            random.seed()
            x = random.randrange(10)
            self.id += str(x)

    def get_id(self):
        return self.id
    
    def get_role(self):
        return self.role
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender

    def __str__(self):
        return "Name: " + self.get_name() + "\nHospital ID: " + self.get_id() + "\nAge: " + self.get_age() + "\nGender: " + self.get_gender()

      
  