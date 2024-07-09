class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.display_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.display_balance()

    def display_balance(self):
        return f"Balance: {self.balance}"

# Checks for Implementation
def test_bank_account():
    # Check that "Current Balance:" is not in display_balance method
    account = BankAccount()
    assert "Current Balance:" not in account.display_balance(), "The string 'Current Balance:' should not be in the display_balance method"

    # Check deposit
    assert account.deposit(100) == "Balance: 100", "Deposit method failed"

    # Check withdrawal
    assert account.withdraw(50) == "Balance: 50", "Withdrawal method failed"

    # Check withdrawal more than balance
    assert account.withdraw(60) == "Insufficient funds", "Insufficient funds check failed"

    # Check display balance
    assert account.display_balance() == "Balance: 50", "Display balance method failed"

# Run tests
test_bank_account()


# This part below is to test the class functionality (Optional)
# if __name__ == "__main__":
#     account = BankAccount(100)
#     account.deposit(50)
#     account.withdraw(30)
#     account.display_balance()
