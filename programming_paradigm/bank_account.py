class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew: ${amount:.2f}"

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"

# Checks for Implementation
def test_bank_account():
    account = BankAccount(250)  # Start with an initial balance of $250.00

    # Check that "Current Balance:" is in display_balance method
    assert "Current Balance: $" in account.display_balance(), "The string 'Current Balance: $' should be in the display_balance method"

    # Check deposit
    assert account.deposit(100) == "Deposited: $100.00", "Deposit method failed"

    # Check withdrawal
    assert account.withdraw(50) == "Withdrew: $50.00", "Withdrawal method failed"

    # Check withdrawal more than balance
    assert account.withdraw(670) == "Insufficient funds.", "Insufficient funds check failed"

    # Check display balance
    assert account.display_balance() == "Current Balance: $300.00", "Display balance method failed"

# Run tests
test_bank_account()

# This part below is to test the class functionality (Optional)
# if __name__ == "__main__":
#     account = BankAccount(100)
#     account.deposit(50)
#     account.withdraw(30)
#     account.display_balance()
