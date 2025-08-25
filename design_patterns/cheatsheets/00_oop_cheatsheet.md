# Cheatsheet: Object-Oriented Programming (OOP)

**Concept:** A programming paradigm that organizes software design around data, or objects, rather than functions and logic. Objects combine data (attributes) and behavior (methods).

---

### 1. Pillars of OOP

-   **Encapsulation:** Bundling data and methods that operate on them within a single unit (class), and restricting direct access to internal data. Protects data integrity.
    -   **Python:** Convention (`_` for protected, `__` for private - name mangling).

-   **Inheritance:** Allows a class (subclass) to inherit attributes and methods from another (superclass). Establishes an "is-a" relationship.
    -   **Code reuse** and **specialization**.
    -   `super().__init__()` to call the superclass constructor.

-   **Polymorphism:** Ability of objects of different classes to respond to the same method call in different ways.
    -   **Method Overriding:** Subclasses implement methods from the superclass.
    -   **Duck Typing (Python):** If an object has the necessary methods, it can be used, regardless of its explicit type.

-   **Abstraction:** Hiding implementation details and showing only essential functionality. Achieved with abstract classes and methods.
    -   **Python:** `abc` module (`ABC`, `@abstractmethod`).

---

### 2. Classes and Objects

-   **Class:** Blueprint or template for creating objects. Defines attributes and methods.
    ```python
    class Car:
        wheels = 4 # Class attribute
        def __init__(self, brand, model): # Constructor
            self.brand = brand # Instance attribute
            self.model = model
        def start(self): # Method
            return f"The {self.model} starts."
    ```
-   **Object (Instance):** Concrete occurrence of a class.
    ```python
    my_car = Car("Toyota", "Corolla")
    print(my_car.start())
    ```

---

### 3. Composition vs. Inheritance

-   **Inheritance ("Is-a"):** `Dog` *is an* `Animal`.
    -   Strong coupling.
    -   Rigid hierarchy.
    -   `class Dog(Animal):`

-   **Composition ("Has-a"):** `Car` *has an* `Engine`.
    -   Loose coupling.
    -   Greater flexibility.
    -   `class Car: self.engine = Engine()`

-   **Golden Rule:** "Favor composition over inheritance" for greater flexibility and less coupling.

---

### 4. Abstract Classes and Interfaces (in Python)

-   **Abstract Class:** Cannot be instantiated. Defines a common interface and can have concrete methods.
    ```python
    from abc import ABC, abstractmethod
    class Shape(ABC):
        @abstractmethod
        def area(self): pass
    ```
-   **Interface (pure ABC):** ABC with only abstract methods. Defines a behavior contract.
    ```python
    from abc import ABC, abstractmethod
    class Drawable(ABC):
        @abstractmethod
        def draw(self): pass
    ```

---

### 5. UML Class Diagrams

-   **Class:** Rectangle (Name, Attributes, Methods).
-   **Abstract:** Name/methods in *italics* or `<<abstract>>`.
-   **Interface:** `<<interface>>` or circle.
-   **Relationships:**
    -   **Inheritance:** Solid line with hollow triangular arrowhead.
    -   **Implementation:** Dashed line with hollow triangular arrowhead.
    -   **Association:** Simple line (with multiplicity).
    -   **Aggregation:** Hollow diamond on the "whole" side.
    -   **Composition:** Filled diamond on the "whole" side.
    -   **Dependency:** Dashed line with open arrowhead.

---

### 6. SOLID Principles

-   **S** (Single Responsibility): One class, one reason to change.
-   **O** (Open/Closed): Open for extension, closed for modification.
-   **L** (Liskov Substitution): Subtypes must be substitutable for their base types.
-   **I** (Interface Segregation): Small, specific interfaces.
-   **D** (Dependency Inversion): Depend on abstractions, not details.