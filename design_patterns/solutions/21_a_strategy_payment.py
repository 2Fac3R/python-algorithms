
from abc import ABC, abstractmethod

"""
Solution for: Payment Processing with Strategy Pattern
"""

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str, expiry_date: str):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount: float) -> str:
        return f"Paying ${amount:.2f} using Credit Card {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def pay(self, amount: float) -> str:
        return f"Paying ${amount:.2f} using PayPal account {self.email}"

# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy
        self._items = []

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def add_item(self, item: str, price: float):
        self._items.append({"item": item, "price": price})

    def checkout(self) -> str:
        total_amount = sum(item["price"] for item in self._items)
        return self._payment_strategy.pay(total_amount)
