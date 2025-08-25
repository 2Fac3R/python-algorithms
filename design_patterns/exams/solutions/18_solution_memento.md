
# Solutions: Exam - Memento Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Memento pattern aims to solve?

-   **Answer:** The Memento pattern aims to solve the problem of saving and restoring the internal state of an object without violating its encapsulation. It allows an object's state to be externalized and restored later, without exposing the object's internal structure to other objects.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Memento pattern.

-   **Answer:**
    -   **Originator:** The object whose state needs to be saved and restored. It creates a `Memento` containing a snapshot of its current internal state and uses a `Memento` to restore its state (e.g., `TextEditor`).
    -   **Memento:** A passive object that stores a snapshot of the `Originator`'s internal state. It should be immutable and have a restricted interface, typically only accessible by the `Originator` (to restore) and the `Caretaker` (to store and retrieve). It does not expose the `Originator`'s internal details (e.g., `EditorMemento`).
    -   **Caretaker:** Responsible for keeping track of the `Memento`s. It never operates on or examines the contents of a `Memento`. It simply stores and retrieves them. It acts as a history manager for the `Originator`'s states (e.g., `History`).

---

### Question 3 (Encapsulation)

How does the Memento pattern preserve the encapsulation of the Originator?

-   **Answer:** The Memento pattern preserves the encapsulation of the `Originator` by ensuring that the `Memento` object, which holds the `Originator`'s state, has a restricted interface. Only the `Originator` itself can fully access and manipulate the state stored within the `Memento`. The `Caretaker`, which stores and retrieves `Memento`s, only sees a narrow interface of the `Memento` (e.g., a `get_saved_content()` method that returns an immutable copy or a high-level representation), preventing it from directly accessing or modifying the `Originator`'s internal details. This way, the `Originator`'s internal structure remains private, and its state can be saved and restored without breaking its encapsulation.

---

### Question 4 (Scenario)

Imagine you are building a drawing application where users can draw various shapes (circles, rectangles, lines) on a canvas. You want to implement a "Save State" and "Load State" feature, allowing users to save the entire drawing and restore it later. How would you apply the Memento pattern to achieve this, ensuring that the drawing's state can be saved and loaded without exposing the internal details of the canvas or shapes?

-   **Answer:**
    1.  **Originator:** The `DrawingCanvas` class would be the Originator. Its state would include all the shapes currently drawn on it (their types, positions, colors, etc.). It would have methods like `add_shape()`, `remove_shape()`, `draw_all_shapes()`, and crucially, `create_memento()` and `restore_memento(memento)`.
    2.  **Memento:** A `CanvasMemento` class would be created. Its constructor would take a snapshot of the `DrawingCanvas`'s state (e.g., a deep copy of the list of shapes and their properties). It would have a method `get_saved_state()` that returns this snapshot. This `Memento` object would be immutable.
    3.  **Caretaker:** A `DrawingHistory` class would act as the Caretaker. It would maintain a list of `CanvasMemento` objects. It would have `save_state(canvas: DrawingCanvas)` to add a new memento to its history and `load_state(canvas: DrawingCanvas)` to pop the last memento and restore the canvas's state using `canvas.restore_memento()`.
    4.  **Client Interaction:** When a user clicks "Save", the client code would call `drawing_history.save_state(drawing_canvas)`. When a user clicks "Load" or "Undo", the client code would call `drawing_history.load_state(drawing_canvas)`. The `DrawingCanvas` (Originator) would handle the actual saving and restoring of its internal state to/from the `CanvasMemento`, keeping its internal representation private from the `DrawingHistory` (Caretaker).

