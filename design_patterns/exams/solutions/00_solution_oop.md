# Solutions: Exam - Object-Oriented Programming (OOP)

---

### Question 1 (Fundamental Concepts)

Briefly define the four fundamental pillars of Object-Oriented Programming (OOP).

-   **Answer:**
    1.  **Encapsulation:** The bundling of data (attributes) and the methods (functions) that operate on that data within a single unit (the class), and restricting direct access to some of the object's components to protect data integrity.
    2.  **Inheritance:** A mechanism that allows a new class (subclass) to acquire attributes and methods from an existing class (superclass), promoting code reuse and establishing an "is-a" relationship.
    3.  **Polymorphism:** The ability of objects of different classes to respond to the same method call in different ways. It allows the same code to work with objects of various classes as long as they share a common interface (explicit or implicit).
    4.  **Abstraction:** The ability to hide implementation details and show only essential functionality to the user, focusing on "what" an object does rather than "how" it does it.

---

### Question 2 (Encapsulation in Python)

Explain how encapsulation is achieved in Python, referring to the naming conventions for public, protected, and private attributes.

-   **Answer:** In Python, encapsulation is primarily achieved by convention, as there are no strict access modifiers like `public`, `private`, or `protected` in other languages. The following naming conventions are used:
    -   **Public:** Attributes and methods without a prefix. They are accessible from anywhere.
    -   **Protected:** Attributes and methods starting with a single underscore (`_`). By convention, this indicates they are intended for internal use by the class and its subclasses, but they are still technically accessible from outside (no technical restriction).
    -   **Private:** Attributes and methods starting with two underscores (`__`). Python performs "name mangling" (e.g., `__attribute` becomes `_ClassName__attribute`) to make direct access from outside the class difficult. This is not strict privacy but discourages direct external access.

---

### Question 3 (Polymorphism and Duck Typing)

Describe the concept of polymorphism and how "Duck Typing" in Python contributes to its implementation. Provide a small example.

-   **Answer:**
    -   **Polymorphism:** It is the ability of objects of different classes to respond to the same method call in different ways. It allows the same code to operate with objects of various classes as long as they share a common interface (explicit or implicit).
    -   **Duck Typing:** In Python, polymorphism is greatly facilitated by "Duck Typing." This concept states that "If it walks like a duck and quacks like a duck, then it is a duck." That is, Python does not care about the explicit type of an object, but rather whether it has the necessary methods or attributes for the operation to be performed. If an object has the required methods, it is considered compatible.
    -   **Example:**
        ```python
        class Dog:
            def sound(self):
                return "Woof"

        class Cat:
            def sound(self):
                return "Meow"

        class Cow:
            def sound(self):
                return "Moo"

        def make_sound(animal):
            # It doesn't matter if it's a Dog, Cat, or Cow, only if it has the 'sound' method
            return animal.sound()

        dog = Dog()
        cat = Cat()
        cow = Cow()

        print(make_sound(dog)) # Output: Woof
        print(make_sound(cat))  # Output: Meow
        print(make_sound(cow))  # Output: Moo
        ```

---

### Question 4 (Composition vs. Inheritance)

Explain the difference between inheritance and composition, and when it is recommended to favor one over the other in software design. Provide an example of each.

-   **Answer:**
    -   **Inheritance ("Is-a"):** It is a mechanism where a class (subclass) acquires the attributes and methods of another class (superclass). It establishes an "is-a" hierarchical relationship. It promotes code reuse but creates strong coupling between classes and can lead to rigid hierarchies and issues like the "diamond problem" in multiple inheritance.
        -   **Example:** A `Car` *is a* `Vehicle`.
        ```python
        class Vehicle:
            def move(self): return "Vehicle moving"
        class Car(Vehicle):
            def start(self): return "Car starting"
        ```
    -   **Composition ("Has-a"):** It is a mechanism where a class contains an instance of another class as one of its attributes. It establishes a "has-a" or "part-whole" relationship. It promotes weaker coupling and greater flexibility, as the container class delegates functionality to the contained class, and the implementation of the part can be changed at runtime.
        -   **Example:** A `Car` *has an* `Engine`.
        ```python
        class Engine:
            def turn_on(self): return "Engine turned on"
        class Car:
            def __init__(self): self.engine = Engine()
            def start(self): return self.engine.turn_on()
        ```
    -   **When to favor:** It is recommended to **favor composition over inheritance** in most cases. Inheritance should be used when there is a very clear and fundamental "is-a" relationship, and when the subclass truly extends the superclass's behavior in a way that does not break the Liskov Substitution Principle. Composition is preferable for reusing functionality, achieving loose coupling, allowing runtime flexibility, and better adhering to the Open/Closed Principle.

---

### Question 5 (Abstract Classes)

What is the main purpose of an abstract class in OOP and how is an abstract method defined in Python?

-   **Answer:**
    -   **Main purpose:** The main purpose of an abstract class is to define a common interface (a contract) for a set of subclasses, providing a partial or no implementation of its methods. It serves as a blueprint for other classes, obliging them to implement certain methods to be considered "complete" or "concrete." An abstract class cannot be instantiated directly.
    -   **Defining an abstract method in Python:** In Python, an abstract method is defined within a class that inherits from `abc.ABC` (Abstract Base Class) and is marked with the `@abstractmethod` decorator.
        ```python
        from abc import ABC, abstractmethod

        class GeometricShape(ABC):
            @abstractmethod
            def calculate_area(self):
                pass # No implementation here

            @abstractmethod
            def draw(self):
                pass # No implementation here

        class Circle(GeometricShape):
            def __init__(self, radius):
                self.radius = radius
            def calculate_area(self):
                return 3.14159 * self.radius ** 2
            def draw(self):
                return "Drawing a circle"
        ```