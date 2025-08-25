
# Solutions: Exam - SOLID Principles

---

### Question 1 (General Concept)

What is the main objective of SOLID principles in software design?

-   **Answer:** The main objective of SOLID principles is to create software designs that are more understandable, flexible, maintainable, and extensible. By applying them, the aim is to reduce coupling, increase cohesion, and facilitate the evolution of the system over time.

---

### Question 2 (SRP)

Explain the Single Responsibility Principle (SRP) and provide an example of a class that violates it and how it could be refactored to comply.

-   **Answer:**
    -   **Single Responsibility Principle (SRP):** States that a class should have one, and only one, reason to change. This means that a class should have a single, well-defined responsibility or purpose.
    -   **Violation Example:** A `User` class that handles authentication, profile management, and sending notifications. If the authentication, profile, or notification logic changes, the `User` class must be modified, violating SRP.
    -   **Refactoring to comply:** The `User` class could be split into `UserAuthenticator`, `UserProfileManager`, and `UserNotificationSender`, each with its single responsibility.

---

### Question 3 (OCP)

Describe the Open/Closed Principle (OCP). How is this principle generally achieved in OOP?

-   **Answer:**
    -   **Open/Closed Principle (OCP):** States that software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification. This means that the behavior of a module can be extended without altering its existing source code.
    -   **How it's achieved:** It is generally achieved through the use of abstractions (interfaces or abstract classes) and polymorphism. Instead of modifying an existing class to add new functionality, a new class is created that implements the abstraction and extends the functionality without touching the original code. Client code interacts with the abstraction, not with concrete implementations.

---

### Question 4 (LSP)

Explain the Liskov Substitution Principle (LSP). What are its implications for inheritance?

-   **Answer:**
    -   **Liskov Substitution Principle (LSP):** States that objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program. In other words, if `S` is a subtype of `T`, then objects of type `T` can be replaced by objects of type `S` without breaking the program or changing its expected behavior.
    -   **Implications for inheritance:** It implies that subclasses must adhere to the contract defined by their superclass. Subclasses should not change the behavior of inherited methods in a way that is inconsistent with the superclass's expectations. If a subclass throws new exceptions, requires stronger preconditions, or weaker postconditions than its superclass, it violates LSP and can lead to unexpected errors when used polymorphically.

---

### Question 5 (ISP and DIP)

Briefly define the Interface Segregation Principle (ISP) and the Dependency Inversion Principle (DIP). How do they relate to coupling in software design?

-   **Answer:**
    -   **Interface Segregation Principle (ISP):** States that clients should not be forced to depend on interfaces they do not use. It is better to have many small, specific (cohesive) interfaces than one large, general interface. This reduces coupling, as classes only implement what they truly need.
    -   **Dependency Inversion Principle (DIP):** States that high-level modules should not depend on low-level modules. Both should depend on abstractions. Furthermore, abstractions should not depend on details; details should depend on abstractions. This inverts the traditional direction of dependencies, promoting loose coupling and greater flexibility.
    -   **Relationship to coupling:** Both ISP and DIP are fundamental for reducing coupling in software design. ISP does so by ensuring that classes are not coupled to methods they don't use in large interfaces. DIP does so by ensuring that high-level modules are not coupled to concrete low-level implementations, but to abstractions, which allows implementations to change without affecting high-level logic.

