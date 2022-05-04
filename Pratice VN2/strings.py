print("--------For loop with String-------")
msg = ['Hello World', 'mani']

for char in msg:
    print("Character : ", char)

list = ['Peter','Joseph','Ricky','Devansh']
for i in list:
    print("Hello",i)
#list
print("--------For loop with list-------")

list1 = [10, 32, 43, 13, 45, 65, 24, 75, 12]
for num in list1:
    print("Number : ", num)

emp_ids = [10, 32, 43, 13, 45, 65, 24, 75, 12]
for eid in emp_ids:  # eid e_id empid emp_id
    print("Employee id : ", eid)


for s_no in [10, 32, 43, 13, 45, 65, 24, 75, 12]:  # stu_no
    print("Student no : ", s_no)
#tuple
print("--------For loop with tuple-------")

list1 = (10, 32, 43, 13, 45, 65, 24, 75, 12)
for num in list1:
    print("Number : ", num)

emp_ids = (10, 32, 43, 13, 45, 65, 24, 75, 12)
for eid in emp_ids:  # eid e_id empid emp_id
    print("Employee id : ", eid)

stu_nos = (10, 32, 43, 13, 45, 65, 24, 75, 12)  # s_no

for s_no in stu_nos:  # stu_no
    print("Student no : ", s_no)
#range
print("----10------")
for val in range(10):  # 0 to 9
    print("Range val : ", val)
print("----5------")
for val in range(5):   # 0 to 4
    print("Range val : ", val)
print("-----0-----")
for val in range(0):
    print("Range val : ", val)
print("-----1-----")
for val in range(1):
    print("Range val : ", val)

print("----15 to 47----")
for val in range(15, 48):  # 15 to 47
    print("Range val: ", val)

print("----1 to 15----")   # 1 to 15
for val in range(1, 16):
    print("Range val: ", val)


print("----1 to 15 difference with 2----")
for val in range(1, 16, 2):
    print("Range val: ", val)


print("----1 to 30 difference with 3----")
for val in range(1, 31, 3):
    print("Range val: ", val)


print("-----Range with negative---------")
for val in range(20, 1, -1):
    print("Range val: ", val)

print("------ -20 to -40  1-------")
for val in range(-20, -40):
    print("Range val: ", val)

print("------ -20 to -40-------")
for val in range(-20, -40, -1):
    print("Range val: ", val)
#dict
print("-------For loop with dictionary--------")

emp_details = {'eid': 100,
               'ename': 'MadhuN',
               'sal': 12500}

print("------All Items-------")
for key, val in emp_details.items():
    print(key, val)

print("------All Keys-------")
for key in emp_details.keys():
    print(key)

print("------All Values-------")
for val in emp_details.values():
    print(val)

print("--------Only keys------")
for val in emp_details:
    print(val)
#set
print("-------For loop with set--------")
set1 = {1, 2, 3, 4, 5, 6}
for val in set1:
    print("Value : ", val)