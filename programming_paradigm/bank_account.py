# bank_account.py

class BankAccount:
    """A simple bank account class that supports basic banking operations."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if funds are sufficient."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")