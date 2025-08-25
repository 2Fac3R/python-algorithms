
# Solutions: Exam - Command Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Command pattern aims to solve?

-   **Answer:** The Command pattern aims to solve the problem of decoupling the sender of a request from the object that performs the request. It encapsulates a request as an object, allowing for parameterization of clients with different requests, queuing or logging of requests, and support for undoable operations.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Command pattern.

-   **Answer:**
    -   **Command:** An interface (or abstract class) that declares a method for executing an operation, typically `execute()`, and often an `undo()` method for supporting undoable operations.
    -   **Concrete Command:** Implements the `Command` interface. It binds a `Receiver` object with an action and its parameters. It also stores the state necessary to execute the command and, if applicable, to undo it.
    -   **Invoker:** The object that asks the command to carry out the request. It holds a `Command` object but doesn't know the `Receiver` or the specific action. It simply triggers the command's `execute()` method.
    -   **Receiver:** The object that performs the actual work when the command's `execute()` method is called. Any class can act as a `Receiver`.
    -   **Client:** Creates a `ConcreteCommand` object, sets its `Receiver`, and then associates the `Command` with the `Invoker`.

---

### Question 3 (Undo/Redo)

How does the Command pattern facilitate the implementation of undo/redo functionality?

-   **Answer:** The Command pattern facilitates undo/redo functionality by encapsulating each operation as a separate object. To support undo, each `ConcreteCommand` object needs to:
    1.  **Store State:** Save the state of the `Receiver` (or the necessary information to revert the change) *before* executing the command.
    2.  **Implement `undo()`:** Provide an `undo()` method that reverses the effect of the `execute()` method, using the stored state.
    A history of executed commands can then be maintained (e.g., in a stack). To undo, pop the last command from the stack and call its `undo()` method. To redo, push it back and call `execute()` again.

---

### Question 4 (Scenario)

Imagine you are building a simple text editor. You want to implement features like "Cut", "Copy", and "Paste". You also want to support undo/redo for these operations. How would you apply the Command pattern to design these features?

-   **Answer:**
    1.  **Command Interface:** Define a `TextEditorCommand` interface with `execute()` and `undo()` methods.
    2.  **Receiver:** The `TextEditor` class would be the receiver. It would have methods like `cut_selection()`, `copy_selection()`, `paste_text(text)`, and internal state representing the document content and selection.
    3.  **Concrete Commands:**
        -   **`CutCommand`:** Stores a reference to the `TextEditor` and the text that was cut. `execute()` calls `editor.cut_selection()`. `undo()` calls `editor.paste_text()` with the stored text at the original position.
        -   **`CopyCommand`:** Stores a reference to the `TextEditor` and the copied text. `execute()` calls `editor.copy_selection()`. `undo()` might not be strictly necessary for copy if it doesn't alter the editor's state, or it could clear the clipboard.
        -   **`PasteCommand`:** Stores a reference to the `TextEditor`, the text to paste, and the original content/position before pasting. `execute()` calls `editor.paste_text()`. `undo()` restores the original content/position.
    4.  **Invoker:** The `Toolbar` or `MenuItem` classes would act as invokers. When a button is pressed, they would trigger the `execute()` method of the associated `TextEditorCommand` object.
    5.  **Client:** The main application would create instances of `TextEditor`, `CutCommand`, `CopyCommand`, `PasteCommand`, etc., and set up the associations. It would also maintain a history stack of executed commands to manage undo/redo operations.

