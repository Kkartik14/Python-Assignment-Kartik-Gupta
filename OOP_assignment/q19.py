# WAP to deposit or withdraw money in a bank account.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Error: Insufficient funds. Balance is {self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")

account = BankAccount(5000)
account.deposit(1000)
account.withdraw(2000)
