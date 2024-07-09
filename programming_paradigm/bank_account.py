class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

# This part below is to test the class functionality (Optional)
# if __name__ == "__main__":
#     account = BankAccount(100)
#     account.deposit(50)
#     account.withdraw(30)
#     account.display_balance()
