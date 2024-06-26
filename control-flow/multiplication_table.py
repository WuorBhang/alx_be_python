#prompt user number
number = int(input("Enter a number to see its multiplication table. "))

#generate and print the multiplication table numbers
for i in range(1, 10 + 1):
   product = number * i
   print(f"{number} * {i} = {product}")