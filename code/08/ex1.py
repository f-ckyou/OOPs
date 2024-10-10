from abc import ABC, abstractmethod

# Abstract class for Payment
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Encapsulated class for Credit Card
class CreditCard:
    def __init__(self, card_number, cardholder_name):
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name

    def get_card_info(self):
        return f"Cardholder: {self.__cardholder_name}"

# Subclass for Abstract Class
class CreditCardPayment(Payment):
    def __init__(self, credit_card):
        self.credit_card = credit_card

    def process_payment(self, amount):
        return f"Processed payment of ${amount} by {self.credit_card.get_card_info()}"


credit_card = CreditCard("1232-4589-6581-0008", "Zoro")
payment = CreditCardPayment(credit_card)

print(payment.process_payment(25.70))