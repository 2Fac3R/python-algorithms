
# Solutions: Exam - UML Class Diagrams

---

### Question 1 (Purpose of UML Class Diagrams)

What is the primary purpose of UML Class Diagrams in software development?

-   **Answer:** The primary purpose of UML Class Diagrams in software development is to model the static structure of a system. They provide a visual representation of classes, their attributes, methods, and the relationships between them. This helps in understanding, designing, and communicating the architecture of an object-oriented system.

---

### Question 2 (Basic Elements)

Describe the three main sections of a UML Class representation and explain the meaning of the visibility symbols (`+`, `-`, `#`).

-   **Answer:**
    -   **Three Main Sections:**
        1.  **Top Section:** Contains the name of the class.
        2.  **Middle Section:** Lists the attributes (instance variables) of the class.
        3.  **Bottom Section:** Lists the methods (functions) of the class.
    -   **Visibility Symbols:**
        -   `+` (Public): The attribute or method is accessible from any other class.
        -   `-` (Private): The attribute or method is accessible only from within the class itself.
        -   `#` (Protected): The attribute or method is accessible from within the class itself and its subclasses.

---

### Question 3 (Relationships)

Draw (conceptually, describe in text) and explain the difference between Aggregation and Composition relationships in UML Class Diagrams. Provide a simple example for each.

-   **Answer:**
    -   **Aggregation:** Represents a "has-a" relationship where one class is a "whole" and the other is a "part," but the part can exist independently of the whole. It's a weak association. In UML, it's drawn as a solid line with a **hollow diamond** arrowhead on the side of the "whole" (the aggregating class).
        -   **Example:** A `Department` has `Professors`. A professor can exist even if the department is dissolved.
            `Department o-- Professor`
    -   **Composition:** Represents a stronger "has-a" relationship where the part cannot exist independently of the whole. If the "whole" is destroyed, the "part" is also destroyed. It implies ownership. In UML, it's drawn as a solid line with a **filled diamond** arrowhead on the side of the "whole" (the composing class).
        -   **Example:** A `House` has `Rooms`. A room cannot exist without the house.
            `House *-- Room`

---

### Question 4 (Interpreting a Diagram)

Consider the following conceptual UML Class Diagram (describe it in text if you cannot render it):

`Class A --|> Class B`
`Class B o-- Class C`
`Class C *-- Class D`
`Class A --..> Class E`

Describe the relationships between the classes:
-   A and B
-   B and C
-   C and D
-   A and E

-   **Answer:**
    -   **A and B:** `A --|> B` represents **Inheritance (Generalization)**. Class A inherits from Class B. (Or, more precisely, B is the superclass of A).
    -   **B and C:** `B o-- C` represents **Aggregation**. Class B aggregates Class C. (B has a C, but C can exist independently of B).
    -   **C and D:** `C *-- D` represents **Composition**. Class C composes Class D. (C has a D, and D cannot exist independently of C).
    -   **A and E:** `A --..> E` represents **Dependency**. Class A depends on Class E. (Class A uses Class E, typically as a method parameter or local variable, indicating a temporary or weaker relationship).

