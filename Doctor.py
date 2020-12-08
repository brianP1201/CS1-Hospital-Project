from Person import Person
import random

class Doctor(Person):
    allAppts = []
    entries = 0
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.role = "Doctor"
        self.id = ""
        for i in range(6):
            random.seed()
            x = random.randrange(10)
            self.id += str(x)
    
    
    def new_appointment(self, new_appt):
        
        if self.entries == 0:
            self.allAppts.append(new_appt)
            self.entries += 1
            print("New appointment added.")
        else:
            for i in range(self.entries):
                if not self.allAppts[i].__eq__(new_appt):
                    self.allAppts.append(new_appt)
                    self.entries += 1
                    print("New appointment added.")
                else:
                    print("This appointment could not be added due to a scheduling conflict.")


