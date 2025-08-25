
# Solutions: Exam - Composite Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Composite pattern aims to solve?

-   **Answer:** The Composite pattern aims to solve the problem of treating individual objects and compositions of objects uniformly. It allows clients to interact with both simple (leaf) objects and complex (composite) objects through a common interface, simplifying client code and making it easier to manage tree-like hierarchical structures.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Composite pattern.

-   **Answer:**
    -   **Component:** This is the abstract base class or interface that declares the common interface for both simple and complex objects in the composition. It defines operations that can be applied to both leaves and composites, and often includes default implementations for child-management operations (e.g., `FileSystemComponent`).
    -   **Leaf:** Represents individual objects in the composition that do not have children. It implements the `Component` interface directly (e.g., `File`).
    -   **Composite:** Represents complex objects that can contain other `Component` objects (both leaves and other composites). It implements the `Component` interface and provides methods for managing its children (e.g., `Directory`). It typically delegates operations to its children.
    -   **Client:** Interacts with objects in the composition through the `Component` interface, treating individual objects and compositions uniformly.

---

### Question 3 (Uniformity)

How does the Composite pattern enable clients to treat individual objects and compositions of objects uniformly?

-   **Answer:** The Composite pattern enables uniformity by defining a common interface (`Component`) that both `Leaf` objects (individual objects) and `Composite` objects (collections of objects) implement. Clients interact solely with this `Component` interface, unaware of whether they are dealing with a single object or a group of objects. When an operation is called on a `Composite`, it typically iterates through its children and calls the same operation on each child, effectively applying the operation recursively down the hierarchy.

---

### Question 4 (Scenario)

Imagine you are building a graphical user interface (GUI) framework where UI elements can be simple widgets (e.g., `Button`, `TextBox`) or containers that hold other widgets (e.g., `Panel`, `Window`). How would you apply the Composite pattern to allow operations like `render()` or `resize()` to be applied consistently to both individual widgets and containers?

-   **Answer:**
    1.  **Component Interface:** Define an abstract `UIElement` class (Component) with abstract methods like `render()` and `resize(width, height)`. It would also have default `add_child()` and `remove_child()` methods that raise `NotImplementedError`.
    2.  **Leaf Classes:** Implement concrete `Button` and `TextBox` classes (Leaves) that inherit from `UIElement` and implement `render()` and `resize()` for their specific behavior.
    3.  **Composite Classes:** Implement concrete `Panel` and `Window` classes (Composites) that inherit from `UIElement`. These classes would maintain a list of `UIElement` children. They would override `add_child()` and `remove_child()` to manage their children. Their `render()` and `resize()` methods would iterate through their children and call the respective `render()` and `resize()` methods on each child, effectively propagating the operation down the hierarchy.
    4.  **Client Usage:** The GUI framework (client) can then treat any `UIElement` (whether it's a `Button`, `TextBox`, `Panel`, or `Window`) uniformly. For example, to render the entire GUI, it would simply call `root_window.render()`, and the Composite pattern would ensure all nested elements are rendered correctly.

