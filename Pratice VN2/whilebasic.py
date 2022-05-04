print("--------Numbers from 1 to 10--------")

num = 1
while num <= 10:   # Check condition in each iteration
    print(num)
    num = num + 1  # num += 1

print("--------End of program--------")

num = 100
while num <= 150:
    print(num)
    num += 1
#
print("--------Print even numbers--------")
# STATE
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

num = 2
while num <= 100:
    if num % 2 == 0 and num % 4 == 0:
        print(num)
    num += 1


print("--------Print odd numbers--------")

# Print odd numbers betweeen 10 to 20
num = 10
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1

# Print numbers between 500 to 1000 and divisible by 5

print("--Numbers divisible  with 5------")
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1


# Print numbers between 500 to 1000. It should be divisible by 5 and divisible by 8
print("--Numbers divisible  with 5 and 8------")
num = 500
while num <= 600:
    if num % 5 == 0 and num % 8 == 0:
        print(num)
    num += 1

# Print numbers between 500 to 1000. It should be divisible by 5 or divisible by 9
print("--Numbers divisible  with 5 or 9------")
num = 500
while num <= 600:
    if num % 5 == 0 or num % 9 == 0:
        print(num)
    num += 1
#
print("--------Numbers div 5 or 8, not by 3 -----------")
# Numbers between 1 to 100 divisible by either 5 or 8, should not divisible 3
n1 = 1
n2 = 50
while n1 <= n2: #true
    if n1 % 5 == 0 or n1 % 8 == 0: # 15 True
        if n1 % 3 != 0:  # 15 / 3  False
            print(n1)

    n1 += 1
