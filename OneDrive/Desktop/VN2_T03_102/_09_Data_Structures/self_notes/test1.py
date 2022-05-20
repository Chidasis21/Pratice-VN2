#
print("------------LIST------------")

list1 = [110, 23.5, True, 'Madhu', [1,2,3], (1,2), {1:10,2:20}, {1,2,3}]
print("List1 : ", id(list1))
print("Index 3rd  : ", id(list1[3])) 
print("Index : ", id(list1[3][1]))
print("Slice : ", list1[3][1:3])
#
print("------------TUPLE------------")

tup1 = (110, 23.5, True, 'Madhu', [1,2,3], (1,2), {1:10,2:20}, {1,2,3})
print("Tuple : ", tup1)
print("Index : ", tup1[3])
print("Index : ", id(tup1[3][1]) , id(tup1[3][-1]))
#
list1 = [1, 2, 3, 4, 5]
list2 = list1
print("Variable  copy : ", id(list1),id(list2))
list1.append(100)
print("After var copy :", list1,list2)
list2.extend([11,22])
print("After var copy :", list1,list2)
# list ex 1
lst1 = [10,20,-30,40,-50]
print(lst1,type(lst1))
#list ex 2
lst2 = [10,"CHIDA","BPUT",9.325,"OD",True]
print(lst2,type(lst2))
#list ex 3
lst3 = []
print(lst3,type(lst3),len(lst3))
#lst ex 4
lst4 = list()
print(lst4,type(lst4))
#lst ex 5
lst5 = [10,"CHIDA","BPUT",9.325,"OD",True]
print(lst5[1])
print(lst5[0:-4])
print(lst5[::])
print(lst5[:])
lst5.append("Megha")
print(lst5,id(lst5))
lst5.append(" W ")
print(lst5,id(lst5))
#lst ex 6
lst6 = [10,20,30,40,50]
print(lst6,type(lst6))
b = bytes(lst6)
print(b, bytes(b))
#for b in v:
 #   print("values:",v,end=",")
lst6 = lst6(b)
print(lst6,type(lst6))
#lst ex 7
lst7 = [10,"CHIDA",20,"Pycharm",50,60,3.26]
lst7.insert(2,"MEGHA")
print(lst7)
lst7.insert(-2,3.5)
print(lst7)
#lst ex 8
lst8 = [10,"CHIDA"]
lst8.append("PYTHON")
print(lst8)
print(lst8,id(lst8))
#lst ex 9
lst9 = [10,"HI",78,90.89,"Django",(1+7j)]
lst9.remove(78)
print(lst9)
lst9.pop(-1)
print(lst9)
lst9.pop()
print(lst9)
#lst ex 10
lst10 = [55,"Python","Chidasis","Django",True,(3+8j)]
print(len(lst10))
#
