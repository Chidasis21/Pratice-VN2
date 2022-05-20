'''class company:
    def getcompanydet(self):
        self.cname="TCS"
        self.caddr="Bangalore"
class sunny(company):
    def getsunnydet(self):
        self.eno=int(input("Enter a number:"))
        self.ename=input("Enter a name:")
        self.eaddr=input("Enter address:")
    def getsunnydet(self):
        print("Input employee no".format(self.eno))
        print("Input employee name".format(self.ename))
        print("Input employee address".format(self.eaddr))
so = sunny()
print("19-----content of so=",so.__dict__)
so.getsunnydet() 
print("21---ontent of so=",so.__dict__)
so= {'eno': 10, 'ename': 'Sunny', 'dsg': 'SE'} so.getcompanydetails() 
print("23---ontent of so=",so.__dict__)
so= {'eno': 10, 'ename': 'Sunny', 'dsg': 'SE', 'cname': 'TCS', 'caddr': 'HYD'}
#
class Rossum:
    def getsub(self):
        print("Rossum developed Python")
class Gosling:
    def getsub(self):
        print("Gosling developed Java")
class Ritch:
    def getsub(self):
        print("Ritch developed C")
class kvr(Rossum,Gosling,Ritch):
    def getsub(self):
        print("Print KVR teach C, Java and Python")
        print("----------------------------------")
        Rossum.getsub(self)
        Gosling.getsub(self)
        Ritch.getsub(self)
k=kvr()
k.getsub()
#
class Employee:
    def getempvalue():
        self.eno=int(input("Enter a nummber :"))
        self.ename=input("Enter a name :")
eo1=Employee()
print("Content of eo1 before reading the data=",eo1.__dict__)
#
class Test: 
    def __init__(self): # default constructor / zero argument constructor 
        print("i am from constructor:") 
        self.a=10 
        self.b=20 
        print("Val of a={}".format(self.a)) 
        print("Val of b={}".format(self.b))
t1=Test()
#Inheritance
#1st
class Parent():
       def first(self):
           print('first function')
class Child(Parent):
       def second(self):
          print('second function')
ob = Child()
ob.first()
ob.second()
#2nd
class Parent:
     def __init__(self,fname,fage):
          self.firstname = fname
          self.age = fage
     def view(self):
         print(self.firstname,self.age)
class Child(Parent):
     def __init__(self,fname,fage):
          Parent.__init__(self,fname,fage)
          self.lastname = "KV Rao"
     def view(self):
          print("course name",self.firstname,"first came",self.age ,"years ago." ,self.lastname," has courses to master python")
ob = Child("Python",'28')
ob.view()
#3rd(Single Inheritance)
class Parent:
     def func1(self):
          print("Function1")
class Child(Parent):
     def func2(self):
          print("Function2")
ob = Child()
ob.func1()
ob.func2()
#4th(Multiple Inheritance)
class Parent:
   def func1(self):
        print("Function1")
class Parent2:
   def func2(self):
        print("Function2")
class Child(Parent , Parent2):
    def func3(self):
        print("Function3")
ob = Child()
ob.func1()
ob.func2()
ob.func3()
#5th(Multilavel Inheritance)
class Parent:
      def func1(self):
          print("function 1")
class Child(Parent):
      def func2(self):
          print("function 2")
class Child2(Child):
      def func3("function 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()
#Encapsulation
class Emp:
    def __init__(self, name, sal, project):
        self.name = name
        self.sal = sal
        self.project = project
    def show(self):
        print("Name: ", self.name, 'Sal:', self.sal)
    def work(self):
        print(self.name, 'is working on', self.project)
emp = Emp('Rakesh', 80000, 'TCS')
emp.show()
emp.work()
#
class Emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def show(self):
        print("name:",self.name,"salary:",self.sal)
emp = Emp('Rakesh',800000)
print("name:",emp.name,"sal",emp.sal)
emp.show()
#
class Emp:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
emp =Emp("Rakesh",80000)
print('sal:',emp.sal)
#
class Emp:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
    def show(self):
        print("name:",self.name,"sal:",self.sal)
emp = Emp('Rakesh',800000)
emp.show()
#
class Company:
    def __init__(self):
        self.project = "TCS"
class Employee:
    def __init__(self,name):
        self.name = name
        Company.__init__('self')
    def show(self):
        print("Emplayee name :",self,name)
        print("Working on project :",self.project)
c = Employee("Rakesh")
c.show()
print('Project :',c.project)'''
#
class Teacher: 
    def getTeacherdet(self): 
        self.tno=int(input("Enter Teacher Number:")) 
        self.tname=input("Enter Teacher Name:") 
        def dispteacherdet(self): 
            print("Teacher Number:{}".format(self.tno)) 
            print("Teacher Name:{}".format(self.tname)) 
class Company: 
    def getcompdet(self): 
        self.cname=input("Enter Comp Name:") 
        self.caddr=input("Enter Company Address:") 
        def dispcompdet(self): 
            print("Comp Name:{}".format(self.cname)) 
            print("Company Address:{}".format(self.caddr)) 
class Student (Teacher,Company): 
    def getstuddet(self): 
        self.s no=int(input("Enter Student Number:")) 
        self.sname=input("Enter Student Name:") 
def dispstuddet(self): 
    print("Student Number:{}".format(self.sno)) 
    print("Student Name:{}".format(self.sname   ))
so=Student() 
so.getstuddet() 
so.getTeacherdet() 
so.getcompdet() 
print("-"*40) 
so.dispstuddet() 
so.dispteacherdet() 
so.dispcompdet() 
print("-"*40)