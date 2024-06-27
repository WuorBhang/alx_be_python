# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

def print_table(number, i=1):
    if i > 10:
        return
    product = number * i
    print(f"{number} * {i} = {product}")
    print_table(number, i + 1)

# Call the recursive function to print the multiplication table
print_table(number)
