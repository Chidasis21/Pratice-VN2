#capitalize
print("------------- 1. capitalize() -----------------")
print("capitalize() : capitalizes first letter of given input string")

str1 = 'python'
print("Normal string           :", str1)
str1.capitalize() # No action here
print("String after capitalize :", str1.capitalize())   # print(10)
# str1 = str1.capitalize()                  # x = 10
print("String after capitalize :", str1)    # print(x)

'''3 Ways'''
print("----Way 1--------")
# 1 : Current string should be used as is, new string used "one time"
str1 = 'python'
print("String     : ", str1)
print("Capitalize : ", str1.capitalize())  # print(10)
print("String     : ", str1)

# 2 : Current string should be used as is, new string used in "multiple places"
print("----Way 2--------")
str1 = 'python'
print("String     : ", str1)
str2 = str1.capitalize()         # x = 10
print("String     : ", str1)
print("String     : ", str2)     # print(x)

# 3 : Current string should get modified
print("----Way 3--------")
str1 = 'python'
print("String     : ", str1)
str1 = str1.capitalize()
print("String     : ", str1)

print("--------------------------------------")

#center
print("------------- 2. center() -----------------")

print("center() : returns center padded string with mentioned length")

str1 = 'hello world'
str2 = 'hello world welcome'
print("Normal string                                                :", str1)
print("Length after padding : ",len(str1.center(28, '$')))
print("String after center function with width 28 & fillchar as $   :", str1.center(28, '^'))
print("String after center function with width 28 & fillchar as $   :", str2.center(28, '^'))
print("String after center function with width 24                   :", str1.center(24))
print("-------------------------------------------------------------------------------------")

from collections import defaultdict

d = defaultdict(str)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
print(d['id'])

#count

# 3. count() : Counts how many times str occurs in string or in a substring of string.
str1 = 'hello world'
print("------------- 3. count() -----------------")
print('count() : Counts how many times str occurs in string or in a substring of string.')

str1 = 'helloworldhell'
print("Slicing :", str1[0:10])
print("Normal string : o  ", str1.count('o'))
print("Normal string : l  ", str1.count('l'))
print("Normal string : he ", str1.count('he'))
print("Normal string : world ", str1.count('world'))
print("Normal string : name  ", str1.count('name'))
print("Normal string : l  ", str1.count('l', 0, 10))

print("Normal string                           :", str1)

print("Number of e's in the total string are   :", str1.count('e', 0, 14))
print("Number of x's in the total string are   :", str1.count('x', 0, 13))
print("-------------------------------------------------------------------------------------")

print("Normal string                           :", str1)

print("Number of e's in the total string are   :", str1.count('e', 0, 14))
print("Number of x's in the total string are   :", str1.count('x', 0, 13))
print("-------------------------------------------------------------------------------------")
#encode
str1 = 'hello world'
str2 = str1.encode('UTF-8', 'strict')
print("------------- 4. decode() -----------------")
print('decode() : Decodes the string using the codec registered for encoding..')

print("Encoded string        :", str2)
print("Decoded string        :", str2.decode('UTF-8', 'strict'))

str1 = 'hello'
str2 = str1.encode()
print("Normal  : ",str1 )
print("Encoded : ", str2)
print("Decoded : ", str2.decode())