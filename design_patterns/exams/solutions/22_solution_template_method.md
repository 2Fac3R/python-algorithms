
# Solutions: Exam - Template Method Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Template Method pattern aims to solve?

-   **Answer:** The Template Method pattern aims to solve the problem of defining a common algorithm or process that consists of multiple steps, where some steps are fixed and implemented in a base class, while others need to be implemented differently by various subclasses. It prevents code duplication for the common parts of the algorithm and ensures that the overall structure of the algorithm is maintained.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Template Method pattern.

-   **Answer:**
    -   **AbstractClass:** Defines the template method, which is the skeleton of an algorithm. It also defines abstract operations (or primitive operations) that `ConcreteClass`es must implement, and may define hook operations that `ConcreteClass`es can optionally override (e.g., `CaffeineBeverage`).
    -   **ConcreteClass:** Implements the abstract operations to carry out subclass-specific steps of the algorithm. It can also override hook operations to provide additional behavior, but it cannot change the overall structure defined by the template method (e.g., `Coffee`, `Tea`).

---

### Question 3 (Inversion of Control)

How does the Template Method pattern achieve "inversion of control"?

-   **Answer:** The Template Method pattern achieves "inversion of control" (also known as the Hollywood Principle: "Don't call us, we'll call you") because the abstract base class (the `AbstractClass`) controls the overall flow and sequence of the algorithm. Instead of the client or subclasses dictating the entire process, the `AbstractClass` defines the fixed steps and calls the varying steps (abstract methods or hook methods) that are implemented by the subclasses. The subclasses provide the specific implementations for these steps, but the `AbstractClass` determines *when* and *in what order* these steps are executed.

---

### Question 4 (Scenario)

Imagine you are building a data processing application. You have a general process for importing data that involves: reading data from a source, parsing the data, validating the data, and saving the data to a database. The reading and parsing steps might vary depending on the data format (e.g., CSV, JSON, XML), but the validation and saving steps are always the same. How would you apply the Template Method pattern to design this data import process?

-   **Answer:**
    1.  **AbstractClass (DataImporter):** Create an abstract `DataImporter` class. This class would have a concrete `import_data()` method (the template method) that defines the overall sequence:
        -   `read_data()` (abstract method)
        -   `parse_data()` (abstract method)
        -   `validate_data()` (concrete method, implemented in `DataImporter`)
        -   `save_data()` (concrete method, implemented in `DataImporter`)
    2.  **Concrete Implementations (in DataImporter):** Implement `validate_data()` and `save_data()` in the `DataImporter` class, as these steps are common across all formats.
    3.  **ConcreteClass (Format-Specific Importers):** Create concrete subclasses for each data format:
        -   **`CSVDataImporter`:** Inherits from `DataImporter` and implements `read_data()` to read from a CSV file and `parse_data()` to parse CSV-formatted data.
        -   **`JSONDataImporter`:** Inherits from `DataImporter` and implements `read_data()` to read from a JSON file and `parse_data()` to parse JSON-formatted data.
        -   **`XMLDataImporter`:** Inherits from `DataImporter` and implements `read_data()` to read from an XML file and `parse_data()` to parse XML-formatted data.
    4.  **Client Usage:** The client code would simply create an instance of the appropriate concrete importer (e.g., `csv_importer = CSVDataImporter()`) and call its `import_data()` method. The template method in the base class would then orchestrate the format-specific reading and parsing, followed by the common validation and saving steps.

