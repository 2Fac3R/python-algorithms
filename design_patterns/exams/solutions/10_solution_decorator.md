
# Solutions: Exam - Decorator Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Decorator pattern aims to solve?

-   **Answer:** The Decorator pattern aims to solve the problem of adding new functionalities or responsibilities to an object dynamically, without altering its structure or affecting other objects of the same class. It provides a flexible alternative to subclassing, which can lead to a class explosion when many combinations of features are required.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Decorator pattern.

-   **Answer:**
    -   **Component:** Defines the interface for objects that can have responsibilities added to them dynamically (e.g., `Coffee`). Both concrete components and decorators must implement this interface.
    -   **Concrete Component:** The original object to which new responsibilities can be attached. It implements the `Component` interface (e.g., `SimpleCoffee`).
    -   **Decorator:** An abstract class that maintains a reference to a `Component` object and conforms to the `Component` interface. It acts as an abstract base for concrete decorators, ensuring that decorators can be stacked (e.g., `CoffeeDecorator`).
    -   **Concrete Decorator:** Adds specific responsibilities to the `Component`. It implements the `Decorator` interface and adds its own behavior before or after delegating the call to the wrapped `Component` (e.g., `Milk`, `Sugar`, `Caramel`).

---

### Question 3 (Alternative to Subclassing)

How does the Decorator pattern provide a flexible alternative to subclassing for extending functionality?

-   **Answer:** The Decorator pattern provides a flexible alternative to subclassing by using composition instead of inheritance for extending functionality. Instead of creating a new subclass for every possible combination of features (which leads to a class explosion), the Decorator pattern allows you to wrap an object with one or more decorator objects. Each decorator adds a specific piece of functionality. Since decorators implement the same interface as the component they decorate, they can be stacked in any order, providing a highly flexible and dynamic way to add responsibilities at runtime without modifying the original class or creating a rigid class hierarchy.

---

### Question 4 (Scenario)

Imagine you are building a system for processing text. You have a basic `TextProcessor` that performs simple operations. You want to add various text formatting capabilities (e.g., `UpperCase`, `LowerCase`, `RemoveSpaces`, `AddPrefix`) that can be combined in any order. How would you apply the Decorator pattern to achieve this?

-   **Answer:**
    1.  **Component Interface:** Define an abstract `Text` class (Component) with an abstract method `get_content() -> str`.
    2.  **Concrete Component:** Implement a `PlainText` class (Concrete Component) that inherits from `Text` and simply returns its raw string content from `get_content()`.
    3.  **Decorator Abstract Class:** Define an abstract `TextDecorator` class (Decorator) that inherits from `Text`. Its constructor would take a `decorated_text` object (another `Text` instance). Its `get_content()` method would be abstract.
    4.  **Concrete Decorators:** Implement concrete decorator classes like `UpperCaseText`, `LowerCaseText`, `RemoveSpacesText`, and `AddPrefixText`. Each of these would inherit from `TextDecorator` and implement `get_content()` to apply their specific formatting logic to the result of `self._decorated_text.get_content()`.
    5.  **Client Usage:** The client code would start with a `PlainText` object and then wrap it with various decorators to achieve the desired formatting. For example, `processed_text = UpperCaseText(RemoveSpacesText(PlainText("hello world")))` would first remove spaces and then convert to uppercase.

