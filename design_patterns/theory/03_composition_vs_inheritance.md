# Composition vs. Inheritance in OOP

In Object-Oriented Programming (OOP) design, inheritance and composition are two of the most fundamental relationships between classes. Both allow for code reuse and the construction of complex systems, but they do so in fundamentally different ways with distinct implications for software flexibility and maintainability.

## 1. Inheritance ("Is-a")

Inheritance is a mechanism that allows one class (subclass or derived class) to acquire the attributes and methods of another class (superclass or base class). It establishes an "is-a" relationship.

### Characteristics:

-   **Code reuse:** The subclass inherits the implementation of the superclass.
-   **Specialization:** The subclass can specialize or extend the behavior of the superclass.
-   **Strong coupling:** The subclass is tightly coupled to the superclass. Changes in the superclass can affect all its subclasses.
-   **Rigid hierarchy:** Once the inheritance hierarchy is defined, it is difficult to change at runtime.
-   **"Deadly Diamond" problem (in multiple inheritance):** Can arise when a class inherits from two or more classes that have a common ancestor, and there is ambiguity about which method implementation to inherit.

### Example:

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"The {self.brand} {self.model} has started."

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def open_doors(self):
        return f"The {self.model} car has opened its {self.doors} doors."

# Usage
my_car = Car("Toyota", "Corolla", 4)
print(my_car.start())
print(my_car.open_doors())
```

## 2. Composition ("Has-a")

Composition is a mechanism where a class contains an instance of another class as one of its attributes. It establishes a "has-a" or "part-whole" relationship.

### Characteristics:

-   **Functionality reuse:** The container class reuses the functionality of the contained class by delegating calls to its methods.
-   **Loose coupling:** Classes are loosely coupled. Changes in the contained class have minimal impact on the container class, as long as the interface of the contained class does not change.
-   **Flexibility:** You can change the implementation of the contained class at runtime, or use different implementations of the same interface.
-   **"Part-whole" relationship:** One class is a "whole" that is composed of "parts."

### Example:

```python
class Engine:
    def __init__(self, type):
        self.type = type

    def turn_on(self):
        return f"Engine {self.type} turned on."

class Wheel:
    def __init__(self, size):
        self.size = size

    def rotate(self):
        return f"Wheel of {self.size} inches rotating."

class Car:
    def __init__(self, brand, model, engine_type, wheel_size):
        self.brand = brand
        self.model = model
        self.engine = Engine(engine_type) # Composition
        self.wheels = [Wheel(wheel_size) for _ in range(4)] # Composition

    def start(self):
        return self.engine.turn_on()

    def move(self):
        wheel_actions = [wheel.rotate() for wheel in self.wheels]
        return f"The {self.model} moves. {' '.join(wheel_actions)}"

# Usage
my_car = Car("Honda", "Civic", "gasoline", 17)
print(my_car.start())
print(my_car.move())
```

## 3. When to Use Inheritance and When Composition?

This is one of the most important design decisions in OOP. The general rule is: **"Favor composition over inheritance."**

### Use Inheritance when:

-   There is a clear **"is-a"** relationship. For example, a `Dog` *is an* `Animal`.
-   You need to extend the functionality of a base class in a way that is fundamental to the subclass's type.
-   The base class is designed to be extended through inheritance (e.g., abstract classes with `template` methods).
-   You are modeling a domain where type hierarchies are natural and stable.

### Use Composition when:

-   There is a **"has-a"** (has-a) or "uses-a" relationship. For example, a `Car` *has an* `Engine`.
-   You need to reuse the functionality of another class, but you don't want to inherit its full interface or state.
-   You want greater flexibility and decoupling. You can change the implementation of the "part" without affecting the "whole."
-   You need to change behavior at runtime (e.g., by injecting different composed objects).
-   You are designing for the **Open/Closed Principle (OCP)**, where behavior is extended without modifying existing code.

### Summary:

| Feature             | Inheritance                            | Composition                               |
| :------------------ | :------------------------------------- | :---------------------------------------- |
| Relationship        | "Is-a"                                 | "Has-a" / "Uses-a"                      |
| Reuse               | Reuses implementation and behavior     | Reuses functionality by delegating        |
| Coupling            | Strong                                 | Loose                                     |
| Flexibility         | Low (rigid hierarchy)                  | High (runtime part changes)               |
| OCP Principle       | Difficult to maintain                  | Easy to maintain (extension without modification) |
| Common problems     | Fragile base class, complex hierarchies | Increased number of objects, explicit delegation |

Many design patterns (such as Strategy, Decorator, Bridge, etc.) are clear examples of how composition is used to achieve more flexible and robust designs than pure inheritance.