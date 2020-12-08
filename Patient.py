import random
from Person import Person
from datetime import datetime
from Appointment import Appointment

class Patient(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.role = "Patient"
        self.id = ""
        for i in range(6):
            random.seed()
            x = random.randrange(10)
            self.id += str(x)
    def request_appointment(self):
        time = input("What time would you like to schedule your appointment? (Ex: 2:00 PM)")

        year = int(input("What year do you want your appointment to take place?"))
        while (year < datetime.now().year) or (not isinstance(year, int)):
            year = int(input("Invalid year. Please enter a valid year during " + str(datetime.now().year) + " or any year after." ))

        month = int(input("What month do you want your appointment to take place? Ex: 1 - Jan, 2 - Feb, etc."))
        while(month < 1 or month > 12) or (not isinstance(month, int)):
            month = int(input("Invalid month. Please enter a valid month, with the number corresponding with the correct month."))
            
        week = int(input("What week of the month do you want your appointment to take place? 1, 2, 3, or 4?"))
        while(week < 1 or week > 4) or (not isinstance(week, int)):
            week = int(input("Invalid week. Please enter a valid week with the number 1, 2, 3, or 4."))

        day = int(input("What day of the week do you want to schedule your appointment? Ex: 1 - Sun, 2 - Mon, etc."))
        while(day < 1 or day > 7) or (not isinstance(day, int)):
            day = int(input("Invalid day. Please enter a valid day with a number 1-7, corresponding to the day of the week."))
        
        newAppt = Appointment(time, year, month, week, day)
        print(newAppt)
        return newAppt
        


        
