
# Solutions: Exam - State Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the State pattern aims to solve?

-   **Answer:** The State pattern aims to solve the problem of an object's behavior changing dramatically based on its internal state, which often leads to large, complex conditional statements (if/else, switch/case) within the object's methods. This makes the code hard to maintain, extend, and violates the Open/Closed Principle.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the State pattern.

-   **Answer:**
    -   **Context:** The object whose behavior changes depending on its state. It maintains a reference to the current `State` object and delegates state-specific requests to it (e.g., `TrafficLight`).
    -   **State:** An interface (or abstract class) that defines the behavior associated with a particular state of the `Context`. It declares methods that correspond to the state-dependent operations of the `Context`.
    -   **Concrete State:** Each subclass implements the behavior associated with a specific state. It also handles state transitions, typically by calling a method on the `Context` to change its current `State` object (e.g., `RedLightState`, `YellowLightState`, `GreenLightState`).

---

### Question 3 (Open/Closed Principle)

How does the State pattern adhere to the Open/Closed Principle?

-   **Answer:** The State pattern adheres to the Open/Closed Principle by making the `Context` class *open for extension* (you can add new states) but *closed for modification* (you don't need to change the `Context`'s code when adding new states). When a new state is introduced, you simply create a new `ConcreteState` class that implements the `State` interface. The `Context`'s code remains unchanged because it always delegates to its current `State` object, which is determined at runtime.

---

### Question 4 (Scenario)

Imagine you are building a simple vending machine. The vending machine can be in different states: `NoCoinState`, `HasCoinState`, and `SoldState`. Its behavior (e.g., what happens when a coin is inserted, or a product is dispensed) changes depending on its current state. How would you apply the State pattern to design this vending machine?

-   **Answer:**
    1.  **Context:** The `VendingMachine` class would be the Context. It would have methods like `insert_coin()`, `select_product()`, `dispense_product()`, and `get_state()`. It would hold a reference to its current `VendingMachineState` object.
    2.  **State Interface:** Define an abstract `VendingMachineState` class with abstract methods corresponding to the actions that can be performed on the vending machine (e.g., `insert_coin(machine)`, `select_product(machine)`, `dispense_product(machine)`).
    3.  **Concrete States:**
        -   **`NoCoinState`:** Implements `VendingMachineState`. `insert_coin()` would change the machine's state to `HasCoinState`. `select_product()` and `dispense_product()` would indicate an error (e.g., "Please insert coin first").
        -   **`HasCoinState`:** Implements `VendingMachineState`. `insert_coin()` might add more credit. `select_product()` would dispense the product (if available) and change the state to `SoldState` or `NoCoinState` (if change is given). `dispense_product()` would indicate an error (e.g., "Please select product first").
        -   **`SoldState`:** Implements `VendingMachineState`. `insert_coin()`, `select_product()`, `dispense_product()` would indicate that the product is being dispensed or that the machine is busy, and then transition back to `NoCoinState` after dispensing.
    4.  **State Transitions:** Each `ConcreteState` class would be responsible for defining its own behavior for each action and for transitioning the `VendingMachine` (Context) to the next appropriate state by calling `machine.set_state(NewState())`.

