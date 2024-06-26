num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
        case '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}.")
        
        case '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}.")
        
        case '*':
          result = num1 * num2
          print(f"The result of {num1} * {num2} is {result}.")
        
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}.")
            else:
                print("Error: Division by zero is not allowed.")
