x = (10+25-30)

print(x)
print(type(x))
print(id(x))

y = True
print(type(y))
print(id(y))
#
z = "str"
print(id(z), type(z))
#
a = 120.56
print(type(a), id(a))
print(x)  # read operation retrieving
#
x = 10  #when value has reference count
y = 10
z = 10

x = 100
x = 10
_name = 10
eid = 11
#
x =100
print(x)
#
x = y = 10     # one value to multiple variables
print(id(x),id(y) )
#
x = 20
print(id(x))
#
x = 10
print(id(x),type(x), x) # if ref count = o moves to garbage collection
x = 10
#
x =0.4
y = 0.2
print(id(x))
print(id(y))
sum = x+y
print(sum, id(sum))