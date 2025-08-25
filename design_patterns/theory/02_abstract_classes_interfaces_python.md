# Abstract Classes and Interfaces in Python

In Object-Oriented Programming (OOP), abstract classes and interfaces are fundamental concepts for achieving abstraction, polymorphism, and flexible, extensible software design. In Python, the `abc` (Abstract Base Classes) module provides the infrastructure for defining abstract classes.

## 1. Abstract Classes

An abstract class is a class that cannot be instantiated directly. Its primary purpose is to define a common interface for a set of subclasses, providing a partial or no implementation of its methods. Subclasses that inherit from an abstract class are obligated to implement the abstract methods defined in the base class.

### Key characteristics:

-   **Cannot be instantiated:** You cannot create objects directly from an abstract class.
-   **Contain abstract methods:** Methods declared but without implementation. They are marked with the `@abstractmethod` decorator.
-   **Can contain concrete methods:** Unlike pure interfaces in other languages, abstract classes in Python can have methods with complete implementations that subclasses can inherit or override.
-   **Enforce implementation:** Any concrete subclass of an abstract class must implement all abstract methods of its base class; otherwise, the subclass will also be considered abstract and cannot be instantiated.

### Implementation in Python (`abc` module)

To define an abstract class in Python, you inherit from `ABC` (Abstract Base Class) from the `abc` module and mark abstract methods with `@abstractmethod`.

```python
from abc import ABC, abstractmethod

# Definition of an abstract class
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass

    def describe(self):
        """Concrete method that can be inherited or overridden."""
        return f"This is a geometric shape called {self.name}."

# Concrete subclass that implements abstract methods
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage of classes
circle = Circle("My Circle", 5)
rectangle = Rectangle("My Rectangle", 4, 6)

print(circle.describe())
print(f"Circle Area: {circle.area():.2f}")
print(f"Circle Perimeter: {circle.perimeter():.2f}")

print(rectangle.describe())
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

# Attempting to instantiate an abstract class will result in a TypeError
# try:
#     generic_shape = Shape("Generic")
# except TypeError as e:
#     print(f"Error instantiating Shape: {e}")
```

## 2. Interfaces (Conceptual in Python)

In languages like Java or C#, interfaces are explicit language constructs that define a contract: a set of methods that a class must implement. A class can implement multiple interfaces, allowing for behavior inheritance without state inheritance.

Python does not have an explicit `interface` keyword like other languages. However, the concept of an interface is achieved in two main ways:

### 2.1. Abstract Base Classes (ABCs) as Interfaces

ABCs in Python, when they only contain abstract methods and have no instance attributes of their own, function very similarly to interfaces. They oblige subclasses to implement a specific set of methods.

```python
from abc import ABC, abstractmethod

# ABC acting as an interface
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass

class EmailNotifier(Notifier):
    def send(self, message: str):
        return f"Sending email: {message}"

    def get_type(self) -> str:
        return "Email"

class SMSNotifier(Notifier):
    def send(self, message: str):
        return f"Sending SMS: {message}"

    def get_type(self) -> str:
        return "SMS"

# Function that works with the interface
def send_notification(notifier: Notifier, message: str):
    print(f"Using {notifier.get_type()} for: {notifier.send(message)}")

# Usage
send_notification(EmailNotifier(), "Hello from email!")
send_notification(SMSNotifier(), "Text message.")
```

### 2.2. Duck Typing as Implicit Interface

Python relies heavily on "duck typing." This means that the type of an object is less important than the methods it defines. If an object has the methods you need, you can use it, regardless of its inheritance.

```python
# No explicit interface, just expected behavior
class Duck:
    def quack(self):
        return "Quack!"

    def walk(self):
        return "Walking like a duck"

class Dog:
    def bark(self):
        return "Woof!"

    def walk(self):
        return "Walking like a dog"

class Person:
    def speak(self):
        return "Hello!"

    def walk(self):
        return "Walking like a person"

# Function that uses duck typing
def make_walk(animal):
    # It doesn't matter if it's a Duck, Dog, or Person, only if it has the 'walk' method
    return animal.walk()

print(make_walk(Duck()))
print(make_walk(Dog()))
print(make_walk(Person()))
```

In the context of design patterns, ABCs are preferred for defining explicit interfaces and obliging subclasses to adhere to a contract, which improves code clarity and robustness, especially in large projects or teams.

## 3. When to Use Abstract Classes vs. Interfaces (ABCs)?

-   **Abstract Classes:** Use them when you want to define a template for subclasses that share a common base of implementation and/or state, in addition to a method contract. They are ideal for modeling "is-a" relationships where there is a base behavior that can be inherited.
-   **Interfaces (pure ABCs):** Use them when you only want to define a behavior contract without any implementation. They are ideal for modeling capabilities or roles that different classes can have, regardless of their inheritance hierarchy. A class can implement multiple interfaces.

In summary, abstract classes and interfaces (through ABCs) are powerful tools in Python for designing modular, extensible, and maintainable systems, fundamental pillars for the effective application of design patterns.