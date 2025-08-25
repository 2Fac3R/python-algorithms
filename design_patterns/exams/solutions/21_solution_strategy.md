
# Solutions: Exam - Strategy Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Strategy pattern aims to solve?

-   **Answer:** The Strategy pattern aims to solve the problem of having multiple algorithms or behaviors that can be used interchangeably within a specific context, and needing to select one of them at runtime. It prevents the context class from becoming bloated with conditional logic to choose algorithms and decouples the context from the specific algorithm implementations.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Strategy pattern.

-   **Answer:**
    -   **Context:** The class that uses a `Strategy` object. It maintains a reference to a `Strategy` object and delegates the execution of the algorithm to it. It can be configured with a `ConcreteStrategy` object (e.g., `ShoppingCart`).
    -   **Strategy:** An interface (or abstract class) that declares a common interface for all supported algorithms. The `Context` uses this interface to call the algorithm defined by a `ConcreteStrategy` (e.g., `PaymentStrategy`).
    -   **Concrete Strategy:** Implements the `Strategy` interface, providing a specific implementation of the algorithm (e.g., `CreditCardPayment`, `PayPalPayment`).

---

### Question 3 (Interchangeability)

How does the Strategy pattern enable algorithms to be interchangeable at runtime?

-   **Answer:** The Strategy pattern enables algorithms to be interchangeable at runtime by encapsulating each algorithm in a separate class that implements a common `Strategy` interface. The `Context` class holds a reference to an object of this `Strategy` interface. At runtime, the client can set or change the `ConcreteStrategy` object associated with the `Context`. Since the `Context` interacts with the `Strategy` through its common interface, it doesn't need to know the specific algorithm being used, allowing the algorithm to be swapped dynamically without modifying the `Context`'s code.

---

### Question 4 (Scenario)

Imagine you are building a navigation application that needs to calculate routes based on different criteria: shortest distance, fastest time, or fewest turns. How would you apply the Strategy pattern to allow users to select their preferred routing algorithm at runtime?

-   **Answer:**
    1.  **Strategy Interface:** Define an abstract `RouteCalculationStrategy` class with an abstract method `calculate_route(start_point, end_point) -> List[Point]`.
    2.  **Concrete Strategies:**
        -   `ShortestDistanceStrategy`: Implements `RouteCalculationStrategy` to calculate the route with the shortest distance.
        -   `FastestTimeStrategy`: Implements `RouteCalculationStrategy` to calculate the route with the fastest travel time.
        -   `FewestTurnsStrategy`: Implements `RouteCalculationStrategy` to calculate the route with the fewest turns.
    3.  **Context:** Implement a `NavigationContext` class. It would have a private attribute `_route_strategy` of type `RouteCalculationStrategy`. It would have a `set_route_strategy(strategy: RouteCalculationStrategy)` method to allow changing the algorithm at runtime. It would also have a `get_route(start_point, end_point)` method that delegates the actual route calculation to its current `_route_strategy`.
    4.  **Client Usage:** The navigation application (client) would create an instance of `NavigationContext`. When a user selects a routing preference (e.g., "Fastest Route"), the client would create the corresponding `FastestTimeStrategy` object and set it on the `NavigationContext` using `navigation_context.set_route_strategy(FastestTimeStrategy())`. Then, when the user requests a route, `navigation_context.get_route(start, end)` would use the currently selected strategy to calculate the route.

