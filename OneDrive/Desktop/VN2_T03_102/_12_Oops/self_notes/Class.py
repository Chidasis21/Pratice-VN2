'''
Class :-    Class is one of distinct feature of OOPs.
            Class is  TO develope programming define data type and develope the realtime application.
            To develope a program define datatype with class we using a keyword 'CLASS'.
            A Class is a collection of data members and method.
            All the value are store in the form objects and to creat an object we need class defination.
#Class exapmles :-
#1st
class  Emp:
    Cname="VN2"
Emp.Cadd="Bangalore"
eo1=Emp()
eo1.eno="100"
eo1.ename="Sri"
eo1.sal="10000"
eo2=Emp()
eo2.eno="101"
eo2.ename="Chanchad"
eo2.sal="10000"
eo3=Emp()
eo3.eno="100"
eo3.ename="Raju"
eo3.sal="10000"
print()
print("First Emp data")
print("----------------------")
print("Emp no:{}".format(eo1.eno))
print("Emp name:{}".format(eo1.ename))
print("Emp sal:{}".format(eo1.sal))
print("Second Emp data")
print("----------------------")
print("Emp no:{}".format(eo2.eno))
print("Emp name:{}".format(eo2.ename))
print("Emp sal:{}".format(eo2.sal))
print("Third Emp data")
print("----------------------")
print("Emp no:{}".format(eo3.eno))
print("Emp name:{}".format(eo3.ename))
print("Emp sal:{}".format(eo3.sal))
#2nd
class Emp:
    cname = "IBM"
Emp.cadd = "Bhubaneswar"

eo1 = Emp()
eo1.eno = int(input("Enter a first Emp number :"))
eo1.ename = input("Enter a first Emp name :")
eo1.sal = int(input("Enter a first Emp sal :"))

eo2 = Emp()
eo2.eno = int(input("Enter a second Emp number :"))
eo2.ename = input("Enter a second Emp name :")
eo2.sal = int(input("Enter a second Emp sal :"))

eo3 = Emp()
eo3.eno = int(input("Enter a third Emp number :"))
eo3.ename = input("Enter a third Emp name :")
eo3.sal = int(input("Enter a third Emp sal :"))

print("-----------------------------")
print("First Emp data")
print("-----------------------------")
print("Emp num:{}".format(eo1.eno))
print("Emp name:{}".format(eo1.ename))
print("Emp sal:{}".format(eo1.sal))

print("-----------------------------")
print("Second Emp data")
print("-----------------------------")
print("Emp num:{}".format(eo2.eno))
print("Emp name:{}".format(eo2.ename))
print("Emp sal:{}".format(eo2.sal))

print("-----------------------------")
print("Third Emp data")
print("-----------------------------")
print("Emp num:{}".format(eo3.eno))
print("Emp name:{}".format(eo3.ename))
print("Emp sal:{}".format(eo3.sal))

#3rd
class Employee:
    def __init__(self):
        print("I am from constructor")
        self.eno=int(input("Enter Employee Number:"))
        self.ename=input("Enter Employee Name:")
eo1=Employee()
__init__(self)
print("Content of eo1 before reading the data=",eo1.__dict__)
#4th
class Test:
    def __init__(self):
        print("i am from constructor:")
        self.a=10
        self.b=20
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
t1=Test()
#5th
class Test:
    def __init__(self, a,b):
        print("i am from Parameterized constructor:")
        self.a=a
        self.b=b
        c=self.a+self.b
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
        print("sum=",c)
x=float(input("Enter the value of x:"))
y=float(input("Enter the value of y:"))
t1=Test(x,y)
#6th
class Test:
    def __init__(self):
        print("i am from default constructor:")
        self.a=10
        self.b=20
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
t1=Test()
t2=Test()
#7th
class Test:
    def __init__(self,a,b):
        print("i am from Parameterized constructor:")
        self.a=a
        self.b=b
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b)) # main program
t1=Test(10,20)
t2=Test(100,200)
t3=Test(1000,2000)
#8th
class person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello,My name is ', self.name)
p = person('Chidasis')
p.say_hi()
#9th
class person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello,My name is ', self.name)
p1 = person('Chidasis')
p2 = person('Pradeep')
p3 = person('Ashish')
p4 = person('Rakesh')
p1.say_hi()
p2.say_hi()
p3.say_hi()
p4.say_hi()'''
'''#10th
class X(object):
    def __init__(self, person):
        print("X init called")
        self.person = person
class Y(X):
    def __init__(self, person):
        print("Y init called")
        self.person = person
        X.__init__(self, person)
obj = Y("person")
#11th'''
