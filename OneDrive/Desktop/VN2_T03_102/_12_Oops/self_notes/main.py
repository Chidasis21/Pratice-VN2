class leapyear:
    def __init__(self,year):
        self.year = year
    def check_leap_year(self):
        if self.year % 4 == 0 and self.year % 100 != 0:
            print(self.year, "It is a leap year")
        elif self.year % 100 != 0:
            print(self.year, "It is not a leap year")
        elif self.year % 400 == 0:
            print(self.year, " It is a leap year")
        else:
            print(self.year, "It is not leap year")
y1 = leapyear(2001)
y1.check_leap_year()