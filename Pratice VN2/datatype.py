#
x = 10
print(x)
#
x = y = z =10
print("x")
print("Type of x : ", type(x))
print("Id of x   : ", id(x))
#
x = 10 + 20 - 45 * 43 / 2
print("final value:", x)
print("Type of x : ", type(x))
print("Id of x   : ", id(x))

is_active = True
print("Type of is_active : ", type(is_active))
print("ID of is_active   : ", id(is_active))
#
x = 10
print("integer:", type(x), id(x))
y = 10.0
print("float:", type(y),id(y))
str = '10'
print("Type of str:", type(str), id(str))
# Type conversions
print("----Type conversions--------")
#
a = 0
print(bool(a))
print("converting int to float")
x = 10
print("value : ",x, type(x))
# Convert to float
y = float(x)
print("value : ",y, type(y))
print("converting int to boolean")
x = 0
print(x, type(x))
y = bool(x)
print(y, type(y))
print("-------------------")
x = 14
print(x, type(x))
x = bool(x)
print(x, type(x))
print("-------------------")
x = 0
print(x, type(x))
x = bool(x)
print(x, type(x))
#
eid = "10001"
print(eid, type(eid))
scan_code = 'abc32'
#
x = 300
y = 300
print(id(x), id(y))