
# Cheatsheet: Composition vs. Inheritance

**Concept:** Two fundamental ways to establish relationships between classes in OOP, impacting code reuse, flexibility, and coupling.

---

### 1. Inheritance ("Is-a")

-   **Definition:** A subclass acquires attributes and methods from a superclass. Establishes an "is-a" relationship.
-   **Characteristics:**
    -   **Code Reuse:** Subclass inherits superclass implementation.
    -   **Specialization:** Subclass extends/specializes superclass behavior.
    -   **Strong Coupling:** Subclass is tightly coupled to superclass. Changes in superclass can break subclasses.
    -   **Rigid Hierarchy:** Hierarchy is fixed at compile time.
-   **Example:** `class Car(Vehicle):` (A Car *is a* Vehicle)

---

### 2. Composition ("Has-a")

-   **Definition:** A class contains an instance of another class as one of its attributes. Establishes a "has-a" or "part-whole" relationship.
-   **Characteristics:**
    -   **Functionality Reuse:** Container class reuses functionality by delegating to its components.
    -   **Loose Coupling:** Classes are weakly coupled. Changes in component have minimal impact on container.
    -   **Flexibility:** Components can be swapped at runtime.
    -   **"Part-Whole" Relationship:** One class is a "whole" composed of "parts."
-   **Example:** `class Car: self.engine = Engine()` (A Car *has an* Engine)

---

### 3. When to Use Which?

**General Rule:** "Favor composition over inheritance."

-   **Use Inheritance when:**
    -   There's a clear **"is-a"** relationship.
    -   Subclass fundamentally extends superclass behavior.
    -   Base class is designed for inheritance (e.g., abstract classes with template methods).
    -   Modeling stable type hierarchies.

-   **Use Composition when:**
    -   There's a **"has-a"** or "uses-a" relationship.
    -   You need to reuse functionality without inheriting full interface/state.
    -   You want greater flexibility and loose coupling.
    -   Behavior needs to change at runtime.
    -   Designing for **Open/Closed Principle (OCP)**.

---

### Summary Table

| Feature             | Inheritance                            | Composition                               |
| :------------------ | :------------------------------------- | :---------------------------------------- |
| Relationship        | "Is-a"                                 | "Has-a" / "Uses-a"                      |
| Reuse               | Implementation and behavior            | Functionality by delegating               |
| Coupling            | Strong                                 | Loose                                     |
| Flexibility         | Low (rigid hierarchy)                  | High (runtime component changes)          |
| OCP Principle       | Harder to maintain                     | Easier to maintain (extension without modification) |
| Common Problems     | Fragile base class, complex hierarchies | Increased number of objects, explicit delegation |
