number = int(input("Enter the size of the pattern: "))
for row in range (1, number + 1):
    for col in range (1, number + 1):
        print("*", end="")
    print()
