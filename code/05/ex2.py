# How can encapsulation help ensure validation of input when setting attributes?

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private attribute

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid balance!")
        else:
            self.__balance = amount

# Create an object of BankAccount with initial balance
account = BankAccount(1000)

# Access the balance using getter
print("Current balance:", account.balance)  # Output: 1000

# Try to set an invalid balance 
account.balance = -500  # Output: Invalid balance!

# Set a valid balance
account.balance = 2000  # Use the setter to update the balance
print("Updated balance:", account.balance)  # Output: 2000
