# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
for i in range(1,11):
    print("{0} * {1} = {2}".format(number, i, (number * i)))
