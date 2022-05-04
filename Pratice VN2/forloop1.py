#
print("----------Iterating string using for loop------------------")

str = "Python"
for i in str:
    print(i)

print("--------------Program to print the table of the given number----------")

list = [1,2,3,4,5,6,7,8,9,10]
list2 = [5, 10, 15, 12]

for i in list:
    for j in list2:
        val = i * j
        print(val,end = ',')

print(" Program to print the sum of the given list.")

list = [10,30,23,43,65,12]
x = 0
for i in list:
    x = x+i #(x += i)
print("The sum is:",x)
#
print("Program to print numbers in sequence")

for i in range(10):
    print(i,end = ' ')

print(" Program to print table of given number")

n = int(input("Enter the number "))
for i in range(1, 11):
    c = n*i
    print(n,"*",i,"=",c)

print("Program to print even number using step size in range()")


n = int(input("Enter the number "))
for i in range(2,n,2):
    print(i)

for i in range(1, 100, 2):
    print(i, end=',')
#
list = ['Peter','Joseph','Ricky','Devansh']
for i in range(len(list)):
    print("Hello",list[i])
#
print(" Nested for loop ")
# User input for number of rows
rows = 5
# Outer loop will print number of rows
for i in range(1,rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("*", end='')
    print()

print(" Program to number pyramid ")
rows = 5

for i in range(0,rows+1):
    for j in range(i):
        print(i,end = '')
    print()
#
# Example 1
for i in range(0,5):
    print(i)
else:
    print("for loop completely exhausted, since there is no break.")

# Example 2
for i in range(0,5):
    print(i)
    break
else:print("for loop is exhausted");
print("The loop is broken due to break statement...came out of the loop")
