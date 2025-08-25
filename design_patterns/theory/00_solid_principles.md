# SOLID Principles

The SOLID principles are a set of five design principles intended to make software designs more understandable, flexible, and maintainable. They were promoted by Robert C. Martin (Uncle Bob).

---

## 1. Single Responsibility Principle (SRP)

### Definition
A class should have only one reason to change. This means a class should have only one job or responsibility.

### Problem it Solves
Prevents "God Objects" (classes that do too much), reduces coupling, and makes code easier to understand, test, and maintain. When a class has multiple responsibilities, a change to one responsibility might inadvertently affect another.

### Violation Example
```python
class Report:
    def __init__(self, data):
        self.data = data

    def generate_content(self):
        # Responsibility 1: Generate report content
        return f"Report Content: {self.data}"

    def format_html(self, content):
        # Responsibility 2: Format content for HTML
        return f"<html><body>{content}</body></html>"

    def save_to_file(self, filename, formatted_content):
        # Responsibility 3: Save content to a file
        with open(filename, 'w') as f:
            f.write(formatted_content)

# Usage
report = Report("Sales Data")
content = report.generate_content()
html_content = report.format_html(content)
report.save_to_file("sales_report.html", html_content)
```
**Violation:** The `Report` class has three reasons to change: if the content generation logic changes, if the HTML formatting changes, or if the saving mechanism changes.

### Adherence Example
```python
class ReportGenerator:
    def generate_content(self, data):
        return f"Report Content: {data}"

class HTMLFormatter:
    def format(self, content):
        return f"<html><body>{content}</body></html>"

class FileSaver:
    def save(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)

# Usage
generator = ReportGenerator()
formatter = HTMLFormatter()
saver = FileSaver()

report_data = "Sales Data"
content = generator.generate_content(report_data)
html_content = formatter.format(content)
saver.save("sales_report.html", html_content)
```
**Adherence:** Each class now has a single responsibility. Changes to formatting won't affect content generation or saving.

---

## 2. Open/Closed Principle (OCP)

### Definition
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification. This means you should be able to add new functionality without altering existing code.

### Problem it Solves
Prevents "fragile code" where adding new features breaks existing ones. Promotes stable, maintainable, and testable code.

### Violation Example
```python
class DiscountCalculator:
    def calculate_discount(self, customer_type, amount):
        if customer_type == "Regular":
            return amount * 0.10
        elif customer_type == "Premium":
            return amount * 0.20
        elif customer_type == "VIP":
            return amount * 0.30
        else:
            return 0

# Usage
calc = DiscountCalculator()
print(calc.calculate_discount("Regular", 100))
# If a new customer type (e.g., "Gold") is added, this class must be modified.
```
**Violation:** To add a new discount type, you must modify the `calculate_discount` method, potentially introducing bugs to existing logic.

### Adherence Example
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass

class RegularDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.10

class PremiumDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.20

class VIPDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.30

class NewDiscountCalculator:
    def calculate_discount(self, strategy: DiscountStrategy, amount):
        return strategy.calculate(amount)

# Usage
calc = NewDiscountCalculator()
print(calc.calculate_discount(RegularDiscount(), 100))
# To add a new discount type (e.g., GoldDiscount), you just create a new class
# that extends DiscountStrategy, without modifying NewDiscountCalculator.
```
**Adherence:** The `NewDiscountCalculator` is closed for modification (you don't touch its code) but open for extension (you add new discount strategies by creating new classes).

---

## 3. Liskov Substitution Principle (LSP)

### Definition
Subtypes must be substitutable for their base types without altering the correctness of the program. If `S` is a subtype of `T`, then objects of type `T` may be replaced with objects of type `S` without breaking the program.

### Problem it Solves
Ensures that inheritance is used correctly, preventing unexpected behavior and making code more robust and reusable.

### Violation Example
```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Ostrich(Bird):
    def fly(self):
        # Ostriches cannot fly, so this method might raise an error or do nothing.
        # This breaks the expectation that any Bird can fly.
        raise NotImplementedError("Ostriches cannot fly!")

def make_bird_fly(bird: Bird):
    bird.fly()

# Usage
make_bird_fly(Bird())
# make_bird_fly(Ostrich()) # This will raise an error, breaking the program's correctness.
```
**Violation:** `Ostrich` breaks the contract of `Bird` by not being able to `fly` correctly, even though it inherits from `Bird`.

### Adherence Example
```python
from abc import ABC, abstractmethod

class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class NonFlyingBird(ABC):
    @abstractmethod
    def walk(self):
        pass

class Eagle(FlyingBird):
    def fly(self):
        print("Eagle is flying high")

class Ostrich(NonFlyingBird):
    def walk(self):
        print("Ostrich is walking fast")

