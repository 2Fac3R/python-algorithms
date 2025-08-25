
# Cheatsheet: Abstract Classes and Interfaces in Python

**Concept:** Tools for achieving abstraction, polymorphism, and flexible software design in Python.

---

### 1. Abstract Classes

-   **Purpose:** Define a common interface and potentially partial implementation for subclasses. Cannot be instantiated directly.
-   **How to define:** Inherit from `abc.ABC` and use `@abstractmethod` decorator.
-   **Key points:**
    -   Subclasses *must* implement all abstract methods to be concrete.
    -   Can have concrete methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    def describe(self): return "A geometric shape."

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14 * self.radius ** 2
```

---

### 2. Interfaces (Conceptual in Python)

Python doesn't have explicit `interface` keyword. Achieved via:

-   **ABCs as Interfaces:** An ABC with *only* abstract methods acts as an interface. Enforces a contract.
    ```python
    from abc import ABC, abstractmethod

    class Notifier(ABC):
        @abstractmethod
        def send(self, message: str): pass

    class EmailNotifier(Notifier):
        def send(self, message: str): return f"Email: {message}"
    ```
-   **Duck Typing:** If an object behaves like a certain type (has the required methods), it's treated as that type, regardless of formal inheritance.
    ```python
    class Duck: def quack(self): return "Quack!"
    class Person: def quack(self): return "I can quack!"

    def make_it_quack(obj): return obj.quack()

    print(make_it_quack(Duck()))
    print(make_it_quack(Person()))
    ```

---

### 3. When to Use

-   **Abstract Classes:** When you want to define a base class with some common implementation *and* enforce a contract for subclasses (e.g., `Vehicle` with `start_engine` abstract, `get_info` concrete).
-   **Interfaces (pure ABCs):** When you want to define a contract of behavior that multiple unrelated classes can adhere to, without providing any implementation (e.g., `Flyable`).

---

### Pros & Cons

-   **Pros:** Enforce contracts, promote polymorphism, improve code clarity and robustness, facilitate modular design.
-   **Cons:** Can add boilerplate for simple cases, requires understanding of `abc` module.
