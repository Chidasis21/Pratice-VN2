#
print(10)
#
x = 10  # Let us assume x = 10
print(x)
print(x+20)
#
x = 10
print("Value of x : ", x)
print("Addition   : ", x+20)
#introduction
str1 = 'Hello World'  # "Hello World"
#   012345678910
#                 -3-2-1
x = y = 10
# 2 = 3 = l
print(str1)
print(type(str1), id(str1))

print(id(str1), id(str1[0]), id(str1[2]))
print("l mem location:", id(str1[2]),id(str1[3]), id(str1[9]) )
#
ch = 'A'  # "A"
print(ch)

ch = "1"  # "1"
print(ch+"2") # join/concatnate
print(ch, type(ch))
print("Addition :", int(ch)+2)

ch = '1.5'
#5kgs oil + 2dozen
print("Addition : ", float(ch)+2.7) # 1.52.7

ch = '*'
print(ch, type(ch))
#
print("-----Conversions----------")
x = 10
y = "20"
#print(x+y)
print(x, y, type(x), type(y))

if type(x) == type(y):
    print("Addition :", x+y)
else:
    print("Addition is not possible")
#
x = 10
print("------------String for loop------------")
for char in 'Hello World':  # A 65 a 97
    print(char)
print()
print("------------CRUD Operations------------")
# CRUD Operations
x = 10     # CREATE    Write operation
print(x)   # RETRIEVE  Read operation
x = 20     # UPDATE
del x      # DELETE
#
msg = 'Hello World'
msg1 = 'Hello World'
print(msg, msg1, id(msg), id(msg1))
msg = 'python'
#memory allocation
x = 10
print(x, type(x), id(x))

print(msg)
print("4th index :", msg[4])
print("10th index :", msg[-1])
print(id(msg))
print(id(msg[2]), id(msg[5]))
#
x = 10
print("Value of x: ", x)
x = 20
print("Value of x: ", x)

msg = 'Hello World'
print("Message1 is : ", msg, id(msg))

msg = 'Python'
print("Message1 is : ", msg, id(msg))
#
x = 10
x = x + 20

msg = 'hello'  # immutable fixed
print('Message2 : ',msg)
msg = 'Hello' + 'world'
print('Message2 : ',msg)

x = 'Hello World'
x = [1,2,3,4,5,6,7,8]
for x[-1] in x:
    print(x[-1])
#sequence operation
message = 'HELLO WORLD'   # 0 1 2 3 4 5 6
print(message)

print("----String with for loop--------")
for char in message:
    print(char)

print("----String with for loop--------")
for char in message[0:5]:
    print(char)

print("----String with for loop--------")
for char in message[::-1]:
    print(char)

# SEQUENCE OPERATIONS
message = 'HELLO WORLD'
print("----------1. Indexing---------")
# 1. Indexing:
print("4th index : ", message[4])
print("7th index : ", message[7])
print("9th index : ", message[9])
print("9th index : ", message[-2])
print("10th index : ", message[10])
print("10th index : ", message[-1])


print("----------2. Slicing---------")
# 2. Slicing :
message = 'HELLO-WORLD'
print("2 to 5 : ", message[2:5])
print("3 to 7 : ", message[3:7])
print("-9 to 5 : ", message[-9:5])

print("----------3. Adding---------")
# 3. Adding :
str1 = 'Hello'
str2 = 'World'
print("Addition :", str1 + str2)
print("Addition :", str2 + str1)

str1 = 'Hello '
str2 = 'World'
print("Addition :", str1 + str2)
print("Addition :", str2 + str1)


print("----------3. Multiplying---------")
# 4. Multiplying
str1 = 'HELLO '
print(str1[3])
print("Multiplication :", str1 * 5)

print("----------4. Membership ---------")
# 5. Checking for membership
msg1 = 'HELLO-PYTHON'

print("H  : ", 'H' in msg1)
print("L  : ", 'L' in 'HELLO-PYTHON')
print("LL  : ", 'LL' in 'HELLO-PYTHON')
print("PH  : ", 'PH' in 'HELLO-PYTHON')
print("-  : ", '-' in 'HELLO-PYTHON')
print("Space  : ", ' ' in 'HELLO PYTHON')
print("B  : ", 'B' not in 'HELLO PYTHON')
message = 'HELLO-PYTHON'
print('H' in message)
print('L' in message)

str1 = 'HelloWorld'  # Refer ASCII table  A-Z 65-90    a-z 97....122

print("----------6. Length ---------")
# 6. len()
print("Length of string : ", len(str1))
#7. max()
print("----------7. Max ---------")
print("Max of string : ", max(str1))

#8. min()
print("----------8. Min ---------")
print("Min of string : ", min(str1))
#mutable
x = 100
print(10)
print(10+20)
print(x)
#
x = 10
print("First  :", x)
x = 20
print("Second :", x)
#
x = 10
print(x)
x = x + 10
print(x)
#
msg = 'Hello'
print("Message : ", msg)
msg = 'World'
print("Message : ", msg)

msg = 'Hello'
print("Message : ", msg)
msg = msg + 'World'
print("Message : ", msg)