
# Solutions: Exam - Abstract Factory Pattern

---

### Question 1 (Problem Solved)

What problem does the Abstract Factory pattern primarily solve in software design?

- **Answer:** The Abstract Factory pattern primarily solves the problem of creating families of related or dependent objects without specifying their concrete classes. It ensures that the client code is decoupled from the specific implementations of these product families, allowing for easy switching between different product variants.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Abstract Factory pattern.

-   **Answer:**
    -   **Abstract Factory:** Declares an interface for operations that create abstract product objects (e.g., `GUIFactory` with `create_button()` and `create_checkbox()`).
    -   **Concrete Factory:** Implements the operations to create concrete product objects for a specific variant (e.g., `WindowsFactory` creates `WindowsButton` and `WindowsCheckbox`).
    -   **Abstract Product:** Declares an interface for a type of product object (e.g., `Button`, `Checkbox`).
    -   **Concrete Product:** Defines a product object to be created by the corresponding concrete factory and implements the `AbstractProduct` interface (e.g., `WindowsButton`, `MacOSCheckbox`).
    -   **Client:** Uses interfaces declared by `AbstractFactory` and `AbstractProduct` classes to create and interact with product families.

---

### Question 3 (Relationship with Factory Method)

How does the Abstract Factory pattern relate to the Factory Method pattern? Can one be used within the other?

-   **Answer:** The Abstract Factory pattern often uses Factory Methods to create its individual products. While Abstract Factory focuses on creating families of related objects, Factory Method focuses on creating a single product. An Abstract Factory can have multiple Factory Methods, each responsible for creating a different type of product within the family. So, yes, Factory Methods can be used within an Abstract Factory implementation.

---

### Question 4 (Scenario)

Consider a scenario where you are developing a game that needs to support different types of enemies (e.g., `Orc`, `Goblin`) and different types of weapons (e.g., `Sword`, `Bow`). How would you apply the Abstract Factory pattern to create compatible families of enemies and weapons (e.g., `OrcWarrior` with `OrcSword`, `GoblinArcher` with `GoblinBow`)?

-   **Answer:**
    1.  **Abstract Products:** Define `Enemy` (e.g., with `attack()`) and `Weapon` (e.g., with `use()`) abstract interfaces.
    2.  **Concrete Products:** Create concrete enemy types (`OrcWarrior`, `GoblinArcher`) and weapon types (`OrcSword`, `GoblinBow`).
    3.  **Abstract Factory:** Define an `GameElementFactory` abstract interface with methods like `create_enemy()` and `create_weapon()`.
    4.  **Concrete Factories:** Implement `OrcFactory` (creates `OrcWarrior` and `OrcSword`) and `GoblinFactory` (creates `GoblinArcher` and `GoblinBow`).
    5.  **Client:** The game logic would receive a `GameElementFactory` (e.g., `OrcFactory`) and use its methods to create compatible enemies and weapons without knowing their specific classes.

