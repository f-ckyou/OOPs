from abc import ABC, abstractmethod

# Abstract class for ShoppingCart
class ShoppingCart(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def checkout(self):
        pass

# Encapsulated class for Item
class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

# Subclass for UserCart implementing the abstract methods
class UserCart(ShoppingCart):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if isinstance(item, Item): # ensures that only valid items can be added
            self.items.append(item)
            return f"{item.get_name()} for ${item.get_price()} has been added to the cart."

    def checkout(self):
        total = sum(item.get_price() for item in self.items)
        self.items.clear()  # Clear the cart after checkout
        return f"Checkout complete. Total amount: ${total}"

cart = UserCart()
item1 = Item("Laptop", 1199)
item2 = Item("Phone", 299)

print(cart.add_item(item1))  
print(cart.add_item(item2)) 
print(cart.checkout())   
