''''
#Q1.
class Addition:
    def getvalues(self):
        self.a=float(input("Enter a value of a :"))
        self.b=float(input("Enter a value of b :"))
    def findsum(self):
        self.c=self.a+self.b
    def findsub(self):
        self.c=self.a-self.b
    def findmul(self):
        self.c=self.a*self.b
    def finddiv(self):
        self.c=self.a/self.b
    def displayvalue(self):
        print("Value of a = {}".format(self.a))
        print("Value of b = {}".format(self.b))
        print("sum={}".format(self.c))
ao=Addition()
ao.getvalues()
ao.findsum()
ao.displayvalue()

#Q2.
class Addition: 
    def getvalues(self): 
        self.a=float(input("Enter Value of a:")) 
        self.b=float(input("Enter Value of b:")) 
    def findsum(self): 
        self.c=self.a+self.b 
    def dispvalues(self): 
        print("Val of a={}".format(self.a)) 
        print("Val of b={}".format(self.b)) 
        print("Sum={}".format(self.c)) 
ao=Addition() 
ao.getvalues() 
ao.findsum() 
ao.dispvalues()

#Q3.
class Employee: 
    @classmethod 
    def getcompanyname(cls): 
        cls.cname="TCS" 
        cls.getcompanyaddr() 
        @classmethod 
    def getcompanyaddr(cls): 
        cls.addr="HYD" 
    def getempdet(self): 
        self.eno=int(input("Enter Employee Number:")) 
        self.ename=input("Enter Employee Name:")
    def dispempdet(self): 
        print("Employee Number:{}".format(self.eno)) 
        print("Employee Name:{}".format(self.ename)) 
        print("Employee Company Name:{}".format(Employee.cname)) 
        print("Employee Company Name:{}".format(Employee.addr))
Employee.getcompanyname() 
eo1=Employee() 
eo1.getempdet() 
eo1.dispempdet()

#Q4
class Employee: 
    @classmethod 
    def getcompanyname(cls): 
        cls.cname="TCS" 
        cls.getcompanyaddr() 
        @classmethod 
    def getcompanyaddr(cls): 
        cls.addr="HYD" 
    def getempdet(self): 
        self.eno=int(input("Enter Employee Number:")) 
        self.ename=input("Enter Employee Name:") 
    def dispempdet(self): 
        print("Employee Number:{}".format(self.eno)) 
        print("Employee Name:{}".format(self.ename)) 
        Employee.getcompanyname()
        print("Employee Company Name:{}".format(Employee.cname)) 
        print("Employee Company Name:{}".format(Employee.addr))
eo1=Employee() 
eo1.getempdet() 
eo1.dispempdet()

#Q5
class Employee: 
    @classmethod 
    def getcompanyname(cls): 
        cls.cname="TCS" 
        cls.getcompanyaddr() 
        @classmethod 
    def getcompanyaddr(cls): 
        cls.addr="HYD" 
    def getempdet(self): 
        self.eno=int(input("Enter Employee Number:")) 
        self.ename=input("Enter Employee Name:") 
        Employee.getcompanyname() 
        self.dispempdet() 
    def dispempdet(self): 
        print("Employee Number:{}".format(self.eno)) 
        print("Employee Name:{}".format(self.ename)) 
        print("Employee Company Name:{}".format(Employee.cname)) 
        print("Employee Company Name:{}".format(Employee.addr)) 
eo1=Employee() 
eo1.getempdet()

#Q6
class Circle: 
    def getrad(self): 
        self.r=float(input("Enter Radius:")) 
    def calarea(self): 
        ac=3.14*self.r**2 
        print("Area of Cicrle={}".format(ac)) 
    def calcircum(self): 
        pc=2*3.14*self.r 
        print("Circumference pf Circle={}".format(pc))
co=Circle() 
co.getrad() 
co.calarea() 
co.calcircum()

#Q7
class Circle: 
    PI=3.14 
    def getrad(self): 
        self.r=float(input("Enter Radius:")) 
    def calarea(self): 
        ac=Circle.PI*self.r**2 
        print("Area of Cicrle={}".format(ac)) 
    def calcircum(self): 
        pc=2*self.PI*self.r 
        print("Circumference pf Circle={}".format(pc))
co=Circle() 
co.getrad() 
co.calarea() 
co.calcircum()

#Q8
class Circle: 
    @classmethod 
    def getpi(cls): 
        cls.pi=3.14 
        return 
        Circle.pi 
    def getrad(self): 
        self.r=float(input("Enter Radius:")) 
    def calarea(self): 
        ac=Circle.getpi()*self.r**2 
        print("Area of Cicrle={}".format(ac)) 
    def calcircum(self): 
        pc=2*self.getpi()*self.r 
        print("Circumference pf Circle={}".format(pc))
co=Circle() 
co.getrad() 
co.calarea()
co.calcircum()

#Q8
import pickle 
from student import
Student class StudentInsert:
    def savestuddata(self): 
        with open("stud.info","ab") as fp: 
            while(True): 
                print("-"*40) #create an student object 
                so=Student() 
                    so.getstuddet() #save so data in a file 
                pickle.dump(so,fp) 
                print("-"*40) 
                print("Student Data Saved in a File:") 
                print("-"*40) 
                ch=input("Do u want to insert another student record(yes/no):") 
                if(ch=="no"): 
                    break 
                if(ch!="yes"): 
                    print("\nPlz learn Typing!") 
                    break
so1=StudentInsert() 
so1.savestuddata()

#Q9
import pickle 
class StudentRetrive: 
    def getstuddata(self): 
        try: 
            with open("stud.info","rb") as rp: 
                print("-"*40) 
                print(" S t u d e n t I n f o r m a t i o n") 
                print("-"*40) 
                while(True): 
                    try: 
                        stuobj=pickle.load(rp) 
                        stuobj.dispstuddet() 
                    except EOFError: 
                        print("-"*40) 
                        break 
        except FileNotFoundError: 
            print("File does not exists:")
sr=StudentRetrive() 
sr.getstuddata()

#Q10
import cx_Oracle
class OOpswithDB: 
    def records(self,tname): 
        try: 
            con=cx_Oracle.connect("scott/tiger@localhost/orcl") 
            cur=con.cursor() 
            records=cur.execute("select * from %s" %tname) 
            print("-"*40) 
            for cname in [cnames[0] for cnames in cur.description]: 
                print("\t{}".format(cname),end=" ") 
                print() 
                print("-"*40) 
                for record in records: 
                    for val in record: 
                        print("\t{}".format(val),end=" ") 
                    print() 
                print("-"*40) 
        except cx_Oracle.DatabaseError as db: 
            print("\nProblem in DB:",db) 
tname=input("Enter Table Name:") 
od= OOpswithDB() 
od.records(tname)
'''
