num = int(input("Please enter a number: "))
for i in  range(num):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()