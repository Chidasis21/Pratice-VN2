x = 10
print(x, id(x), type(x))
sal = 100.4
print(sal, id(sal), type(sal))

# int --> int()
x = 10.4
print("Before : ", x, type(x))
x = int(x)
print("After : ", x, type(x))

# float --> float()
x = 10
print("Before : ", x, type(x))
x = float(x)
print("After : ", x, type(x))

# bool --> bool()
x = 0
print("Before : ", x, type(x))
x = bool(x)
print("After : ", x, type(x))

# str --> str()   40+
mobile_no = 123456
print("Before : ", mobile_no, type(mobile_no))
mobile_no = str(mobile_no)  # "123456"
print("After : ", mobile_no, type(mobile_no))