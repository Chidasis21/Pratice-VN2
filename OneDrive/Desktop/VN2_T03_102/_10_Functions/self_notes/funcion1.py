'''
#1st (Input numbers table)
def table(num):
    for i in range (1,11):
        print(num,'X',i, '=',num * i)
n = int(input("enter a number :"))
table(n)
#2nd  (Sum of 2 number)
def sum(num):
    total = 0
    for number in num:
        total += number
    return total
set1 = {1,2,3,4,6}
print(sum(set1))
#3rd (Multiplication 2 value)
def mullst(num):
    result = 1
    for i in num:
        result = result * i
    return result
lst1 = {2,4,6}
lst2 = {1,3,2}
print(mullst(lst1))
print(mullst(lst2))
#4th (Uppercase and lowercase latter)
def strexmp(x):
    a = {"uppercase":0,"lowercase":0}
    for i in x:
        if i.isupper():
            a["uppercase"]+= 1
        elif i.islower():
            a["lowercase"]+= 1
        else:
            pass
    print("Your string:",x)
    print("no.of uppercase:",a["uppercase"])
    print("no.of lowercase:", a["lowercase"])
strexmp('PahhggjujgjyGFHYKHJJT')
#5th (Unique value find)
def unik(x):
    a = []
    for i in x:
        if i not in a:
            a.append(i)
    return a
print(unik([1,2,3,4,5,5,6,6,6,1]))
#6th (Input is a palindrom or not)
def palindrom(x):
    return x == x[ : : -1]
x = input("Enter a string : ")
x = x.lower()
ans = palindrom(x)
if ans:
    print("Yes It is palindrom")
else:
    print("It is not palindrom")
#7th (Number is in a given range)
n=int(input("enter a number : "))
def str1(n):
    if n in range(1,11):
        print("range of number")
    else:
        print("Number outside the range")
str1(n)
#8th (Sum of 2 number)
def sum(n1,n2):
    sum = n1+n2
    return sum
n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
print("The sum is",sum(n1,n2))
#9th (Even or odd number)
num=int(input("Enter a number : "))
def oddeven(num):
    if(num&1!=1):        #This is a bitwise operator
        print(num,"is even number")
    else:
        print(num,"is odd number")
oddeven(num)
#10th (Factorial Number)
n=int(input("Enter a number : "))
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(n))
#  (Parameter)
def square (num):
    return num*num
number = float(input("Enter a number : "))
square = square(number)
print("The square of the given number {0} = {1}".format(number,square))
#11th  (Pascle number)
n = int(input("Enter a number : "))
list1 = []
for i in range(n):
    temp_list = []
    for j in range [i + 1]:
        if j==0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1]+list1[i-1][j])
    lst1.append(temp_list)

for i in range(n):
    for j in range(n-i-1):
        print(format("","<3"),end="")
    for j in range(i+1):
        print(format(list1[i][j],"<3"),end="")
    print()
#
def my_function():
    print(" Hello! I am Chidasis ")
my_function()
#
def my_function(name):
    print(name + " Chidasis ")
my_function("Email")
my_function("Address")
my_function("Ph no")
#
a = int(input(" Enter 1st number :"))
b = int(input(" Enter 2nd number :"))
def sum(num1,num2):
    sum = num1 + num2
    print(sum)
    return sum
sum(num1,num2)
#
def sum(num1,num2):
    n= (num1+num2)
    return n
print(12+30)
print(14+53)
#
a = int(input(" Enter 1st number :"))
b = int(input(" Enter 2nd number :"))
def sub(a,b):
    sub = a - b
    print(sub)
    return sub
sub(a,b)
#
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

def sum(num1,num2):
    result = num1+num2
    return sum
print(num1+num2)
#
a = 10
b = 20
def sum(a,b):
    result = a + b
    print("Addition of :",result)
a = (10, 20)
b = (20, 30)
#
n1 = 10
n2 = 100
def sum(n1, n2):
    result = n1 + n2
    print("Addition is : ", result)
sum(10, 20)
sum(100, 200)
#function calling
num  = 10
num1 = 11
def sum(num,num1): # Function Defination
    result = num + num1  # Function Body
    print("Addition :",result)
sum(num,num1) # Result
#
num1 = 10
num2 = 20
def sum(num1,num2): #Function Defination
    result = num1 + num2 #Function body
    print("Addition is :",result)
sum(10,20) # Function Aruguments
x = 10
print(x)
print(x + 10)
print(x + 20)
#
n1 = float(input("Enter a number:"))
n2 = float(input("enter a number:"))
def sum(n1,n2):
    result = n1 + n2
    print("Addition of :",result)
sum(n1,n2)
#
#Types of Function
1.Function with parameter, with return type (T , T)
2.Function with parameter, without return type (T , F)
3.Function without parameter, with return type (F , T)
4.Function without parameter, without return type (F , F)
#  1...
num1 = 23
num2 = 25
def sum(num1, num2):
    result = num1 + num2
    return result
print("Addition is :",sum(23,25))
#  2...
num1 = 25
num2 = 30
def sum(num1, num2):
    result = num1 + num2
    print("Addition is :",result)
sum(num1,num2)
print("second add :",sum(100,200))
#  3...
def sum():
    num1 = 55
    num2 = 35
    result = num1 + num2
    return result
addition = sum()
print("Addition of :",addition)
#  4...
def sum():
    num1 = 89
    num2 = 63
    result = num1 + num2
    print("Addition of :",result)
sum()
print("Addition of :",sum)
#
1.Positional arguments(Requred arguments) - (arguments passed to a function with cirrect positional order)
2.Defult arguments - ()
3.Keyword arguments(Named arguments)

#  1....
def sum(a1,a2,a3):
    print("sum :",a1,a2,a3)
    result = a1 + a2 + a3
    print("sum is  :",result)
sum(10,52,52)
#
def person(name,age):
    print(name)
    print(age-2)
person('Rakesh',24)
#  2....
def add(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)
add(10,50,60)
#
def sum(a1,a2,a3 = 100):
    result = a1 + a2 + a3
    print(" sum is :",result)
sum(10,20)
sum(10,20,30)
#  3....
def person(name, **data):
    print(name)
    print(data)
person('Chidasis',age= 24,city= 'Bangalore',Phno=9439034756)
#
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('Chidasis',age= 24,city='Bangalore',Phno= 9439034756)
#You can call as much as  you can
def greet():
    print("Hello")
    print("Good Morning")
def sname():
    print("Megha")
greet()
sname()
#
def sum(n1, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res

print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))
#
def cheeseshop(kind):
    print("Do you have any ",kind,"?")
    print("I am sorry,we are all out",kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    keys = sorted(keywords.key())
    for kw in keys:
        print(kw,":",kewords[kw])
#
class Circle: 
    def area(self,r):
        ac=3.14*r**2 
        print("Area of Circle={}".format(ac)) 
class Square: 
    def area(self,s):
        sa=s**2 
        print("Area of Square={}".format(sa)) 
        print("-"*50) 
class Rect(Square,Circle): 
    def area(self,l,b): 
        ra=l*b 
        print("Area of Rect={}".format(ra)) 
        print("-"*50) 
        Square.area(self,float(input("Enter Side Value:")) ) 
        Circle.area(self,float(input("Enter the Radious:")) )
l,b=int(input("Enter Length:")),int(input("Enter Breadth:"))
ro=Rect() 
ro.area(l,b)
#
import threading,time 
def generate(): 
    print("Name of sub thread={}".format(threading.current_thread().name)) 
    n=int(input("\nEnter a number:")) 
    if(n<=0): 
        print("{} is invalid input:".format(n)) 
    else: 
        print("-"*40) 
        print("Numbers within:{}".format(n)) 
        print("-"*40) 
        for i in range(1,n+1): 
            print("Val of i={}".format(i)) 
            time.sleep(1) 
            print("-"*40)
t=threading.Thread(target=generate) 
print("Name of t1=",t.name) 
t.name="Vamsi"
t.start()
#
import time 
from threading import Thread 
class MulTable(Thread): 
    def run(self): 
        n=int(input("Enter a number:")) 
        if(n<=0): 
            print("{} is invalid input".format(n)) 
        else: 
            print("-"*50) 
            print("Mul table for {}".format(n)) 
            print("-"*50) 
            for i in range(1,11): 
                print("\t{} x {}={}".format(n,i,n*i)) 
                time.sleep(1) 
            print("-"*50)
mt=MulTable() 
mt.start()
#
import time 
from threading import Thread 
class MulTable(Thread):
    def setvalue(self): 
        self.n=int(input("Enter a number:")) 
    def run(self):
        self.setvalue() 
        if(self.n<=0): 
            print("{} is invalid input".format(self.n)) 
        else: 
            print("-"*50) 
            print("Mul table for {}".format(self.n)) 
            print("-"*50) 
            for i in range(1,11): 
                print("\t{} x {}={}".format(self.n,i,self.n*i)) 
                time.sleep(1) 
                print("-"*50)
mt=MulTable() 
mt.start()
#
import time 
from threading import Thread 
class CharGen(Thread): 
    def setvalue(self): 
        self.line=input("Enter a Line of Text:") 
    def run(self): 
        self.setvalue() 
        for i in self.line: 
            time.sleep(1) 
            print(i) 
            print() 
ct=CharGen() 
ct.start()
#
import threading,time 
class EvenOdd: 
    def __init__(self,n): 
        self.n=n 
    def generateeven(self): 
        print("Name of sub therad={}".format(threading.current_thread().name)) 
        if(self.n<=0): 
            print("{} is invalid input:".format(self.n)) 
            for i in range(2,self.n+1,2): 
                print("Val of Even Thread={}".format(i)) 
                time.sleep(1) 
    def generateodd(self): 
        print("Name of sub therad={}".format(threading.current_thread().name)) 
        if(self.n<=0): 
            print("{} is invalid input:".format(self.n)) 
            for i in range(1,self.n+1,2): 
                print("Val of Odd Thread={}".format(i)) 
                time.sleep(1)
n=int(input("Enter the Number:")) 
eo=EvenOdd(n) 
et=threading.Thread(target=eo.generateeven) 
ot=threading.Thread(target=eo.generateodd)
et.start() 
ot.start()
#
import time 
from threading import Thread 
class MulTable(Thread): 
    def run(self): 
        n=int(input("Enter a number:")) 
        if(n<=0): 
            print("{} is invalid input".format(n)) 
        else: 
            print("-"*50) 
            print("Mul table for {}".format(n)) 
            print("-"*50) 
            for i in range(1,11): 
                print("\t{} x {}={}".format(n,i,n*i)) 
                time.sleep(1) 
                print("-"*50)
mt=MulTable() 
mt.start()
#
import time 
from threading import Thread 
class MulTable(Thread):
    def setvalue(self): 
        self.n=int(input("Enter a number:")) 
    def run(self):
        self.setvalue() 
        if(self.n<=0): 
            print("{} is invalid input".format(self.n)) 
        else: 
            print("-"*50) 
            print("Mul table for {}".format(self.n)) 
            print("-"*50) 
            for i in range(1,11): 
                print("\t{} x {}={}".format(self.n,i,self.n*i)) 
                time.sleep(1) 
                print("-"*50)
mt=MulTable() 
mt.start()'''