
# Cheatsheet: SOLID Principles

**Concept:** Five software design principles for creating more understandable, flexible, and maintainable systems.

---

### S - Single Responsibility Principle (SRP)

-   **Concept:** A class should have one, and only one, reason to change (a single responsibility).
-   **Benefit:** Facilitates understanding, testing, and maintenance. Reduces coupling.
-   **Example:** Separate business logic, persistence, and notification into distinct classes.

---

### O - Open/Closed Principle (OCP)

-   **Concept:** Open for extension, closed for modification. You can add new functionality without altering existing code.
-   **Benefit:** Facilitates system evolution. Achieved with abstractions (interfaces/abstract classes) and polymorphism.
-   **Example:** Use a `Shape` interface with an `area()` method to calculate areas of different shapes, instead of `if/else` in a central function.

---

### L - Liskov Substitution Principle (LSP)

-   **Concept:** Subtypes must be substitutable for their base types without altering the correctness of the program.
-   **Benefit:** Ensures that subclasses maintain the expected behavior of their superclasses. Valid "is-a" relationship.
-   **Example:** A `Penguin` should not inherit from `FlyingBird` if it cannot fly; it should inherit from `Bird`.

---

### I - Interface Segregation Principle (ISP)

-   **Concept:** Clients should not be forced to depend on interfaces they do not use. It is better to have many small, specific interfaces than one large, general interface.
-   **Benefit:** Reduces coupling and prevents classes from implementing unnecessary methods.
-   **Example:** Instead of a `Worker` interface with `work()`, `eat()`, `sleep()`, have `WorkerBase`, `Eater`, `Sleeper`.

---

### D - Dependency Inversion Principle (DIP)

-   **Concept:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.
-   **Benefit:** Promotes decoupling and flexibility, allowing low-level implementations to change without affecting high-level logic.
-   **Example:** A `NotificationService` depends on a `Messenger` interface, not a concrete `EmailMessenger`.
