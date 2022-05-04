is_active = True
is_perm = False
if 10 > 20 and 10 == 10:
    print("Executed 1")

if 'mani': # not none
    print("Madhu Nettem")
#
print("------------------------------------")
#if-statement
name = 'vn2'
if(name==''): # False
    print("if condition fails")
if None:  #False
    print("checking None exec:")
if not None:
    print("checking Not none value : ")

if 'Madhu':  # [1,2,3], (1,2,3), {1:1,2:2}  {1,2,3,4}
    print("Name exec")
if [1,]:  # []  () {}
    print("Empty string")


print("Arithmetic :", 10 + 20)
print("Relational :", 10 >= 20)
print("10 and 20 :", 10 and 20)  # 20 True and True --> True
print("10 and 0  :", 10 and 0)   #  0 True and False --> False
print("0 and 20 :", 0 and 20)    #  0 False and True --> False
print("0 and 0 :", 0 and 0)      #  0 False and False --> False
print("10 or 20 :", 10 or 20)
print("10 or 0 :", 10 or 0)
print("0 or 20 :", 0 or 20)
print("0 or 0 :", 0 or 0)
print("Membership :", 10 in [10, 20, 30])


x = 20
y = 10
if x > y:
    print("X value")
#
print("----------if---------------")
# S4: DEVELOPMENT      # Business logic implementation


#SDLC
x = 10 # static way of input
user_input = int(input("Enter number: "))  # S1 #dynamic way
if user_input == 20:                       # S2
    print("Welcome to Python World")  # S3
print("--------------------------------")
#
if 10+20:  # 30
    print("Successfully executed 10+20")  # Indentation

if True:
    print("True condition")

if False:
    print("False condition")

if not False:
    print("Print False condition")


if True or False:
    print("OR - condition ")

if True and True:
    print("AND - condition")

if 0:
    print("Value 0")
if None:
    print("Value None")
if not 0:
    print("Value 1")
if not None:
    print("Value not None")

if 10-20:
    print("Addition is success")

if 10 > 20:
    print("End of the program")
#
print("---------1----------")
x = 10+20
if x >= 10:
    print("Success")
    print("Hello world")

print("---------2----------")
if 10+2 >= 10:
    print("Arithmetic ops")
    print("Comparion ops")

print("---------1 Arithmetic----------")
if 10:
    print("Value is 10")
if 10+20:
    print("Arithmetic ops Addition1 ")

if 10-10:
    print("Arithmetic ops Substraction 1 ")

if 10-20:
    print("Arithmetic ops Substraction 2")

if 10 > 20:
    print("Comparions ops 1")

if 10+20 > 5+10:
    print("Comparions ops 2 ")


print("-------6 Logical--------")
x = True
y = False

if x or y:
    print("Boolean or1")

if False or True:
    print("Boolean or2")

if 10>20 or 5<10:
    print("Boolean or3")
# Condition
print("---------1----------")
x = 10+20
if x >= 10:
    print("Success")
    print("Hello world")

print("---------2----------")
if 10+2 >= 10:
    print("Arithmetic ops")
    print("Comparion ops")

print("---------1 Arithmetic----------")
if 10:
    print("Value is 10")
if 10+20:
    print("Arithmetic ops Addition1 ")

if 10-10:
    print("Arithmetic ops Substraction 1 ")

if 10-20:
    print("Arithmetic ops Substraction 2")

if 10 > 20:
    print("Comparions ops 1")

if 10+20 > 5+10:
    print("Comparions ops 2 ")


print("-------6 Logical--------")
x = True
y = False

if x or y:
    print("Boolean or1")

if False or True:
    print("Boolean or2")

if 10>20 or 5<10:
    print("Boolean or3")
#Condition
x = 12  # Hardcoding manner
print(x, type(x))


# to handle string
x = input("Enter number : ")  # Dynamic way of giving input value "12"
print(x, type(x))

# to handle integer
x = int(input("Enter number : "))  # Dynamic way of giving input value  int("12")
print(x, type(x))

if x >= 10:  # x > 9
    print("Two digit number")

print("-----End of program------")


# conditions:

if 10 > 5:
    print("Value is smaller")

if 10 % 3:
    print("Division result is 0")

if 10+20:
    print("Addition is 30")

if True and True:
    print("Logical and True 1")

if 10 > 2 and 10 % 2 == 0:
    print("Logical and True 2")


if False or True:
    print("Logical or True")

if 10>2:
    print("Line1")
    print("Line2")
    print("Line3")
    print("Line4")
    print("Line5")
    print("Line6")
    print("Line7")
print("End of program")

if type(10) == float:  # <class int> --> nonzero
    print("Type is integer")

is_present = False
if not is_present:
    print("Please attend the class !")

if 10 < 20 and 5 > 1:
    print("Yes the values are greater")

if 10+20 and 31-30:
    print("Logically executed")
#
x = 10
if x != 0:
    print("Value exists for x :", x)

x = input("Enter any number1 :")
print(x, type(x))  # "100" '100'
if x != 0:
    print("Value exists for x :", x)


x = int(input("Enter any number2 :"))  # Here we are converting string of number to number
print(x, type(x)) #  100
if x >= 10:
    print("Value exists for x :", x)