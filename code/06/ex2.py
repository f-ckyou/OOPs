class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance is {self.balance}")

class SavingsAccount(Account):
    def add_interest(self):
        interest = self.balance * 0.02
        self.balance += interest
        print(f"Interest added, new balance is {self.balance}")

savings = SavingsAccount(187, 2000)
savings.deposit(500) # # Output: Deposited 500, new balance is 2500
savings.add_interest() # Output: Interest added, new balance is 2550