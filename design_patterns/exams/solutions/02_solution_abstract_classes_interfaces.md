# Solutions: Exam - Abstract Classes and Interfaces in Python

---

### Question 1 (Abstract Class Purpose)

What is the primary purpose of an abstract class in Python, and what is a key characteristic that distinguishes it from a regular class?

-   **Answer:** The primary purpose of an abstract class in Python is to define a common interface (a contract) for a set of subclasses, often providing a partial implementation of its methods. A key characteristic that distinguishes it from a regular class is that **an abstract class cannot be instantiated directly**. You must create a concrete subclass that implements all its abstract methods before you can create an object.

---

### Question 2 (Defining Abstract Methods)

How do you define an abstract method in Python, and what happens if a concrete subclass fails to implement all abstract methods from its abstract base class?

-   **Answer:**
    -   **Defining an abstract method:** You define an abstract method in Python by inheriting the class from `abc.ABC` and decorating the method with `@abstractmethod`.
        ```python
        from abc import ABC, abstractmethod

        class MyAbstractClass(ABC):
            @abstractmethod
            def abstract_method(self):
                pass
        ```
    -   **Consequence of non-implementation:** If a concrete subclass fails to implement all abstract methods from its abstract base class, that subclass itself will also be considered an abstract class. This means you will not be able to instantiate it, and attempting to do so will result in a `TypeError`.

---

### Question 3 (Interfaces in Python)

Python does not have an explicit `interface` keyword. Explain how the concept of an interface is achieved in Python, mentioning two common approaches.

-   **Answer:** In Python, the concept of an interface is achieved primarily through:
    1.  **Abstract Base Classes (ABCs) from the `abc` module:** When an ABC contains *only* abstract methods (and no concrete implementations or instance attributes), it effectively acts as an interface. Subclasses are then formally obligated to implement all these abstract methods to become concrete. This provides a clear contract.
        ```python
        from abc import ABC, abstractmethod

        class Drawable(ABC):
            @abstractmethod
            def draw(self): pass

        class Circle(Drawable):
            def draw(self): return "Drawing a circle"
        ```
    2.  **Duck Typing:** This is Python's more idiomatic way of achieving polymorphism and interface-like behavior. If an object "walks like a duck and quacks like a duck" (i.e., it has the methods and attributes expected by the client code), then it can be used, regardless of its formal inheritance hierarchy. There's no explicit declaration of an interface, just an implicit expectation of behavior.
        ```python
        class Duck:
            def quack(self): return "Quack!"
        class Person:
            def quack(self): return "I can quack!"

        def make_it_quack(obj): return obj.quack()

        print(make_it_quack(Duck()))
        print(make_it_quack(Person()))
        ```

---

### Question 4 (Scenario: Payment Gateway)

Imagine you are building a payment processing system. You need to integrate with various payment gateways (e.g., PayPal, Stripe, Square), each with its own way of processing payments. You want to ensure that any new payment gateway added to the system adheres to a common contract, and that your core payment logic can work with any gateway without knowing its specific implementation details.

How would you use abstract classes or ABCs in Python to design a flexible and extensible payment gateway integration, demonstrating the definition of a common interface and a concrete implementation?

-   **Answer:**
    1.  **Define an Abstract Base Class (Interface):** Create an ABC called `PaymentGateway` that defines the common contract for all payment gateways. It would have abstract methods like `process_payment(amount: float, currency: str)` and `refund_payment(transaction_id: str)`.
        ```python
        from abc import ABC, abstractmethod

        class PaymentGateway(ABC):
            @abstractmethod
            def process_payment(self, amount: float, currency: str) -> str:
                pass

            @abstractmethod
            def refund_payment(self, transaction_id: str) -> str:
                pass
        ```
    2.  **Implement Concrete Payment Gateways:** Create concrete classes for each payment gateway (e.g., `PayPalGateway`, `StripeGateway`) that inherit from `PaymentGateway` and provide their specific implementations for `process_payment` and `refund_payment`.
        ```python
        class PayPalGateway(PaymentGateway):
            def process_payment(self, amount: float, currency: str) -> str:
                return f"Processing ${amount} {currency} via PayPal."

            def refund_payment(self, transaction_id: str) -> str:
                return f"Refunding PayPal transaction {transaction_id}."

        class StripeGateway(PaymentGateway):
            def process_payment(self, amount: float, currency: str) -> str:
                return f"Processing ${amount} {currency} via Stripe."

            def refund_payment(self, transaction_id: str) -> str:
                return f"Refunding Stripe transaction {transaction_id}."
        ```
    3.  **Core Payment Logic (Client):** Your core payment logic (e.g., in a `PaymentProcessor` class) would depend only on the `PaymentGateway` ABC, not on specific implementations. This allows you to swap gateways easily.
        ```python
        class PaymentProcessor:
            def __init__(self, gateway: PaymentGateway):
                self.gateway = gateway

            def make_purchase(self, amount: float, currency: str) -> str:
                return self.gateway.process_payment(amount, currency)

            def issue_refund(self, transaction_id: str) -> str:
                return self.gateway.refund_payment(transaction_id)
        ```
    This design ensures that any new payment gateway must adhere to the `PaymentGateway` contract, and the `PaymentProcessor` remains flexible and decoupled from the specific gateway implementations.