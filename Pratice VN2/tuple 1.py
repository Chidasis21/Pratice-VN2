#memory allocation
x = 10
print(x)
print(20)
print(10+20)
#
li1 = [1, 2, 3, 4]
tup1 = (1, 2, 3, 4)
print(tup1, type(tup1))
x = tup1.index(1)
y = li1.append(12)
print("index position of x:", x)
tup1 = ()
print("Empty tuple :", tup1, type(tup1))

tup1 = ('a',)
print("Empty tuple :", tup1, type(tup1))

tup1 = (1,)
print("Empty tuple :", tup1, type(tup1))
#
str ="hello world"  #  elemnts
lst = [13, 67, 98]
tup = (22, 24, 67)

for i in str:   # iterations
    print(i)

for each in lst:
    print(each)

for ele in tup:
    print(ele)

for num in range(0, 100, 5):
    print(num)
#
tup1 = (1, 2, 3, 4, 5, 6, 7, 234)

# Indexing # RETRIEVAL
print("Indexing : ", tup1[7]) # [pass index position getting value]

# Slicing
print("Slicing : ", tup1[0:7])

# Adding
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Tuple1 : ", t1)
print("Adding : ", t1 + (t2))
t1 = t1 + t2
print("Tuple1 : ", t1)

# Multiplying
t1 = (1, 2, 3)
print("Mulitiplye : ", t1*3)
# Membership
t1 = (1, 2, 3, 4, 67)
print("Membership : ", 1 not in t1)
print("Length : ", len(t1))
print("Max : ", max(t1))
print("Min : ", min(t1))

#len() max() min()
t1 = (1, 2, 3, 4, 5)

#t1 = t1.append(10)  # ERROR Tuple is immutable
print(t1)
t1 = (1, 2, 3, [4, 5, 6], 7)
# t1[3] = 100 # ERROR
print("Before -- ", t1)

t1[3].append(100)

print("After -- ", t1)

t2 = list(t1)
print(t2)

#Functions
list1 = [1, 2, 3, 4]
print("Before : ", list1, type(list1))
tup1 = tuple(list1)
print("After : ", tup1, type(tup1))


t1 = (10, 43, 2, 532, 53, 64, 24, 25, 53)
print("Iterate the tuple")
for each in t1:
    print(each)

le = len(t1) # 9 elements
for i in range(len(t1)):  # range(9) 0123456789
    print(i, " : ", t1[i])

# Find index of 64
t1 = (10, 43, 2, 532, 53, 64, 24, 25, 24, 10,  53, 10)
print("length of t1",len(t1))

for i in range(len(t1)):  # lengrh - 12 range(12)
    if t1[i] == 64:
        print("Index is : ", i)

print("Count : ", t1.count(10))

print("Index : ", t1.index(64))  # print(t1[5])

list1 = [1, 2, 3]
print("Before : ", list1)
list1.append(10)
print("After  : ", list1)
# return type
# pop() remove()
print("List pop :", list1.pop(2))  # index position
print(list1)
print("List remove :", list1.remove(10))  # value
print(list1)

tup1 = (1,4,[2,3])
tup1[2].append(100)
print(tup1)