
# Solutions: Exam - Flyweight Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Flyweight pattern aims to solve?

-   **Answer:** The Flyweight pattern aims to solve the problem of excessive memory consumption when an application needs to create a large number of objects that are very similar and contain a lot of redundant information. It optimizes memory usage by sharing common intrinsic state among multiple objects.

---

### Question 2 (Intrinsic vs. Extrinsic State)

Explain the difference between intrinsic and extrinsic state in the context of the Flyweight pattern. Provide an example for each.

-   **Answer:**
    -   **Intrinsic State:** This is the part of an object's state that is constant and shared among multiple objects. It is independent of the flyweight's context and is stored within the `Flyweight` object itself. It makes the flyweight shareable.
        -   **Example:** In a text editor, the font, size, and color of a character are intrinsic states. Many 'A' characters might have the same font, size, and color.
    -   **Extrinsic State:** This is the part of an object's state that is unique to each object and varies depending on the context. It cannot be shared and is typically passed to the `Flyweight` methods by the client or `Context` object at runtime.
        -   **Example:** In a text editor, the position (x, y coordinates) of a character on the screen is an extrinsic state. Each 'A' character will have a unique position.

---

### Question 3 (Flyweight Factory)

What is the role of the `FlyweightFactory` in the Flyweight pattern?

-   **Answer:** The `FlyweightFactory` is responsible for creating and managing `Flyweight` objects. Its primary role is to ensure that flyweights are shared properly. When a client requests a flyweight, the factory checks if an existing flyweight with the same intrinsic state already exists. If it does, the factory returns the existing instance; otherwise, it creates a new `ConcreteFlyweight` object, stores it, and then returns it. This mechanism prevents the creation of redundant flyweight objects, thereby optimizing memory usage.

---

### Question 4 (Scenario)

Imagine you are developing a text editor that needs to display a very large document. The document contains millions of characters, but many characters share the same font, size, and color. How would you apply the Flyweight pattern to optimize memory usage for character formatting?

-   **Answer:**
    1.  **Flyweight (CharacterProperties):** Create a `CharacterProperties` class to store the intrinsic state (shared properties) of a character, such as `font`, `size`, and `color`. This class would have a method like `display(character_value, x, y)` that takes the extrinsic state.
    2.  **Flyweight Factory (CharacterPropertyFactory):** Implement a `CharacterPropertyFactory` with a static method (e.g., `get_properties(font, size, color)`). This factory would maintain a dictionary or cache of `CharacterProperties` objects. When `get_properties` is called, it checks if a `CharacterProperties` object with the requested font, size, and color already exists. If yes, it returns the existing one; otherwise, it creates a new `CharacterProperties` object, stores it, and returns it.
    3.  **Context (Character):** Create a `Character` class that stores the extrinsic state (unique properties) of each character instance, such as its `character_value` (the actual letter, e.g., 'A', 'b') and its `x`, `y` coordinates on the screen. Each `Character` object would hold a reference to a `CharacterProperties` (Flyweight) object obtained from the `CharacterPropertyFactory`.
    4.  **Client (Document/Editor):** The document or editor would store a list of `Character` objects. When rendering the document, it would iterate through these `Character` objects, and each `Character` object would call its associated `CharacterProperties`'s `display` method, passing its unique `character_value`, `x`, and `y` coordinates. This way, millions of `Character` objects can share a much smaller number of `CharacterProperties` objects, significantly reducing memory consumption.

