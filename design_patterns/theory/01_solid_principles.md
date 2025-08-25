# SOLID Principles

SOLID principles are a set of five software design principles that, when applied, make software designs more understandable, flexible, and maintainable. They were popularized by Robert C. Martin (also known as Uncle Bob).

## 1. S - Single Responsibility Principle (SRP)

### Concept

A class should have one, and only one, reason to change. This means that a class should have a single, well-defined responsibility or purpose.

### Explanation

If a class has multiple responsibilities, a change in one of those responsibilities could affect the others, introducing unexpected errors. By adhering to SRP, each class focuses on a specific task, making it easier to understand, test, and maintain.

### Example (Bad vs. Good)

**Bad:**

```python
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        # Logic to generate report content
        pass

    def save_to_file(self, filename):
        # Logic to save the report to a file
        pass

    def send_by_email(self, address):
        # Logic to send the report by email
        pass
```

In this example, the `Report` class has three responsibilities: generating the report, saving it, and sending it. If the way of saving or sending changes, the `Report` class must be modified.

**Good:**

```python
class ReportContent:
    def __init__(self, data):
        self.data = data

    def generate_content(self):
        # Logic to generate report content
        pass

class ReportSaver:
    def save_to_file(self, report_content, filename):
        # Logic to save the report to a file
        pass

class ReportEmailSender:
    def send_by_email(self, report_content, address):
        # Logic to send the report by email
        pass
```

Here, each class has a single responsibility, making them more robust to changes.

## 2. O - Open/Closed Principle (OCP)

### Concept

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

### Explanation

This means that the behavior of a module can be extended without altering its source code. OCP is often achieved through the use of abstractions (interfaces or abstract classes) and polymorphism. Instead of modifying an existing class to add new functionality, a new class is created that extends the functionality without touching the original code.

### Example (Bad vs. Good)

**Bad:**

```python
class AreaCalculator:
    def calculate_area(self, shape):
        if shape.type == "circle":
            return 3.14 * shape.radius ** 2
        elif shape.type == "square":
            return shape.side ** 2
        # If a new shape is added, this function must be modified
```

**Good:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.lado = side
    def area(self):
        return self.lado ** 2

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area

# To add a new shape, just create a new class that inherits from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
```

## 3. L - Liskov Substitution Principle (LSP)

### Concept

Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program. In simpler terms, if `S` is a subtype of `T`, then objects of type `T` can be replaced by objects of type `S` without breaking the program.

### Explanation

This principle ensures that subclasses not only extend the functionality of their superclasses but also maintain the same expected behavior. If a subclass changes the behavior of an inherited method in a way that breaks the expectations of the client using the superclass, then it violates LSP.

### Example (Bad vs. Good)

**Bad:**

```python
class Duck:
    def fly(self):
        return "Duck flying"

class RubberDuck(Duck):
    def fly(self):
        raise NotImplementedError("Rubber ducks cannot fly")
```

Here, `RubberDuck` inherits from `Duck`, but changes the behavior of `fly` in a way that a client expecting a flying `Duck` would break. This violates LSP.

**Good:**

```python
class Bird:
    # Not all birds fly, so fly is not a method here
    def eat(self):
        return "Eating"

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class Duck(FlyingBird):
    def fly(self):
        return "Duck flying"

class Penguin(Bird):
    # Penguin inherits from Bird, but not from FlyingBird
    def swim(self):
        return "Penguin swimming"
```

## 4. I - Interface Segregation Principle (ISP)

### Concept

Clients should not be forced to depend on interfaces they do not use. It is better to have many small, specific interfaces than one large, general interface.

### Explanation

If an interface is too large, classes implementing it may be forced to implement methods they do not need, leading to useless code or empty implementations. ISP promotes cohesive and specific interfaces for each client.

### Example (Bad vs. Good)

**Bad:**

```python
from abc import ABC, abstractmethod

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

class Robot(Worker):
    def work(self):
        return "Robot working"

    def eat(self):
        raise NotImplementedError("Robots do not eat")

    def sleep(self):
        raise NotImplementedError("Robots do not sleep")
```

`Robot` is forced to implement `eat` and `sleep` even though it doesn't need them. This violates ISP.

**Good:**

```python
from abc import ABC, abstractmethod

class WorkerBase(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleeper(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(WorkerBase, Eater, Sleeper):
    def work(self):
        return "Human working"
    def eat(self):
        return "Human eating"
    def sleep(self):
        return "Human sleeping"

class Robot(WorkerBase):
    def work(self):
        return "Robot working"
```

Now, `Robot` only implements the interface it actually needs.

## 5. D - Dependency Inversion Principle (DIP)

### Concept

High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

### Explanation

This principle promotes decoupling between modules. Instead of a high-level module (which defines business logic) directly depending on a low-level module (which handles implementation details like databases or APIs), both should depend on an abstraction (an interface or abstract class). This makes the system more flexible and easier to change.

### Example (Bad vs. Good)

**Bad:**

```python
class MySQLDatabase:
    def save(self, data):
        return f"Saving {data} to MySQL"

class ReportService:
    def __init__(self):
        self.db = MySQLDatabase() # Direct dependency on a detail

    def generate_and_save(self, data):
        return self.db.save(data)
```

`ReportService` directly depends on `MySQLDatabase`. If it changes to PostgreSQL, `ReportService` must be modified.

**Good:**

```python
from abc import ABC, abstractmethod

class Database(ABC): # Abstraction
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database): # Detail
    def save(self, data):
        return f"Saving {data} to MySQL"

class PostgreSQLDatabase(Database): # Another detail
    def save(self, data):
        return f"Saving {data} to PostgreSQL"

class ReportService: # High-level module
    def __init__(self, db: Database): # Depends on abstraction
        self.db = db

    def generate_and_save(self, data):
        return self.db.save(data)

# Usage
mysql_db = MySQLDatabase()
mysql_service = ReportService(mysql_db)
print(mysql_service.generate_and_save("Report A"))

postgresql_db = PostgreSQLDatabase()
postgresql_service = ReportService(postgresql_db)
print(postgresql_service.generate_and_save("Report B"))
```

`ReportService` now depends on the `Database` abstraction, not a concrete implementation. This allows changing the database without modifying `ReportService`.

## Conclusion

SOLID principles are guidelines for writing cleaner, more maintainable, and extensible code. Although applying them may seem like an extra effort at first, in the long run, they reduce complexity and facilitate software evolution.