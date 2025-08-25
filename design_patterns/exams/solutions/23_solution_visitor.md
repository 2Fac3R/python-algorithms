
# Solutions: Exam - Visitor Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Visitor pattern aims to solve?

-   **Answer:** The Visitor pattern aims to solve the problem of adding new operations to an existing object structure (e.g., a hierarchy of classes) without modifying the classes of those objects. It helps to avoid scattering operation-specific code across multiple classes and allows for new operations to be defined independently of the element classes.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Visitor pattern.

-   **Answer:**
    -   **Visitor:** An interface (or abstract class) that declares a `visit()` method for each concrete element type in the object structure. Each `visit()` method takes a concrete element as an argument (e.g., `DocumentVisitor`).
    -   **Concrete Visitor:** Implements the `Visitor` interface, providing a specific implementation for each `visit()` method. Each `ConcreteVisitor` defines a new operation to be performed on the elements (e.g., `HTMLConverter`, `MarkdownConverter`).
    -   **Element:** An interface (or abstract class) that defines an `accept()` method. This method takes a `Visitor` object as an argument (e.g., `DocumentElement`).
    -   **Concrete Element:** Implements the `Element` interface and its `accept()` method. The `accept()` method typically calls the corresponding `visit()` method on the passed `Visitor` object, passing `self` as an argument (e.g., `Paragraph`, `Heading`).
    -   **Object Structure (Optional):** A collection or complex object that can enumerate its elements and provide a high-level interface to accept a visitor (e.g., `Document`).

---

### Question 3 (Adding New Operations)

How does the Visitor pattern allow you to add new operations to an object structure without modifying the classes of the elements?

-   **Answer:** The Visitor pattern allows you to add new operations without modifying element classes by separating the algorithm (the operation) from the object structure (the elements). Instead of adding new methods to each `Element` class, you create a new `ConcreteVisitor` class for each new operation. This `ConcreteVisitor` implements the `Visitor` interface, which has a `visit()` method for each `ConcreteElement` type. When you want to perform the new operation, you create an instance of the `ConcreteVisitor` and pass it to the `accept()` method of each `Element`. The `accept()` method then calls the appropriate `visit()` method on the `Visitor`, effectively executing the new operation on the element without the element class needing to know about the new operation beforehand.

---

### Question 4 (Scenario)

Imagine you are building a compiler for a programming language. The Abstract Syntax Tree (AST) consists of various node types (e.g., `AssignmentNode`, `VariableNode`, `FunctionCallNode`, `IfStatementNode`). You need to perform several operations on this AST, such as:

-   **Code Generation:** Convert the AST into executable machine code or bytecode.
-   **Type Checking:** Verify that all types in the AST are consistent and valid.
-   **Optimization:** Apply various optimizations to the AST.

How would you apply the Visitor pattern to design these operations, ensuring that you can add new operations without modifying the AST node classes?

-   **Answer:**
    1.  **Element Interface:** Define an abstract `ASTNode` class (Element) with an abstract `accept(visitor: ASTVisitor)` method. All concrete AST node types (`AssignmentNode`, `VariableNode`, `FunctionCallNode`, `IfStatementNode`) would inherit from `ASTNode` and implement `accept()` to call the corresponding `visit_` method on the visitor.
    2.  **Visitor Interface:** Define an abstract `ASTVisitor` class (Visitor) with abstract `visit_` methods for each concrete `ASTNode` type (e.g., `visit_assignment_node(node)`, `visit_variable_node(node)`, `visit_function_call_node(node)`, `visit_if_statement_node(node)`).
    3.  **Concrete Visitors:**
        -   **`CodeGeneratorVisitor`:** Implements `ASTVisitor`. Each `visit_` method would contain the logic to generate the appropriate machine code or bytecode for that specific AST node type.
        -   **`TypeCheckerVisitor`:** Implements `ASTVisitor`. Each `visit_` method would contain the logic to perform type checking for that specific AST node type, ensuring type compatibility.
        -   **`OptimizerVisitor`:** Implements `ASTVisitor`. Each `visit_` method would contain the logic to apply specific optimizations relevant to that AST node type.
    4.  **Object Structure (AST):** The entire AST itself can be considered the object structure. You would typically traverse the AST by starting from the root node and calling `root_node.accept(visitor)`.
    5.  **Client Usage:** To perform code generation, you would create an instance of `CodeGeneratorVisitor` and pass it to the root of the AST. To perform type checking, you would create a `TypeCheckerVisitor` and pass it to the AST. This allows you to add new compiler passes (operations) without modifying the core AST node classes.

