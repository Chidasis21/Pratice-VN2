print("------Continue---------")

for val in range(1, 101):
    if val % 5 == 0:
        if val % 10 == 0:
            continue
        print(val)