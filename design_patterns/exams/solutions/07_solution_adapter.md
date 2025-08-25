
# Solutions: Exam - Adapter Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Adapter pattern aims to solve?

-   **Answer:** The Adapter pattern solves the problem of incompatible interfaces between existing classes. It allows classes with different interfaces to work together without modifying their original source code, promoting reusability and flexibility.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Adapter pattern.

-   **Answer:**
    -   **Target:** This is the interface that the client expects to use. The client interacts with objects through this interface (e.g., `MediaPlayer`).
    -   **Adaptee:** This is the existing class with the incompatible interface that needs to be adapted (e.g., `WAVPlayer`, `OGGPlayer`).
    -   **Adapter:** This class implements the `Target` interface and contains an instance of the `Adaptee`. It translates calls from the `Target` interface into calls that the `Adaptee` can understand (e.g., `WAVPlayerAdapter`, `OGGPlayerAdapter`).
    -   **Client:** This is the code that uses the `Target` interface to interact with objects. It is unaware of the `Adaptee`'s incompatible interface (e.g., `client_code` function).

---

### Question 3 (Types of Adapters)

Briefly explain the difference between Class Adapter and Object Adapter implementations. Which one is generally preferred in Python and why?

-   **Answer:**
    -   **Class Adapter:** Uses inheritance. The `Adapter` class inherits from both the `Target` interface and the `Adaptee` class. This approach is not directly supported in Python for multiple inheritance of concrete classes in the same way as in languages like C++ (due to Python's method resolution order and the desire to avoid diamond problem complexities). It would typically involve inheriting from the `Target` ABC and the `Adaptee` concrete class.
    -   **Object Adapter:** Uses composition. The `Adapter` class implements the `Target` interface and contains an instance of the `Adaptee` as an attribute. It then delegates calls to the `Adaptee`'s methods.
    -   **Preference in Python:** Object Adapter is generally preferred in Python. This is because Python's strong emphasis on composition over inheritance makes the Object Adapter a more natural and flexible fit. It avoids the complexities of multiple inheritance and allows for adapting subclasses of the `Adaptee` without creating new adapter classes for each subclass.

---

### Question 4 (Scenario)

Imagine you have a third-party analytics library that provides data in a specific format (e.g., a list of dictionaries with keys like `"event_name"`, `"timestamp"`, `"user_id"`). Your application, however, expects analytics data in a different format (e.g., objects with `get_event_type()`, `get_time()`, `get_user()`). How would you use the Adapter pattern to integrate this third-party library with your application?

-   **Answer:**
    1.  **Define Target Interface:** Create an abstract base class or interface (e.g., `AnalyticsData`) with methods like `get_event_type()`, `get_time()`, `get_user()`, which your application expects.
    2.  **Identify Adaptee:** The third-party analytics data (list of dictionaries) is the `Adaptee`.
    3.  **Create Adapter Class:** Implement an `AnalyticsDataAdapter` class that inherits from `AnalyticsData`.
    4.  **Constructor:** The `AnalyticsDataAdapter`'s constructor would take a single dictionary (representing one event from the third-party library) as an argument.
    5.  **Adapt Methods:** Inside the `AnalyticsDataAdapter`, implement the `get_event_type()`, `get_time()`, and `get_user()` methods. These methods would access the corresponding keys in the internal dictionary (`self.data["event_name"]`, `self.data["timestamp"]`, `self.data["user_id"]`) and return the data in the format your application expects.
    6.  **Client Usage:** Your application code would then iterate through the list of dictionaries from the third-party library, create an instance of `AnalyticsDataAdapter` for each dictionary, and then interact with these adapter objects using the `AnalyticsData` interface.

