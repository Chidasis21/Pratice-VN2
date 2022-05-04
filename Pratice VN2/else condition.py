print("-----------Result with PASS/FAIL-----------")
    # 1. STATE
# marks = 80  # static way of data initialization,  hardcoding data
marks = int(input("Enter marks b/w 0 to 100 :"))   # Dynamic way

    # 2. B    EHAVIOR
if marks >= 0 and marks <= 100:   # 0 to 100
    if marks >= 35:  # True
        print(marks, "Result : PASS")
    else:
        print(marks,"Result : FAIL")
else:
    print("Please enter valid marks")

marks = int(input("Enter marks :"))   # Dynamic way
# 2. BEHAVIOR
if marks < 0 or marks > 100:
    print("Please enter valid marks")
else:
    if marks >= 35:
        print("Result : PASS")
    else:
        print("Result : FAIL")
#
print("-----------Positive or Negative-----------")
#num = 10
num = int(input("Enter any number: "))

if num > 0:
    print("Number is positive")
elif num < 0:  # -1  , 0
    print("Number is negative")
else:     # elif num == 0
    print("Neither pos. nor Neg.")
#
print("-----------Result with class-----------")
# STATE
marks = int(input("Enter marks :"))

if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 to 100")
else:
    if marks >= 60:
        print("Result : FIRST CLASS")
        if marks == 100:
            print("-----SUPER..Congratulations-----")
        elif marks >= 90:
            print("----GOOD..Congratulations-------")
    elif marks >= 50 and marks < 60:
        print("Result: SECOND CLASS")
    elif marks >= 35 and marks < 50:
        print("Result: THIRD CLASS")
    else:
        print("Result: FAIL")
        if marks == 0:
            print("--------DOUBLE SUPER----------")
#
x = 10
print(x)
x = 10.5
print(x)
x = True  # 1 nonzero nonNone
print(x)
x = False # 0  None
print("---------------------")

# Find given number is even or odd
# Solution : If any number is divisible by 2 and remainder is 0, it is Even number,
# else odd number.
num = int(input("Enter number : "))
print("Given number : ", num)


# Decision Making
if num % 2 == 0:
    print("Even number")  # 4 spaces indentation
else:
    print("Odd number")   # block of statements
#
x = 10
print(x)
x = 10.5
print(x)
x = True  # 1 nonzero nonNone
print(x)
x = False # 0  None
print("---------------------")

num = int(input("Enter number : "))
print("Given number : ", num)

# Decision Making
if num % 2 == 0:
    print("Even number")  # 4 spaces indentation
else:
    print("Odd number")   # block of statements
