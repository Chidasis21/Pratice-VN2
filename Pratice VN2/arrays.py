# from array import *
import array as arr

arr = arr.array('i',[12, 32, 43])  # Only Homogeneous data
print(arr, type(arr))

print("-------Iterate through each value-----")
for each in arr:
    print(each)

print("-------Iterate through each index-----")
for ind in range(len(arr)):
    print(arr[ind])

# Adding elements to array
my_arr.insert(1, 100)
print("After inserting : ", my_arr)

# Retrieve elements from array
print("Array elements : ", my_arr)
print("Array elements : ", my_arr[0])
print("Array elements : ", my_arr[1:2])

array = [1,10]
print(type(array), array)