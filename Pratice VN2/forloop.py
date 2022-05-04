x = 10   # integer
x = 10.5  # float
x = True   # boolean
msg = 'Hello World'  # string

# Data structures
msg = 'Hello World'         # string
list1 = [1, 2, 3, 4, 5]     # list
tup1 = (1, 2, 3, 4, 5)      # tuple
dict1 = {1: 1, 2: 2, 3: 3}  # dictionary
set1 = {1, 2, 3, 4, 5, 6}   # set
#
course = 'python'
i = 'hello'
#
print("--------For loop with String-------")
# Print each character of string
course = 'PYTHON PROGRAMMING'
for char in course:  # char = 'P'
    print(char)
print("----------End-----------------------")
print(10)

x = 10
print(x)

msg = 'Python world '
for e in msg:
    print("Character : ", e)

print(msg)
print(msg[0])
print(msg[1])
#
for char in 'Welcome to Python':
    print("Char : ", char)
print("_____________________________________________________________")
for char in 'aflkdsfdsalfsdf  324324SDFDSF@!#@!$#@%fsdfsd dsfdsFDSf!@#@!#!@':
    print("Char : ", char)

# List with for loop
for val in [1, 2.5, True, 'Madhu', 5.0, False, 7]:
    print("List data :", val)

for val in [1, 2, 3, 4, 5, 6, 7]:
    print("List data :", val)

# Tuple with for loop
for val in (1, 2, 3, 4, 5, 6, 7):
    print("Tuple data :", val)
print("----------------------------")
# Dictionary with for loops
e_data = {'eid': 100.50, 'name': 'Madhu Nettem', 'sal': True}
print(e_data)
for i in e_data:
    print("Dict data :", i)
print("--------------------------------")
for x in e_data.keys():
    print("Dict key :", x)
print("--------------------------------")
for val in e_data.values():
    print("Dict val :", val)
print("--------------SET---------------------")
# set with for loop
set1 = {1, 2, 3, 4, 5, 6}
for val in set1:
    print("Set value : ", val)

