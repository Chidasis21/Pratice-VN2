'''#
def mullst(num):
    result = 1
    for i in num:
        result = result * i
    return result
lst1 = {2,4,6}
lst2 = {1,3,2}
print(mullst(lst1))
print(mullst(lst2))
#
def unique(x):
    a = []
    for i in x:
        if i not in a:
            a.append(i)
    return a
print(unique(x)([1,2,3,4,5,5,6,6,6,1]))
#
str1 = input("Enter a String : ")
str2 = ''
i = 0
while (i < len(str1)):
    if (i % 2 == 0):
        str2 = str2 + str1[i]
    i = i + 1
print("Input String : ", str1)
print("Final String : ", str2)
#
str1 = input("Enter a String : ")
str2 = ''
i = 0
while (i < len(str1)):
    if (i % 2 == 0):
        str2 = str2 + str1[i]
    i = i + 1
print("Input String : ", str1)
print("Final String : ", str2)
#
str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1+str2
print("Concatenated two different strings:",str)
#
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
#
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()
#
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
#
def isPalindrome(n):
    reverse = 0
    reminder = 0
    while(n != 0):
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = int(n / 10)
    return reverse

num = int(input('Enter the number: '))

reverse = isPalindrome(num)
if(num == reverse):
  print(num,'is a Palindrome')
else:
  print(num,'is not a Palindrome')
#
import gc 
class Employee: 
    def __init__(self,eno,ename,sal): 
        print("I am from Constructor:") 
        self.eno=eno 
        self.ename=ename 
        self.sal=sal 
        print("{}\t{}\t{}".format(self.eno,self.ename,self.sal)) 
    def __del__(self):
        print("\nDestructor called by Garbage Collector:")
print("Line-15-->Is Gc is Enabled / Running?=",gc.isenabled())
print("Line-16-->Program execution Started:"),gc.disable() 
print("Line-19-->Is Gc is Enabled / Running?=",gc.isenabled())
eo1=Employee(10,"RS",34.56) 
eo2=Employee(20,"DR",44.56) 
eo3=Employee(30,"MC",24.56) 
print("Line-23-->Program execution ended:")
#polymerphism
class IntSum: 
    def sumop(self):
        print("-"*40) 
        a=int(input("Enter First int Value:")) 
        b=int(input("Enter Second int Value:")) 
        c=a+b 
        print("sum of integers={}".format(c)) 
        print("-"*40) 
class StrSum(IntSum): 
    def sumop(self):
        print("="*60) 
        a=input("Enter First Str Value:") 
        b=input("Enter Second str Value:") 
        c=a+b 
        print("sum of strs={}".format(c)) 
        print("="*60) 
class ComplexSum(StrSum): 
    def sumop(self):
        print("*"*60) 
        a=complex(input("Enter First Complex Value:")) 
        b=complex(input("Enter Second Complex Value:")) 
        c=a+b 
        print("sum of complex values={}".format(c)) 
        print("*"*60)
cc=ComplexSum() 
cc.sumop()
#By using super()
class C1: 
    def __init__(self): 
        print("C1-Default Constructor") 
class C2 (C1): 
    def __init__(self): 
        print("C2-Default Constructor") 
        super().__init__() 
class C3 (C2): 
    def __init__(self): 
        print("C3-Default Constructor") 
        super().__init__()
o3=C3()
#
class c1:
    def __init__(self,a):
        print("c1-Parameterized constructure")
        print("Val of b in c1 = {}".format(a))
        print("-----------------------------")
class c2(c1):
    def __init__(self,b):
        print("c2-Parameterized constructure")
        print("Val of b in c2 = {}".format(b))
        print("-----------------------------")
        super().__init__(300)
class c3(c2):
    def __init__(self,c):
        print("c3-Parameterized constructure")
        print("val of b in c3 = {}".format(c))
        print("-----------------------------")
        super().__init__(200)
c3 = c3(100)
#
class A:
    classvar1 = "I am a variable in class A"
    def __init__(self):
        self.var1 = "I am inside the the A constusture"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
class B:
    classcar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am in class B"
        self.classvar1 = "Instance var in class A"
        super().__init__()
        print(super().classvar1)
a = A()
b = B()
#
class person1:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fulname (self):
        prin(firstname,'',lastname)
class student(person1):
    def __init__(self, firstname, lastname, grade):
        self.grade = grade
        super().__init__(firstname, lastname)
    def display_det():
        super(),fullname()
        print('Chidasis','Sethy','24')
std = student('Chidasis','Sethy','24')
std.display_det()
#
class pclass1(obj):
    def __init__(self):
        print("This is Base Class1")
        pass
class pclass2(obj):
    def __init__(self):
        print("This is Base class2")
        pass
class cclass1(pclass1,pclass2):
    def __init__(self):
        super(cclass1,self).__init__()
c1 = cclass1()'''
#
class mango:
    def __init__(self):
        self.mango_attribute = "I am from Mango"
    def mango_method(self):
        print('Mango is good')
class mangojuice:
    def __init__(self):
        super().__init__()
        self.mangojuice_attribute(self):
    def child_method(self):
        print('Juice is best')
child = mangojuice()
print(child.mangojuice_attribute)
print(child.mango_attribute)
child.mango_attribute 
child.child_method
#
