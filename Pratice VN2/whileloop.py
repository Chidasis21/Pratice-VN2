print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

#print numbers from 1 to 5
print("--------------")
x = 1
while x <= 5:
    print(x)
    x += 1   # Assignment operator += -=   x += 1
print("End of program")
print("--------------")
#
print("-----------Odd numbers----------")
num1 = 1 #int(input("Enter number1: "))
num2 = 100 #int(input("Enter number2: "))
while num1 <= num2:
    if num1 % 2 == 1:
        print(num1)
    num1 += 1
print("--------------------------------")
#
print("------Divisible by 5------")
n1 = 1
n2 = 100
while n1 <= n2:
    if n1 % 5 == 0:
        print(n1)
    n1 += 1
print("-------------------------")
#
print("------Divisible by 3 and 7----------")
n1 = 1
n2 = 500
while n1 <= n2:
    if n1 % 3 == 0 and n1 % 7 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")


# Print numbers divisible by 5 or 6
print("------Divisible by 5 or 6----------")
n1 = 100
n2 = 500
while n1 <= n2:
    if n1 % 5 == 0 or n1 % 6 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")


print("------Numbers which ends with 0----------")
n1 = 100
n2 = 500
while n1 <= n2:
    if n1 % 10 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")
#
print("--------Numbers from 1 to 10--------")

num = 1
while num <= 10:   # Check condition in each iteration
    print(num)
    num = num + 1  # num += 1

print("--------End of program--------")
#
num = 100
while num <= 150:
    print(num)
    num += 1
#
print("--------Print even numbers--------")
# STATE
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

num = 2
while num <= 100:
    if num % 2 == 0 and num % 4 == 0:
        print(num)
    num += 1


print("--------Print odd numbers--------")

# Print odd numbers betweeen 10 to 20
num = 10
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1

# Print numbers between 500 to 1000 and divisible by 5

print("--Numbers divisible  with 5------")
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1


# Print numbers between 500 to 1000. It should be divisible by 5 and divisible by 8
print("--Numbers divisible  with 5 and 8------")
num = 500
while num <= 600:
    if num % 5 == 0 and num % 8 == 0:
        print(num)
    num += 1

# Print numbers between 500 to 1000. It should be divisible by 5 or divisible by 9
print("--Numbers divisible  with 5 or 9------")
num = 500
while num <= 600:
    if num % 5 == 0 or num % 9 == 0:
        print(num)
    num += 1
#
print("--------Numbers div 5 or 8, not by 3 -----------")

n1 = 1
n2 = 50
while n1 <= n2: #true
    if n1 % 5 == 0 or n1 % 8 == 0: # 15 True
        if n1 % 3 != 0:  # 15 / 3  False
            print(n1)

    n1 += 1
#
print("sum and average of user input number until zero")

num = 1
i = -1
s = 0
while(num!=0):
    num = int(input("enter any number"))
    s = s + num
    i = i + 1  # (here i +)
print("sum of numbers entered by user", s)
print("Average of numbers entered by user", s/i)
#
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

#print numbers from 1 to 5
'''
while <condition>:
    <statements body> 
'''
print("--------------")
x = 1
while x <= 5:
    print(x)
    x += 1   # Assignment operator += -=   x += 1
print("End of program")
#
print("--------------")

# IV. DEVELOPMENT
    #STATE
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
    #BEHAVIOR
while num1 <= num2:
    print(num1)
    num1 += 1
print("***** End of program *****")

#
num1 = 500
num2 = 100
if num1 <= num2:
    while num1 <= num2:
        print(num1)
        num1 += 1
else:
    print("### num1 should be less than num2  ###")
print("***** End of program *****")

n = 10

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
#
print("------Divisible by 5------")
n1 = 1
n2 = 100
while n1 <= n2:
    if n1 % 5 == 0:
        print(n1)
    n1 += 1
print("-------------------------")
#
print("------Divisible by 3 and 7----------")
n1 = 1
n2 = 500
while n1 <= n2:
    if n1 % 3 == 0 and n1 % 7 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")


# Print numbers divisible by 5 or 6
print("------Divisible by 5 or 6----------")
n1 = 100
n2 = 500
while n1 <= n2:
    if n1 % 5 == 0 or n1 % 6 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")


print("------Numbers which ends with 0----------")
n1 = 100
n2 = 500
while n1 <= n2:
    if n1 % 10 == 0:
        print(n1)
    n1 += 1
print("----------------------------------")