def make_flying_bird_fly(bird: FlyingBird):
    bird.fly()

# Usage
make_flying_bird_fly(Eagle())
# make_flying_bird_fly(Ostrich()) # This would be a type error, caught early.
# Ostrich objects are not expected to fly, so they don't inherit from FlyingBird.
```
**Adherence:** By segregating the `fly` behavior into a specific interface (`FlyingBird`), `Ostrich` no longer violates the principle. Clients expecting a `FlyingBird` will always get one that can fly.

---

## 4. Interface Segregation Principle (ISP)

### Definition
Clients should not be forced to depend on interfaces they do not use. Instead of one large interface, create smaller, role-specific interfaces.

### Problem it Solves
Prevents "fat interfaces" that force classes to implement methods they don't need, leading to unnecessary dependencies and harder maintenance.

### Violation Example
```python
from abc import ABC, abstractmethod

class Worker(ABC): # A "fat" interface
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Human working")
    def eat(self):
        print("Human eating")
    def sleep(self):
        print("Human sleeping")

class RobotWorker(Worker):
    def work(self):
        print("Robot working")
    def eat(self):
        # Robots don't eat, but we are forced to implement this method.
        pass 
    def sleep(self):
        # Robots don't sleep, but we are forced to implement this method.
        pass
```
**Violation:** `RobotWorker` is forced to implement `eat()` and `sleep()` even though it doesn't need them, violating the principle.

### Adherence Example
```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")
    def eat(self):
        print("Human eating")
    def sleep(self):
        print("Human sleeping")

class RobotWorker(Workable): # Only implements what it needs
    def work(self):
        print("Robot working")

# Usage
def manage_work(worker: Workable):
    worker.work()

manage_work(HumanWorker())
manage_work(RobotWorker()) # Works perfectly, RobotWorker only implements Workable.
```
**Adherence:** Clients (`manage_work`) only depend on the `Workable` interface, which is small and specific. `RobotWorker` only implements `Workable`, adhering to the principle.

---

## 5. Dependency Inversion Principle (DIP)

### Definition
1.  High-level modules should not depend on low-level modules. Both should depend on abstractions.
2.  Abstractions should not depend on details. Details should depend on abstractions.

### Problem it Solves
Reduces coupling between high-level policies and low-level implementation details. Promotes flexibility, testability, and maintainability by allowing components to be swapped easily.

### Violation Example
```python
class MySQLDatabase: # Low-level module
    def connect(self):
        print("Connecting to MySQL...")
        # ... actual connection logic ...
        return "MySQL Connection"

    def save(self, data):
        print(f"Saving '{data}' to MySQL.")

class ReportGenerator: # High-level module
    def __init__(self):
        self.db = MySQLDatabase() # Direct dependency on a concrete low-level module

    def generate_and_save_report(self, data):
        conn = self.db.connect()
        content = f"Report: {data} generated with {conn}"
        self.db.save(content)

# Usage
generator = ReportGenerator()
generator.generate_and_save_report("Monthly Sales")
# If we want to switch to PostgreSQL, ReportGenerator needs modification.
```
**Violation:** `ReportGenerator` (high-level) directly depends on `MySQLDatabase` (low-level concrete implementation).

### Adherence Example
```python
from abc import ABC, abstractmethod

class IDatabase(ABC): # Abstraction
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(IDatabase): # Low-level detail depends on abstraction
    def connect(self):
        print("Connecting to MySQL...")
        return "MySQL Connection"
    def save(self, data):
        print(f"Saving '{data}' to MySQL.")

class PostgreSQLDatabase(IDatabase): # Another low-level detail
    def connect(self):
        print("Connecting to PostgreSQL...")
        return "PostgreSQL Connection"
    def save(self, data):
        print(f"Saving '{data}' to PostgreSQL.")

class ReportGenerator: # High-level module depends on abstraction
    def __init__(self, db: IDatabase): # Dependency Inversion: depends on abstraction
        self.db = db

    def generate_and_save_report(self, data):
        conn = self.db.connect()
        content = f"Report: {data} generated with {conn}"
        self.db.save(content)

# Usage
mysql_generator = ReportGenerator(MySQLDatabase())
mysql_generator.generate_and_save_report("Monthly Sales")

postgres_generator = ReportGenerator(PostgreSQLDatabase())
postgres_generator.generate_and_save_report("Quarterly Sales")
# ReportGenerator is now closed for modification when changing database types.
```
**Adherence:** `ReportGenerator` (high-level) depends on the `IDatabase` abstraction. `MySQLDatabase` (low-level) also depends on `IDatabase`. The concrete database implementation is "injected" into `ReportGenerator`.

---
