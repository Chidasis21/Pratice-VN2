num = 1
count = 0
while num <= 100:
    if num % 2 == 0:
        print(num)
        count += 1
        if count == 7:
            break
    num += 1
print("End of while loop")
#
print("----Print only first 7 numbers-------")
num = 1
counter = 0
while num <= 100:
    if counter > 7:
        break
    if num % 2 == 0:
        print(num)
        counter += 1
    num += 1
print("Exited while loop")


print("--------Using for loop-------------")
#
counter = 0
for val in range(1, 101):
    if val % 2 == 0:
        print(val)
        counter += 1
        if counter == 7:
            break
print("-----End of for loop-----")

print("----Other program-------")
# Print even numbers between 50 to 80
for val in range(1,101):
    if val >= 50 and val <= 80:
        if val % 2 == 0:
            print(val)
    elif val > 80:
        break
print("End of for loop")
