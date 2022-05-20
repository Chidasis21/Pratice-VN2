str = "Python"
for i in str:
    print(i, end = " ")

list = [1,2,3,4,5,6,7,8,9,10]
n = 12
for i in list:
    c = n*i
    print(c, end= " ")

list = [10,30,23,45,56,78,13]
sum = 0
for i in list:
    sum = sum + i
print("The sum is:", sum)

for i in range (1,11):
    print(i, end= ",")

n = int(input(" Enter a number "))
for i in range(1,11):
    c = n*i
    print(n,"*",i,"=",c)
#
for i in range(20,0,-1):
    if i % 2 != 0:
        print(i, end=" ")
#
num =  int(input(" enter a number "))
for i in range (1,11):
    print(num,'*',i, "=",num * i )
#
num =input(" Enter a number: ")
prod = 1
for n in num:
    prod = prod * int(n)
print(prod)
#
num = int(input(" Enter a number: "))
fact = 1
for i in range (1, num+1):
    fact = fact*i
    print("fact of", num ,"is"," = ",fact)
#
num =input(" Enter a number: ")
sum = 0
for n in num:
    sum = sum + int(n)
print(sum)
#
num = int(input(" enter a number :"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "it is not prime number")
            break
    else:
        print(num,"it is a prime number")
#
n = int(input(" enter a number "))
for i in range (1, n+1):
    for j in range (1, i+1):
        print(j, end = "")
    print()
#
n = int(input(" enter a number "))
for i in range (n, 0, -1):
    for j in range (0, i):
        print(j, end = " ")
    print()
#
I = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(I))
        I = I+1
print()
I = 65
#
for i in range(1,99,3):
    print(i)
#While
s = 0
i = 1
n= 1
while (n!=0):
    n = int(input(" Enter a number "))
    s = s + n
    i = i + 1
print(s)
avg = s/i
print(avg)
#
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
print ("All is well !")
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
#
print("--Numbers divisible  with 5------")
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1
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
print("--------Numbers div 5 or 8, not by 3 -----------")
n1 = 1
n2 = 50
while n1 <= n2: #true
    if n1 % 5 == 0 or n1 % 8 == 0: # 15 True
        if n1 % 3 != 0:  # 15 / 3  False
            print(n1)

    n1 += 1
#
if True or False:
    print("executed")

x = 10
y = 20
if x == y or x > y:
    print(" not executed")
else:
    print("false")
x = True
y = False
if x == y:
    print("executed")
elif y or y:
    print("block")
else:
    print("yes")
print('yes') if x or y else print('no')
print("y") if x or y else print("N") if x or y else print("no")
print("yes") if 10 > 2 else print("no")
#
num = 1
count = 0
while num <= 100:
    if num % 2 == 0:
        print(num)
        count += 1
        if count == 7:
            break
    num += 1
print("End of while loop")
#
str = "Python"
for i in str:
    print(i, end = " ")
list = [1,2,3,4,5,6,7,8,9,10]
n = 12
for i in list:
    c = n*i
    print(c, end= " ")
list = [10,30,23,45,56,78,13]
sum = 0
for i in list:
    sum = sum + i
print("The sum is:", sum)
for i in range (1,11):
    print(i, end= ",")
n = int(input(" Enter a number "))
for i in range(1,11):
    c = n*i
    print(n,"*",i,"=",c)
#
s = 0
i = 1
n= 1
while (n!=0):
    n = int(input(" Enter a number "))
    s = s + n
    i = i + 1
print(s)
avg = s/i
print(avg)
#
I = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(I))
        I = I+1
print()
I = 65
#