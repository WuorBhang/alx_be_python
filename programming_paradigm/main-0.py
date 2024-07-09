import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py initial_balance")
        sys.exit(1)

    try:
        initial_balance = float(sys.argv[1])
    except ValueError:
        print("Invalid initial balance. Please enter a numeric value.")
        sys.exit(1)

    account = BankAccount(initial_balance)

    while True:
        print("\nBank Account Operations:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '2':
            try:
                amount = float(input("Enter withdrawal amount: "))
                if account.withdraw(amount):
                    print(f"Withdrawn: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
