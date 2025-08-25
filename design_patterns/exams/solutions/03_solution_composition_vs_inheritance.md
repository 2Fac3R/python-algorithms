
# Solutions: Exam - Composition vs. Inheritance

---

### Question 1 (Core Difference)

What is the fundamental difference between inheritance and composition in Object-Oriented Programming, often described by the "is-a" and "has-a" relationships?

-   **Answer:**
    -   **Inheritance** represents an **"is-a"** relationship. A subclass *is a* type of its superclass (e.g., a `Dog` *is an* `Animal`). It implies a strong, hierarchical relationship where the subclass inherits the implementation and interface of the superclass.
    -   **Composition** represents a **"has-a"** relationship. A class *has a* component of another class as one of its attributes (e.g., a `Car` *has an* `Engine`). It implies a part-whole relationship where the containing class delegates functionality to its components.

---

### Question 2 (Advantages of Composition)

List at least three advantages of favoring composition over inheritance in software design.

-   **Answer:**
    1.  **Loose Coupling:** Composition creates weaker dependencies between classes. Changes in a component class have less impact on the containing class, as long as the component's interface remains stable.
    2.  **Greater Flexibility:** Components can be swapped at runtime, allowing for dynamic behavior changes. This is harder with inheritance, where the hierarchy is fixed at compile time.
    3.  **Avoids the "Fragile Base Class" Problem:** Inheritance can lead to unexpected behavior in subclasses if the base class changes. Composition avoids this by not exposing the internal details of the components.
    4.  **Better Adherence to SOLID Principles:** Especially the Open/Closed Principle (OCP) and Single Responsibility Principle (SRP). New functionality can be added by creating new components without modifying existing classes.
    5.  **Avoids the "Deadly Diamond of Death" (in languages with multiple inheritance):** Composition is a safer alternative to multiple inheritance for combining functionalities.

---

### Question 3 (Disadvantages of Inheritance)

Describe at least two disadvantages or common problems associated with using inheritance, especially in complex systems.

-   **Answer:**
    1.  **Strong Coupling (Fragile Base Class Problem):** Inheritance creates a strong dependency between the superclass and its subclasses. Changes to the superclass's implementation (even internal ones) can inadvertently break the behavior of subclasses, requiring extensive retesting or modifications.
    2.  **Rigid Hierarchy:** The inheritance hierarchy is defined at compile time and is difficult to change at runtime. If the relationships between classes change, refactoring the hierarchy can be complex and time-consuming.
    3.  **Limited Flexibility:** A class can only inherit from one superclass (in single inheritance languages like Java/C#), limiting the ability to combine behaviors from multiple sources. Even with multiple inheritance (like in Python), it can lead to complexity and ambiguity (e.g., the diamond problem).
    4.  **Violation of Liskov Substitution Principle (LSP):** It's easy to create subclasses that violate LSP, meaning they cannot be substituted for their superclass without breaking the program's correctness.

---

### Question 4 (Scenario)

Imagine you are designing a `Robot` class. A robot can have different types of `Movement` (e.g., `WheeledMovement`, `LeggedMovement`) and different types of `Sensors` (e.g., `CameraSensor`, `InfraredSensor`).

How would you design the `Robot` class using **composition** to incorporate `Movement` and `Sensor` capabilities, allowing for easy swapping of these components? Provide a simplified Python example.

-   **Answer:**
    We would define abstract interfaces (ABCs) for `Movement` and `Sensor` capabilities. Then, concrete implementations of these interfaces would be created. The `Robot` class would then *compose* these interfaces by holding instances of them as attributes.

    ```python
    from abc import ABC, abstractmethod

    # Abstraction for Movement
    class Movement(ABC):
        @abstractmethod
        def move(self) -> str:
            pass

    # Concrete Movement Implementations
    class WheeledMovement(Movement):
        def move(self) -> str:
            return "Moving on wheels."

    class LeggedMovement(Movement):
        def move(self) -> str:
            return "Moving on legs."

    # Abstraction for Sensor
    class Sensor(ABC):
        @abstractmethod
        def detect(self) -> str:
            pass

    # Concrete Sensor Implementations
    class CameraSensor(Sensor):
        def detect(self) -> str:
            return "Detecting with camera."

    class InfraredSensor(Sensor):
        def detect(self) -> str:
            return "Detecting with infrared."

    # Robot class using Composition
    class Robot:
        def __init__(self, movement_system: Movement, sensor_system: Sensor):
            self.movement_system = movement_system
            self.sensor_system = sensor_system

        def perform_action(self) -> str:
            return f"Robot is {self.movement_system.move()} and {self.sensor_system.detect()}"

        def change_movement(self, new_movement_system: Movement):
            self.movement_system = new_movement_system
            return "Movement system changed."

        def change_sensor(self, new_sensor_system: Sensor):
            self.sensor_system = new_sensor_system
            return "Sensor system changed."

    # Usage
    wheeled_robot = Robot(WheeledMovement(), CameraSensor())
    print(wheeled_robot.perform_action())

    # Change components at runtime
    print(wheeled_robot.change_movement(LeggedMovement()))
    print(wheeled_robot.perform_action())

    legged_robot = Robot(LeggedMovement(), InfraredSensor())
    print(legged_robot.perform_action())
    ```

