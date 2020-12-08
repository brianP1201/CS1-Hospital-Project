class Appointment:

    def __init__(self, time, year, month, week, day):
        self.time = time
        self.year = year
        self.set_month(month)
        self.week = week
        self.set_day(day)

    def get_time(self):
        return self.time
    
    def get_year(self):
        return self.year
    
    def set_month(self, month):
        switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
        self.month = switcher.get(month)
    
    def get_month(self):
        return self.month
    
    def get_week(self):
        return self.week
    
    def set_day(self, day):
        switcher = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
        self.day = switcher.get(day)
    def get_day(self):
        return self.day
    
    def __eq__(self, other_appointment):
        invalid = 0

        if(other_appointment.get_year() == self.year):
            invalid += 1
            if(other_appointment.get_month() == self.month):
                invalid += 1
            if(other_appointment.get_week() == self.week):
                invalid += 1
            if(other_appointment.get_day() == self.day):
                invalid += 1
            if(other_appointment.get_time() == self.time):
                invalid += 1
        if invalid < 5:
            return False
        else:
            return True
    def __str__(self):
       return "Appointment scheduled at: " + self.time + " on " + self.day +" Week " + str(self.week) + " in " + self.month + " " + str(self.year)

