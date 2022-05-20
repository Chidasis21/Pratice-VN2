#
price = 50
quantity = 5
if price*quantity < 500:
    print("price*quantity is less than 500")
    print("price = ", price)
    print("quantity = ", quantity)
#
price = 100
if price > 100:
    print("price is greater than 100")
if price == 100:
    print("price is 100")
if price < 100:
    print("price is less than 100")
#
price = 100

if price > 100:
    print("price is greater than 100")
elif price == 100:
    print("price is 100")
elif price < 100:
    print("price is less than 100")
#
x = 1
y = 2.3
z =1j

a = float(x)
b = int(y)
c = complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#
a = 200
b = 30
if b > a:
    print(" b greater then a ")
else:
    print("b is not greater then a")
#
num = float(input("Enter a number"))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
#
a = int(input("Enter a ? "))
b = int(input("Enter b ?"))
c = int(input("Enter c ?"))
if a>b and a>c :
    print(" a is largest ")
if b>a and b>c :
    print(" b is largest ")
if c>a and c>a :
    print(" c is largest ")
#
age = int(input(" Enter your age ? "))
if age >= 18:
    print(" Eligible for Vote ")
else:
    print(" Sorry ! Keep patient ")
#
a = int(input(" Enter number of working days "))
b = int(input(" Total number of days for absent "))

percentage = b*a/100
if percentage <= 75:
    print(" Student allowed to exam ")
else:
    print(" Student not allowed ")
#
a = int(input(" Enter student score "))
if a<=25:
    print("Grade D")
elif a>25 and a<=45:
    print("Grade C")
elif a>45 and a<=50:
    print("Grade B")
elif a>50 and a<=60:
    print("Grade B+")
elif a>60 and a<=80:
    print("Grade A")
else:
    print("Grade A+")
#
salary = int(input(" Enter Employee Salary "))
Timeperiod = int(input(" Enter a number of years "))

Bonus1 = salary*(10/100)
Amount1 = salary+Bonus1
Bonus2 = salary*(8/100)
Amount2 = salary+Bonus2
Bonus3 = salary*(5/100)
Amount3 = salary+Bonus3

if Timeperiod > 10 :
    print(" 10% bonus ", Amount1)
elif Timeperiod >= 6 and Timeperiod <= 10:
    print(" 8% bonus ", Amount2)
elif Timeperiod < 6 :
    print(" 5% bonus ", Amount3)
else:
    print(" Not Paid ")
#
mp= int(input("enter your price"))
if mp > 10000:
    print(" Pay of amount ", mp - mp  * (20/100) )
elif mp >= 7000 and mp <= 10000:
    print(" Pay of amount" , mp - mp * (15/100) )
elif mp <= 7000:
    print(" Pay of amount ", mp - mp * (10/100) )
print(" net amount ")
#
days =  int(input(" enter a number "))
if days <=5 :
    print(" it charges", days*2)
elif days >5  and days <= 10:
    print(" it charges ",days*3)
elif days >11 and days <= 15 :
    print(" it charges ",days*4)
elif days >15:
    print(" it charges ",days*5)