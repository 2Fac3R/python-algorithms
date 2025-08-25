
from abc import ABC, abstractmethod

"""
Challenge: Payment Processing with Strategy Pattern

Design a payment processing system for a shopping cart. The system should support different payment methods
(e.g., Credit Card, PayPal) and allow the payment method to be selected or changed at runtime.

Your task is to:
1.  Define an abstract `PaymentStrategy` class (Strategy interface) with an abstract `pay(amount: float)` method.
2.  Implement concrete strategy classes:
    -   `CreditCardPayment`: Implements `PaymentStrategy` for credit card payments. Its constructor should take card details (e.g., `card_number`, `cvv`, `expiry_date`). Its `pay` method should return a string indicating payment with the credit card.
    -   `PayPalPayment`: Implements `PaymentStrategy` for PayPal payments. Its constructor should take PayPal account details (e.g., `email`, `password`). Its `pay` method should return a string indicating payment with the PayPal account.
3.  Implement a `ShoppingCart` class (Context) with:
    -   A private attribute `_payment_strategy` to hold the currently selected payment strategy.
    -   An `__init__` method that takes an initial `PaymentStrategy`.
    -   A `set_payment_strategy(payment_strategy: PaymentStrategy)` method to change the strategy at runtime.
    -   An `add_item(item: str, price: float)` method to add items to the cart.
    -   A `checkout()` method that calculates the total amount and delegates the payment to the current `_payment_strategy`.

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
        # TODO: Implement payment logic for Credit Card
        pass

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def pay(self, amount: float) -> str:
        # TODO: Implement payment logic for PayPal
        pass

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
        # TODO: Delegate payment to the current strategy
        pass


# --- Tests ---
def run_tests():
    print("Running Strategy Pattern Payment Processing Tests...")

    # Test 1: Pay with Credit Card
    credit_card_strategy = CreditCardPayment("1234-5678-9012-3456", "123", "12/25")
    cart1 = ShoppingCart(credit_card_strategy)
    cart1.add_item("Laptop", 1200.00)
    cart1.add_item("Mouse", 25.00)
    expected_output1 = "Paying $1225.00 using Credit Card 3456"
    assert cart1.checkout() == expected_output1, f"Test 1 Failed: Expected '{expected_output1}', Got '{cart1.checkout()}'"
    print("Test 1 (Credit Card) Passed.")

    # Test 2: Pay with PayPal
    paypal_strategy = PayPalPayment("user@example.com", "mysecretpassword")
    cart2 = ShoppingCart(paypal_strategy)
    cart2.add_item("Keyboard", 75.00)
    cart2.add_item("Monitor", 300.00)
    expected_output2 = "Paying $375.00 using PayPal account user@example.com"
    assert cart2.checkout() == expected_output2, f"Test 2 Failed: Expected '{expected_output2}', Got '{cart2.checkout()}'"
    print("Test 2 (PayPal) Passed.")

    # Test 3: Change strategy at runtime
    cart3 = ShoppingCart(credit_card_strategy) # Start with credit card
    cart3.add_item("Headphones", 150.00)
    assert cart3.checkout() == "Paying $150.00 using Credit Card 3456"
    cart3.set_payment_strategy(paypal_strategy) # Change to PayPal
    cart3.add_item("Microphone", 50.00)
    # Total is now 150 (headphones) + 50 (microphone) = 200
    assert cart3.checkout() == "Paying $200.00 using PayPal account user@example.com"
    print("Test 3 (Runtime Strategy Change) Passed.")

    print("All Strategy Pattern Payment Processing Tests Passed!")

if __name__ == "__main__":
    run_tests()
