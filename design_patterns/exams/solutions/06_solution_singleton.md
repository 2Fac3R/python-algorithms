
# Solutions: Exam - Singleton Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Singleton pattern aims to solve?

- **Answer:** The Singleton pattern aims to ensure that a class has only one instance throughout the application's lifecycle and provides a global point of access to that unique instance. This is particularly useful for managing shared resources or services that should be unique.

---

### Question 2 (Implementation Methods)

Describe at least two common ways to implement the Singleton pattern in Python.

-   **Answer:**
    1.  **Overriding `__new__`:** This method is called before `__init__` during object creation. By checking if an instance already exists within `__new__`, you can return the existing instance or create a new one if it's the first time.
        ```python
        class MySingleton:
            _instance = None
            def __new__(cls):
                if cls._instance is None:
                    cls._instance = super(MySingleton, cls).__new__(cls)
                return cls._instance
        ```
    2.  **Using a Decorator:** A function decorator can be created to manage instances of a class. The decorator stores the single instance in a dictionary and returns it on subsequent calls.
        ```python
        def singleton(cls):
            instances = {}
            def get_instance(*args, **kwargs):
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            return get_instance

        @singleton
        class MyDecoratedSingleton:
            pass
        ```
    3.  **Using a Metaclass:** A metaclass controls the creation of classes. By defining a custom metaclass, you can enforce the singleton behavior at the class creation level.
        ```python
        class SingletonMeta(type):
            _instances = {}
            def __call__(cls, *args, **kwargs):
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
                return cls._instances[cls]

        class MyMetaclassSingleton(metaclass=SingletonMeta):
            pass
        ```

---

### Question 3 (Pros and Cons)

List two advantages and two disadvantages of using the Singleton pattern.

-   **Answer:**
    -   **Advantages:**
        1.  **Ensures a single instance:** Guarantees that there is only one instance of a class, which is crucial for resources that should be unique (e.g., a single logger, a single configuration manager).
        2.  **Global access point:** Provides a well-defined and easily accessible global point to retrieve the instance, avoiding the need to pass the instance around.
    -   **Disadvantages:**
        1.  **Violates Single Responsibility Principle:** The class takes on two responsibilities: its core functionality and ensuring its unique instantiation. This can make the class harder to maintain and understand.
        2.  **Can hide bad design:** Overuse of Singletons can lead to tightly coupled code and make it difficult to test components independently, as they rely on a global state that is hard to mock or reset.

---

### Question 4 (Scenario)

In a large-scale web application, you need to manage application-wide configuration settings that should be loaded once and accessible from anywhere. How would you apply the Singleton pattern to handle these configuration settings?

-   **Answer:**
    1.  **Create a `ConfigurationManager` class:** This class would be responsible for loading, storing, and providing access to the application's configuration settings.
    2.  **Implement Singleton pattern:** Apply the Singleton pattern to the `ConfigurationManager` class (e.g., using the `__new__` method or a decorator). This ensures that only one instance of the configuration manager exists.
    3.  **Load settings once:** In the `__init__` (or `__new__` if initializing there) of the `ConfigurationManager`, load the configuration settings from a file (e.g., JSON, YAML) or environment variables. This loading process will only happen once when the first instance is created.
    4.  **Provide access methods:** Implement methods like `get_setting(key)` or `set_setting(key, value)` within the `ConfigurationManager` to allow other parts of the application to read and (optionally) modify settings.
    5.  **Global access:** Any part of the application needing configuration settings would simply call `ConfigurationManager()` to get the single instance and then use its methods (e.g., `config = ConfigurationManager(); db_host = config.get_setting("DATABASE_HOST")`).

