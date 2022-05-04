#
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])  #int(), float()
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)
#
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

for d in Days:
   print(d)
#
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.discard(" ")
print("after discard:", Days)
#
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print("intersection of sets: ",AllDays)
#
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB # DaysB - DaysA

print("difference of sets: ", AllDays)
#
setA = set(["Mon","Tue","Wed"])
setB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = setA <= setB  # a set of which all the elements are contained in another set.
SupersetRes = setB >= setA  # a set which includes another set or sets.
print("setA is subset of setB: ", SubsetRes)
print("setB is superset of setA: ", SupersetRes)
#
s1 = {1, 2, 2, 2, 2, 4, 3, 5, 2, 7, 6}
print("Set 1 : ", s1)
#
s1 = {1, 1, 3, True, 'Hello', (1, 2, 3)}
print("Set is Mutable : ", s1)
#
'''s1 = {{1, 2, 3}, {1: 1, 2: 2}, [1, 2, 3]}
print("set is mutable :",s1)'''
# {}
s1 = {1}   # Dictionary
print(s1, type(s1))

s1 = set()
print(s1, type(s1))

s1 = set({})
print(s1, type(s1))

print("---------Iterate through set-----------")
s1 = {1, 2, 4, True, 'Hello', 'Python', (1, 2, 3)}
for each in s1:
    print(each)

print("------UPDATE---------")
#update datastructure
s1 = {1, 4, 5, 7, 2, 6, 3}
print("Before add ----", s1)
s1.add(100)
print("After add -----", s1)
#remove the element
s1.discard(5)
print("After discard--", s1)
#union
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Union -----------: ", s1 | s2)
print("Intersection-----: ", s1 & s2)
print("Minus-----: ", s1 - s2)
print("Minus-----: ", s2 - s1)