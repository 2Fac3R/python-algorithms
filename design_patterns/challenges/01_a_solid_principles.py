from abc import ABC, abstractmethod

"""
Challenge: SOLID Principles

This challenge aims to assess your understanding of the SOLID Principles.
You will identify violations and refactor the code to adhere to them.

Your task is to:

1.  **SRP (Single Responsibility Principle):**
    -   Refactor the `TaskManager` class so that each responsibility (task management, persistence, notification) is in its own class.

2.  **OCP (Open/Closed Principle):**
    -   Refactor the `calculate_total_discount` function so that it can handle new product types with different discount logics without modifying the existing function.

3.  **LSP (Liskov Substitution Principle):**
    -   Correct the `Bird` and `Penguin` class hierarchy so that `Penguin` does not violate LSP.

4.  **ISP (Interface Segregation Principle):**
    -   Refactor the `Worker` interface into smaller, more specific interfaces.

5.  **DIP (Dependency Inversion Principle):**
    -   Refactor `NotificationService` so that it depends on a `Messenger` abstraction instead of a concrete implementation.

"""

# 1. SRP (Single Responsibility Principle)
# Class violating SRP
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' added."

    def save_tasks(self, file):
        # Logic to save tasks to a file
        return f"Tasks saved to {file}."

    def send_task_notification(self, task):
        # Logic to send a notification
        return f"Notification sent for task '{task}'."

# TODO: Refactor TaskManager into separate classes for SRP
class TaskManagerSRP:
    pass

class TaskPersistence:
    pass

class TaskNotifier:
    pass


# 2. OCP (Open/Closed Principle)
# Function violating OCP
class StandardProduct:
    def __init__(self, price):
        self.price = price

class PremiumProduct:
    def __init__(self, price):
        self.price = price

def calculate_total_discount(products):
    total_discount = 0
    for p in products:
        if isinstance(p, StandardProduct):
            total_discount += p.price * 0.10 # 10% discount
        elif isinstance(p, PremiumProduct):
            total_discount += p.price * 0.20 # 20% discount
        # If a new product type is added, this function must be modified
    return total_discount

# TODO: Refactor to comply with OCP
class ProductOCP(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_discount(self):
        pass

class StandardProductOCP(ProductOCP):
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.price * 0.10

class PremiumProductOCP(ProductOCP):
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.price * 0.20

def calculate_total_discount_ocp(products):
    total_discount = 0
    for p in products:
        total_discount += p.get_discount()
    return total_discount


# 3. LSP (Liskov Substitution Principle)
# Hierarchy violating LSP
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly")

# TODO: Correct the hierarchy to comply with LSP
class BirdLSP:
    pass

class FlyingBirdLSP(BirdLSP):
    pass

class PenguinLSP(BirdLSP):
    pass


# 4. ISP (Interface Segregation Principle)
# Interface violating ISP
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

# TODO: Refactor Worker into smaller interfaces
class WorkerISP(ABC):
    pass

class EaterISP(ABC):
    pass

class SleeperISP(ABC):
    pass


# 5. DIP (Dependency Inversion Principle)
# Classes violating DIP
class EmailMessenger:
    def send(self, message):
        return f"Email sent: {message}"

class NotificationService:
    def __init__(self):
        self.messenger = EmailMessenger() # Direct dependency

    def notify(self, message):
        return self.messenger.send(message)

# TODO: Refactor to comply with DIP
class MessengerDIP(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailMessengerDIP(MessengerDIP):
    def send(self, message):
        return f"Email sent: {message}"

class NotificationServiceDIP:
    def __init__(self, messenger: MessengerDIP):
        self.messenger = messenger

    def notify(self, message):
        return self.messenger.send(message)


# --- Tests ---
def run_tests():
    print("Running SOLID Principles Challenge Tests...")

    # Test 1: SRP
    # Refactored classes are designed for SRP, direct assertion is hard without full implementation
    print("Test 1 (SRP) - Design inspection needed.")

    # Test 2: OCP
    products_ocp = [
        StandardProductOCP(100),
        PremiumProductOCP(200)
    ]
    assert calculate_total_discount_ocp(products_ocp) == (100 * 0.10) + (200 * 0.20)
    # Add a new product type to verify OCP
    class VIPProductOCP(ProductOCP):
        def __init__(self, price):
            self.price = price
        def get_price(self): return self.price
        def get_discount(self): return self.price * 0.30
    products_ocp.append(VIPProductOCP(300))
    assert calculate_total_discount_ocp(products_ocp) == (100 * 0.10) + (200 * 0.20) + (300 * 0.30)
    print("Test 2 (OCP) Passed.")

    # Test 3: LSP
    # This test relies on the corrected hierarchy in the solution
    class FlyingBirdTest(BirdLSP):
        def fly(self): return "Flying"
    class PenguinTest(BirdLSP):
        def swim(self): return "Swimming"

    birds = [FlyingBirdTest(), PenguinTest()]
    # No direct call to fly on BirdLSP, so LSP is not violated by PenguinTest
    print("Test 3 (LSP) - Design inspection needed. Assuming corrected hierarchy.")

    # Test 4: ISP
    # This test relies on the refactored interfaces in the solution
    print("Test 4 (ISP) - Design inspection needed.")

    # Test 5: DIP
    email_messenger_dip = EmailMessengerDIP()
    notification_service_dip = NotificationServiceDIP(email_messenger_dip)
    assert notification_service_dip.notify("Hello DIP!") == "Email sent: Hello DIP!"
    print("Test 5 (DIP) Passed.")

    print("All SOLID Principles Challenge Tests Passed!")

if __name__ == "__main__":
    run_tests()