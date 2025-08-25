# Object-Oriented Programming (OOP) in Python

Object-OrientOriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior. OOP focuses on the objects that developers want to manipulate, rather than the logic required to manipulate them. This approach is fundamental to understanding design patterns.

## 1. Fundamental Concepts of OOP

### 1.1. Classes and Objects

-   **Class:** A blueprint or "template" for creating objects. It defines a set of attributes (data) and methods (functions) that objects of that class will have.
    ```python
    class Car:
        # Class attribute (shared by all instances)
        wheels = 4

        # Constructor (special method to initialize objects)
        def __init__(self, brand, model, color):
            # Instance attributes (unique to each object)
            self.brand = brand
            self.model = model
            self.color = color

        # Instance method
        def start(self):
            return f"The {self.brand} {self.model} in {self.color} color has started."

        def describe(self):
            return f"This is a {self.color} {self.brand} {self.model} with {Car.wheels} wheels."
    ```

-   **Object (Instance):** A concrete occurrence of a class. It is a real entity created from the class template.
    ```python
    # Creating objects (instances of the Car class)
    my_car = Car("Toyota", "Corolla", "red")
    another_car = Car("Ford", "Fiesta", "blue")

    print(my_car.describe())
    print(another_car.start())
    ```

### 1.2. Encapsulation

Encapsulation is the principle of bundling data (attributes) and the methods (functions) that operate on that data within a single unit (the class), and restricting direct access to some of the object's components. This protects data integrity and simplifies object usage.

In Python, encapsulation is achieved by convention and by using prefixes:

-   **Public:** Attributes and methods accessible from anywhere. (No prefix).
-   **Protected:** Attributes and methods intended for internal use by the class and its subclasses. A single underscore `_` is used as a prefix (convention, does not enforce access restriction).
-   **Private:** Attributes and methods intended for use only within the class. Two underscores `__` are used as a prefix (Python performs "name mangling" to make direct access difficult).

```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # "Private" attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit of {amount}. Current balance: {self.__balance}"
        return "Invalid deposit amount."

    def __get_internal_balance(self): # "Private" method
        return self.__balance

    def get_balance(self):
        return f"Your balance is: {self.__get_internal_balance()}"

# Usage
my_account = BankAccount(100)
print(my_account.deposit(50))
print(my_account.get_balance())
# print(my_account.__balance) # This would raise an AttributeError
```

### 1.3. Inheritance

Inheritance is a mechanism that allows a new class (subclass or derived class) to inherit attributes and methods from an existing class (superclass or base class). This promotes code reuse and establishes an "is-a" relationship.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("This method must be implemented by subclasses")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Calls the superclass constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

# Usage
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "black")

print(my_dog.speak())
print(my_cat.speak())
```

### 1.4. Polymorphism

Polymorphism (from Greek "many forms") allows objects of different classes to be treated as objects of a common class. This means that the same method can behave differently depending on the object on which it is invoked.

In Python, polymorphism is primarily achieved through:

-   **Method Overriding:** Subclasses provide their own implementation of a method that is already defined in their superclass.
-   **Duck Typing:** If it walks like a duck and quacks like a duck, then it is a duck. Python does not care about the explicit type of an object, but rather whether it has the necessary methods or attributes.

```python
# Example of overriding (continuing with Animal, Dog, Cat)

def make_speak(animal):
    return animal.speak()

print(make_speak(my_dog))
print(make_speak(my_cat))

# Example of Duck Typing
class Duck:
    def speak(self):
        return "Quack!"

class Cow:
    def speak(self):
        return "Moo!"

my_duck = Duck()
my_cow = Cow()

print(make_speak(my_duck))
print(make_speak(my_cow))
```

### 1.5. Abstraction

Abstraction refers to the ability to hide implementation details and show only essential functionality to the user. In OOP, this is often achieved through abstract classes and interfaces.

-   **Abstract Classes:** Classes that cannot be instantiated directly and may contain one or more abstract methods (methods declared but without implementation). Subclasses must implement these abstract methods.
-   **Abstract Methods:** Methods that are declared in an abstract class but not implemented in it. They force subclasses to provide their own implementation.

In Python, the `abc` module (Abstract Base Classes) is used to define abstract classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return "This is a geometric shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

print(f"Circle - Area: {my_circle.area()}, Perimeter: {my_circle.perimeter()}")
print(f"Rectangle - Area: {my_rectangle.area()}, Perimeter: {my_rectangle.perimeter()}")
# generic_shape = Shape() # This would raise a TypeError
```

## 2. Composition vs. Inheritance

Two of the most important relationships between classes in OOP are inheritance ("is-a") and composition ("has-a").

-   **Inheritance ("is-a"):** A subclass *is a* type of its superclass. For example, a `Dog` *is an* `Animal`. Inheritance is used to model specialization relationships and to reuse base class implementation.

-   **Composition ("has-a"):** A class *has an* object of another class as one of its attributes. For example, a `Car` *has an* `Engine`. Composition is used to model part-whole relationships and to reuse functionality from other classes without inheriting their interface.

**When to use which?**

-   **Inheritance:** When there is a clear "is-a" relationship and the subclass needs to specialize or extend the behavior of the superclass. However, inheritance creates strong coupling between the base and derived classes.
-   **Composition:** When a class needs the functionality of another, but is not a type of that other class. Composition promotes weaker coupling and greater flexibility, as you can change the composed object at runtime.

Many design patterns, especially structural and behavioral ones, favor composition over inheritance for more flexible and robust designs.

## 3. UML Class Diagrams

UML Class Diagrams are a standard graphical notation for visualizing the structure of an object-oriented system. They are crucial for understanding and communicating design patterns.

**Key elements in class diagrams:**

-   **Classes:** Represented by a rectangle with three sections: Class Name, Attributes, Methods.
-   **Interfaces:** Represented as classes with the `<<interface>>` stereotype or a small circle with the interface name (lollipop notation).
-   **Abstract Classes:** Class names and/or abstract methods in *italics*.

**Key relationships:**

-   **Inheritance (Generalization):** Solid line with a hollow triangular arrowhead pointing to the superclass.
    `Subclass --|> Superclass`
-   **Implementation (Realization):** Dashed line with a hollow triangular arrowhead pointing to the interface.
    `Class --|> <<interface>>Interface`
-   **Association:** Simple line between two classes. Can have multiplicity (e.g., `1..*`, `0..1`).
    `ClassA -- ClassB`
-   **Aggregation:** Line with a hollow diamond arrowhead on the "whole" side (the container). The part can exist independently of the whole.
    `ContainerClass o-- ContainedClass`
-   **Composition:** Line with a filled diamond arrowhead on the "whole" side (the container). The part cannot exist independently of the whole.
    `ContainerClass *-- ContainedClass`
-   **Dependency:** Dashed line with an open arrowhead from the dependent class to the class it depends on.
    `ClassA --..> ClassB`

**Member Visibility:**

-   `+` : Public
-   `-` : Private
-   `#` : Protected

## Conclusion

This preparation plan will equip you with the necessary fundamentals to approach design patterns with confidence. A good understanding of OOP, SOLID principles, abstractions in Python, and reading UML will allow you not only to memorize patterns, but to understand their purpose, advantages and disadvantages, and how to implement them effectively in your own Python projects.