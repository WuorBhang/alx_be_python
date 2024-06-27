number = int(input("Enter the size of the pattern: "))
row = 1
while row <= number:
    col = 1
    while col <= number:
        print("*", end="")
        col += 1
    print()
    row += 1
