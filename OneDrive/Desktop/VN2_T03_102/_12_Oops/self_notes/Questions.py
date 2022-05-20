'''
#1st
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
y1 = leapyear(2004)
y1.check_leap_year()
#2nd
class armstrong:
    def checkarmstrong(self,a):
        digit = len(str(a))
        res = 0
        temp = a
        while a>0:
            rem = a%10
            res = res + (rem ** digit)
            a = int(a/10)
        if res == temp:
            return 1
        else:
            return 0
print("Enter a number :",end="")
num = int(input())

obj = armstrong()
check = obj.checkarmstrong(num)
if check == 1:
    print(num,"It is a armstrong number")
else:
    print(num,"It is not a armstrong number")
#3rd
class calculator():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y
x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
obj = calculator(x,y)
while True:
    def menu():
        z = ('1.Add\n2.Sub\n3.Mul\n4.Div\n0.')
        print(z)
    menu()
    choice = int(input("Select a given number :"))
    if choice == 1:
        print("result:",obj.add())
    elif choice == 2:
        print("result:",obj.sub())
    elif choice == 3:
        print("result:",obj.mul())
    elif choice == 4:
        print("result:",obj.div())
    elif choice == 0:
        print("Use valid Key")
    else:
        print("Invalid input")
print()
# 4th
class R_num:
    def __init__(self, n):
        self.n = n
    def ordinary_num(self):
        if (self.n <= 0):
            print("{} is invalid input:".format(n))
        else:
            while (self.n >= 1000):
                print("M", end="")
                self.n = self.n - 1000
            if (self.n >= 900):
                print("CM", end="")
                self.n = self.n - 900
            if (self.n >= 500):
                print("D", end="")
                self.n = self.n - 500
            if (self.n >= 400):
                print("CD", end="")
                self.n = self.n - 400
            while (self.n >= 100):
                print("C", end="")
                self.n = self.n - 100
            if (self.n >= 90):
                print("XC", end="")
                self.n = self.n - 90
            if (self.n >= 50):
                print("L", end="")
                self.n = self.n - 50
            if (self.n >= 40):
                print("XL", end="")
                self.n = self.n - 40
            while (self.n >= 10):
                print("X", end="")
                self.n = self.n - 10
            if (self.n >= 9):
                print("IX", end="")
                self.n = self.n - 9
            if (self.n >= 5):
                print("V", end="")
                self.n = self.n - 5
            if (self.n >= 4):
                print("IV", end="")
                self.n = self.n - 4
            while (self.n >= 1):
                print("I", end="")
                self.n = self.n - 1
n = int(input("Enter an Ordinary Number:= "))
chida1 = R_num(n)
chida1.ordinary_num()'''
