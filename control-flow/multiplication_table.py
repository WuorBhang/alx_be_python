#prompt user number
number = int(input("Enter a number to see its multiplication table. "))


#looping from 1 to 10
for i in range(1, 10 + 1):
   product = number * i
   print(f"{number} * {i} = {product}")