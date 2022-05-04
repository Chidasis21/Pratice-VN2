#list
x = 10
x = 10.5
is_bool = True
msg = 'Hello World'

list1 = [1, 1, 2, 3, 4, 5, 6]
print("List data structure :", list1)
#
print("----------Homegeneous---------")
list1 = [1, 1, 2, 3, 4, 5, 6]
print('Integers is list : ', list1)

list1 = [1.5, 3.2, 5.6, 4.8]
print('Float is list   : ', list1)

list1 = [True, False, True, False]
print('Boolean is list : ', list1)

list1 = ['hello', ' world', 'welcome', 'python']
print('Strings is list : ', list1)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Lists   is list : ', list1)

list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('Tuples  is list : ', list1)

list1 = [{1: 1, 2: 2}, {'id': 100, 'name': 'Madhu'}]
print('Dict    is list : ', list1)

list1 = [{1, 2, 3}, {4, 5, 6}]
print('Set is list : ', list1)

    # Hetero
list1 = [100, 14.5, False, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {1, 2, 3}]
print("---Hetero-------", list1)

# 2. List allows duplicate elements
list1 = [10, 10, 20]
print("Duplicates in list : ", list1)

# 3. Insertion order maintains
list1 = [1, 2, 3, 4, 5, 6]
print("Insertion order: ", list1)

# 4. List is mutable
print("----List is MUTABLE-----")
list1 = [12, 22, 13, 54, 35]
      #  0   1    2   3   4
print("Before list : ", list1)
list1[2] = 300
print("After list  : ", list1)

# 5. Follow indexing mechanism
list1 = [12, 22, 13, 54, 35]
#
print("---------------------- LIST: SEQUENCE OPERATIONS ---------------------")
list1 = [1, 1.5, True, 'HelloWorld', 234]
       # 0   1    2       3           4

# Indexing
print("Indexing : ", list1)
print("Indexing : ", list1[1])
print("Indexing : ", list1[3], list1[-2])
print("Get o in list1 :", list1[3], list1[3][4])

# Slicing
print("Slicing : ", list1)
print("Slicing : ", list1[0:4])

# Adding
print("Adding 2 lists :", [1, 2, 3] + [4, 5, 6])
#Mulitiplying
print("Mulitply 2 lists :", [1, 2, 3] * 2)
# Membership
print("Check value : ", 1 in [1, 2, 3])
# len
print(list1)
print("Length of list1 : ", len(list1))
list2 = [1,2,3,100]
# max
print("max of list1 : ",max(list2))
# min
print("min of list1 : ",min(list2))


list1 = [1, 2, 3, 4, 5]
list2 = [True, False, False]
list3 = ['Hello', 'World', 'python']
list3 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(list3[0][2])


list4 = [(1, 2), (3, 4, 5)]
list5 = [{1: 1, 2: 2}, {1: 'Madhu', 2: 'Nethra'}, {}]
list6 = [{1, 2, 3}, {4, 5, 6}]

print("-----------List3 operations---------")
list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("List3 : ", list3[0])
print("List3 : ", list3[0][1])
print("List3 : ", list3[0:1])
print("List3 : ", list3[1][2])
#sequential operation
list1 = [12, 22, 13, 54, 35, 76, 14]
print("List1 : ", list1)

# 1. Sequence operations

print("----------1. Indexing-------------")
'''                                                                     
    [12, 22, 13, 54, 35, 76, 14]   1 2 3 4 5 6 7 8 9 10 
      0  1   2   3   4   5   6    
'''
print("List1 1    : ", list1[1])
print("List1 5,-1 : ", list1[5], list1[6], list1[-1])

print("----------2. Slicing-------------")
print("Slicing operation : ", list1[2:])
print("Slicing operation : ", list1[2:5])
print("Slicing operation : ", list1[:5])
print("Slicing operation : ", list1[::1])
print("Slicing operation : ", list1[::2])

print("----------3. Adding-------------")
print("Adding 2 lists    :", [1, 2, 3] + [4, 5, 6])  # print(10+20) [1,2,3,4,5,6]
list1 = [10, 20, 30]
list2 = [11, 12, 13]
print("Adding 2 lists    :", list2+list2)   # x=10 y= 20   print(x+y)


print("----------4. Multiplying-------------")
print("Multiply 2 lists :", [1, 2, 3] * 5)

print("----------5. Membership-------------")
print("Check value : ", 1 in [1, 2, 3])
print("Check value : ", 10 in list1)

print("----------6. length-------------")
print("Length of list1 : ", len(list1))

print("----------7. max-------------")
print("Length of list1 : ", max(list1))

print("----------8. min-------------")
print("Length of list1 : ", min(list1))
#Conversion

# Conversions
x = 10
print("To float : ", float(x), type(x))
x = 10.5
print("To int  : ", int(x), type(x))
x = 0
print("To bool : ", bool(x), type(x))
x = -5
print("To bool : ", bool(x), type(x))

x = 12345
print("To str  : ", x, type(x))
x = str(x)
print("To str  : ", x, type(x))


str1 = 'Hello World'
print("Convert to list : ", list(str1))

list1 = [1, 2, 3, 4, 5, 6]
print("List to string : ", list1, type(list1))
st = str(list1)
print("List to string : ", st, type(st))  # "[1, 2, 3, 4, 5, 6]"

list1 = ['a', 'b', 'c']
num_str = '10'.join(list1)
print(num_str, type(num_str))
num_str = ' '.join(list1)
print(num_str, type(num_str))

# String is immutable
msg = 'Hello'
print("Before string : ", msg)
msg = 'World'
print("After string  : ", msg)

# List is mutable
list1 = [32, 12, 35, 76, 43, 52, 15]
print(id(list1))
list1[2] = 333
print("after update element:", id(list1))

