# Solutions: Exam - Factory Method Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Factory Method design pattern aims to solve?

- **Answer:** It solves the problem of tight coupling between client code and the concrete classes it instantiates. It allows for the creation of objects without specifying the exact class to be created.

---

### Question 2 (Core Principle)

How does the Factory Method pattern achieve loose coupling between the client code and the product creation?

- **Answer:** It achieves loose coupling by deferring the instantiation of concrete product classes to subclasses of the `Creator`. The client code only interacts with the abstract `Product` and `Creator` interfaces, not with the concrete product classes directly.

---

### Question 3 (Components)

In the context of the Factory Method pattern, what is the role of the `Creator` class, and what is the role of the `Product` interface?

- **Creator Role:** Declares the factory method, which returns an object of type `Product`. It may also define a default implementation of the factory method or contain core logic that uses the product.
- **Product Role:** Declares the interface for the objects that the factory method creates. It defines the common interface that all concrete products must implement.

---

### Question 4 (Application)

Imagine you are building a game with different types of characters (e.g., `Warrior`, `Mage`, `Archer`). How would you apply the Factory Method pattern to create these characters, ensuring you can add new character types easily in the future?

- **Answer:**
    1.  Define a `Character` abstract class (Product interface) with common methods (e.g., `attack()`).
    2.  Create concrete `Warrior`, `Mage`, `Archer` classes (Concrete Products) inheriting from `Character`.
    3.  Define an abstract `CharacterCreator` class (Creator) with an abstract `create_character()` method (the factory method).
    4.  Create concrete creators like `WarriorCreator`, `MageCreator`, `ArcherCreator` (Concrete Creators) that inherit from `CharacterCreator` and implement `create_character()` to return their respective character types.
    5.  Client code would then use `creator.create_character()` without knowing the specific character class being instantiated.