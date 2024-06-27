# multiplication_table.py

def main():
    # Prompt User for a Number
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and Print the Multiplication Table
    for i in range(1, 10 + 1):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()
