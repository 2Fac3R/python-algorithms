
# Solutions: Exam - Builder Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Builder pattern aims to solve?

- **Answer:** The Builder pattern aims to solve the problem of constructing complex objects with many optional parts or configurations. It avoids the "telescoping constructor" anti-pattern and ensures that the object is built in a step-by-step manner, preventing inconsistent states during construction.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Builder pattern.

-   **Answer:**
    -   **Product:** The complex object that is being built (e.g., `Pizza`, `Report`). It can be a simple class that holds the constructed parts.
    -   **Builder:** An abstract interface that defines the steps for building the parts of the Product. It declares methods for building each component (e.g., `build_dough()`, `build_sauce()`).
    -   **Concrete Builder:** Implements the `Builder` interface, providing specific implementations for each building step and assembling the parts to create a particular representation of the Product (e.g., `MargheritaPizzaBuilder`, `PepperoniPizzaBuilder`).
    -   **Director:** (Optional) Orchestrates the construction process. It knows the sequence of building steps required to construct a particular type of Product but does not know the concrete details of the parts. It works with the `Builder` interface (e.g., `PizzaDirector`).

---

### Question 3 (Director's Role)

What is the role of the `Director` in the Builder pattern, and why is it optional?

-   **Answer:** The `Director`'s role is to encapsulate the construction logic for common product configurations. It defines the order in which to call the building steps on a `Builder` object. It is optional because the client code can directly interact with the `ConcreteBuilder` to construct the product step-by-step if the construction process is simple or if the client needs more fine-grained control over the building process.

---

### Question 4 (Scenario)

Imagine you are developing a system for creating different types of reports (e.g., PDF, HTML, CSV) with various sections (header, body, footer, tables, charts). How would you apply the Builder pattern to construct these reports?

-   **Answer:**
    1.  **Product:** Define a `Report` class that can hold different sections (header, body, footer, tables, charts) as attributes or a list of parts.
    2.  **Builder Interface:** Define an abstract `ReportBuilder` with methods like `build_header()`, `build_body()`, `build_footer()`, `add_table(data)`, `add_chart(chart_type, data)`, and `get_report()`.
    3.  **Concrete Builders:** Create concrete builders for each report format:
        -   `PdfReportBuilder`: Implements `ReportBuilder` to assemble parts into a PDF-specific structure.
        -   `HtmlReportBuilder`: Implements `ReportBuilder` to assemble parts into HTML tags.
        -   `CsvReportBuilder`: Implements `ReportBuilder` to assemble parts into CSV rows.
    4.  **Director (Optional):** Create a `ReportGenerator` (Director) that takes a `ReportBuilder` and has methods like `generate_summary_report()` or `generate_detailed_report()`. These methods would call the appropriate `build_` methods on the injected builder in a specific sequence.
    5.  **Client:** The client code would choose a specific `ConcreteBuilder` (e.g., `PdfReportBuilder`), optionally pass it to the `ReportGenerator` (Director) to build a standard report, or directly call the builder's methods for custom report construction.