print("Before list :   ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))
list1[1] = 1000
print("After list  : ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))

# CRUD Operations
# 1. CREATE
list1 = [1, 2, 3, 4, 5, 6]

list1 = [1, 2, [30, 40, 50], (11, 22, 33), {1, 2, 3}, {1: 100, 2: 200}]
# 2. RETRIEVE
print('List values1 : ', list1)
print('List values2 : ', list1[2])
print('List values21 : ', list1[2][1])

# 3. UPDATE
list1[1] = 200
print('List values2 : ', list1)

# 4. DELETE
del list1[2][2]
print('List values3 : ', list1)
del list1
#print('List values4 : ', list1)

# copy - shallow copy/ deep copy

list1 = [1,2,4]
list2 = list1.copy()
print(list1, list2)

print("after append")

list1.append(100)
print(list1, list2)

print("after append list2 ")

list2.append(20)
print(list1, list2)
print("deep copy==============")

list1 = list2 # deep copy

list1.append(200)
print(list1, list2)

# shallow copy made changes to original
# deep copy doesn't change original source

from copy import copy, deepcopy
list1 = [1,2,4]
list2 = copy(list1)  # shallow copy

list1.append("mani")
print(list1, list2)

list3 = deepcopy(list1)
list1.append(22)
print(list1, list3)

# list is mutable
# tuple is immutable

list1 = [1, 2, 3, 4, 5, 6]
'''
# Builtin functions:
---------------------
append insert extend   : UPDATE
pop  remove            : DELETE 
count                  : RETRIEVE
index                  : RETRIEVE
reverse                : UPDATE 
sort                   : UPDATE
copy                   : CREATE
'''
# 1. append(): It appends element(any value) at end of the list
             # list1.append(obj) Appends any object obj to list
list1 = [1, 2, 3, 4, 5, 6]
print("Before append : ", list1)
list1.append(10)
print("After append  : ", list1)
list1.append(10.4)
list1.append(True)
list1.append('Hello')
list1.append([1, 2, 3])
list1.append((10, 20, 30))
list1.append({1: 1})
list1.append({100, 200, 300})
print(list1)

for i in list1:
    print(i)


for ind, val in enumerate(list1):
    print(ind, "----", val)

print("After append  :", list1)


# extend  : only sequence str,list,tuple
         #: list1.extend(seq)         Appends the contents of seq to list

list1 = [1, 2, 3, 4, 5, 6]
print("Before extend : ", list1)
# append([10,20,30]) :       ==> [1,2,3,4,5,6, [10,20,30]]
list1.extend([10, 20, 30, ['a', 'v']])#==> [1,2,3,4,5,6,10,20,30]]
print("After extend  : ", list1)
list1.extend('Hello World')
list1.extend((1, 2, 3))
print("After extend  : ", list1)


# append vs extend

list1 = [1, 2, 3]
list1.insert(1, 200)
print(list1)
list1.append([10, 20])    # [1, 2, 3, [10,20]]
list1.extend([100, 200])  # # [1, 2, 3, [10,20], 100, 200]
print("List after append,extend : ", list1)

# 3. pop# list.pop(obj=list[-1]) Removes and returns last object or obj from list
list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before pop   : ", list1)
list1.pop(3)  # index
print("After  pop   : ", list1)  # [23, 12, 46, 14, 7, 2, 19, 25]
print(list1.pop())
print("After  pop   : ", list1)  # [23, 12, 46, 14, 7, 2, 19]

rem_ele = list1.pop(0)
print("Popped element : ", rem_ele)
print("After  pop   : ", list1)

# 4. remove
            # list.remove(obj)    Removes object obj from list
list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before removal : ", list1)
list1.remove(34)
print("After removal  : ", list1)

list1 = [23, 14, 12, 46, 34, 14, 7, 2, 14, 19, 25]
print("Before removal : ", list1)
list1.remove(14)
list1.pop(5)
print("After removal  : ",list1)

# 5.list.insert(index, obj)  Inserts object obj into list at offset index
list1 = [1, 2, 3, 4, 5]
print("Before index : ", list1)
list1[0] = 150  # [150, 2, 3, 4, 5]  Replace the value in index
print("After index   : ", list1)
list1.insert(0, 100)  # [100, 150, 2, 3, 4, 5] Insert the value in index
print("After insert  : ", list1)
list1.insert(3, 100)
print("After insert   : ", list1)

# 6. count ==> list.count(obj)Returns count of how many times obj occurs in list
list1 = [1, 1, 3, 2, 3, 2, 4, 5, 3, 2, 1]
print("List count 5: ", list1.count(5))

# 7. index  ==> list.index(obj) Returns the lowest index in list that obj appears
list1 = [23, 76,13, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]
print("List index : ", list1.index(13))

# 8. reverse ==> list.reverse()  Reverses objects of list in place
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print("List after reverse : ", list1)

# 9. sort ==> list.sort(obj)Sorts the elements
list1 = [23, 76, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]
list1.sort()  # ascending order
print("List sort ascending : ", list1)

list1.sort(reverse=True)  # descending order
print("List sort descending: ",list1)

# 10. copy()

list1 = [1, 2, 3, 4, 5]
print("Before copy list1    : ", list1)
list2 = list1.copy() # individual copy
print("After copy list2     : ", list2)
print("Normal copy function : ", id(list1), id(list2))
list1.append(100)

print("After append : list1 :", list1)
print("After append : list2 :", list2)

# 2nd way of copy

list1 = [1, 2, 3, 4, 5]
list2 = list1
print("Variable  copy : ", id(list1),id(list2))
list1.append(100)
print("After var copy :", list1,list2)
list2.extend([11,22])
print("After var copy :", list1,list2)