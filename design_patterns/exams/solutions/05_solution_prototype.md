
# Solutions: Exam - Prototype Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Prototype pattern aims to solve?

- **Answer:** The Prototype pattern aims to solve the problem of creating new objects efficiently when their creation process is complex or resource-intensive, or when the exact type of object to be created is not known until runtime. It avoids coupling the client code to concrete classes by allowing objects to create copies of themselves.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Prototype pattern.

-   **Answer:**
    -   **Prototype:** Declares an interface (or abstract class) that includes a `clone()` method. All concrete prototypes must implement this method.
    -   **Concrete Prototype:** Implements the `clone()` operation to create a copy of itself. This typically involves copying its own attributes and, if necessary, the attributes of its contained objects.
    -   **Client:** Creates new objects by asking a prototype to clone itself. The client interacts with the `Prototype` interface, not with concrete prototype classes directly.

---

### Question 3 (Cloning Types)

Explain the difference between shallow copy and deep copy in the context of the Prototype pattern. When would you use each?

-   **Answer:**
    -   **Shallow Copy:** Creates a new object, but it does not create copies of the nested objects (mutable attributes). Instead, it copies the references to these nested objects. If the original object's mutable attributes are modified, the shallow copy's corresponding attributes will also reflect those changes because they point to the same underlying objects.
        -   **When to use:** When the object contains only immutable attributes, or when you explicitly want the copied object to share references to mutable nested objects with the original.
    -   **Deep Copy:** Creates a new object and recursively creates copies of all nested objects (mutable attributes). This means the new object is completely independent of the original; changes to the original's nested objects will not affect the deep copy, and vice-versa.
        -   **When to use:** When the object contains mutable attributes (like lists, dictionaries, or custom objects) and you need the copied object to be fully independent of the original, ensuring that modifications to one do not affect the other.

---

### Question 4 (Scenario)

Imagine you are building a game where you need to create many similar enemy characters (e.g., `Goblin`, `Orc`) with slight variations (e.g., different health, attack power, or starting positions). How would you apply the Prototype pattern to efficiently create these enemy characters?

-   **Answer:**
    1.  **Prototype Interface:** Define an abstract `Enemy` class with a `clone()` method and common attributes like `health`, `attack_power`, `position`.
    2.  **Concrete Prototypes:** Create base `GoblinPrototype` and `OrcPrototype` classes that inherit from `Enemy` and implement the `clone()` method (using `copy.deepcopy` to ensure independent copies of mutable attributes).
    3.  **Configuration:** Initialize a few instances of `GoblinPrototype` and `OrcPrototype` with default or common values.
    4.  **Client (Game Manager):** When a new enemy is needed, the game manager would ask the appropriate prototype to `clone()` itself. After cloning, the manager can then modify specific attributes of the new enemy (e.g., `cloned_goblin.health = 80`, `cloned_orc.position = (x, y)`) without affecting the original prototype or other cloned instances. This is much more efficient than creating each enemy from scratch, especially if enemies have complex internal states or many attributes.

