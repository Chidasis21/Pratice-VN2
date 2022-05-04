x = 10
y = float(x)
print(type(x), type(y), x, y)
# Explicit casting:
a = 10.5
b = int(a)
print(type(a), type(b), a, b)
# integer
x = 100
print(x)
id(x)
type(x)

# float
a = 124.55
print(a, type(a))

# boolean
y = True
z = False
print(id(y), id(z))
#
name = "shyam123566"
print(type(name), id(name))
#
x = [1, 2, 10.5, True, "string"]
print(x, type(x), id(x))
print(id(x[1]))
#
x = 11
print(x)
x =y =z = 10
print(id(x), id(y), id(z))
x = 100
x = 200
x = 300
print(x)