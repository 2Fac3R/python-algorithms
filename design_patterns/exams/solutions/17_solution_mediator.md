
# Solutions: Exam - Mediator Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Mediator pattern aims to solve?

-   **Answer:** The Mediator pattern aims to solve the problem of complex, many-to-many interactions between a set of objects. When objects communicate directly with each other, it leads to tight coupling, making the system difficult to understand, maintain, extend, and reuse. The Mediator centralizes this communication, reducing direct dependencies.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Mediator pattern.

-   **Answer:**
    -   **Mediator:** Defines an interface for communicating with `Colleague` objects. It declares methods that `Colleagues` use to notify the `Mediator` of events and methods that the `Mediator` uses to communicate with `Colleagues`.
    -   **Concrete Mediator:** Implements the `Mediator` interface. It knows and maintains its `Colleagues` and coordinates their interactions. It receives messages from `Colleagues` and forwards them to the appropriate `Colleagues`.
    -   **Colleague:** An abstract class or interface for objects that interact. Each `Colleague` knows its `Mediator` object and communicates with it instead of directly with other `Colleagues`.
    -   **Concrete Colleague:** Implements the `Colleague` interface. It communicates with its `Mediator` when an event occurs and receives messages from the `Mediator`.

---

### Question 3 (Loose Coupling)

How does the Mediator pattern promote loose coupling between objects?

-   **Answer:** The Mediator pattern promotes loose coupling by eliminating direct communication between `Colleague` objects. Instead of `Colleagues` having direct references to each other and knowing about each other's interfaces, they only communicate with the `Mediator`. The `Mediator` acts as a central hub, encapsulating the complex interaction logic. This means that `Colleagues` become more independent and reusable, as they are no longer tightly bound to specific peers.

---

### Question 4 (Scenario)

Imagine you are building an air traffic control system. Multiple aircraft (colleagues) need to communicate with each other (e.g., to avoid collisions, report positions), but direct communication between every pair of aircraft would be chaotic and complex. How would you apply the Mediator pattern to manage communication in this system?

-   **Answer:**
    1.  **Mediator Interface:** Define an `AirTrafficControl` interface with methods like `register_aircraft(aircraft: Aircraft)` and `send_message(message: str, sender: Aircraft)`.
    2.  **Concrete Mediator:** Implement a `ControlTower` class that implements `AirTrafficControl`. It would maintain a list of all registered `Aircraft`. When `send_message` is called by an `Aircraft`, the `ControlTower` would receive the message, determine the appropriate recipients (e.g., all other aircraft in a certain vicinity, or a specific aircraft), and then forward the message to them.
    3.  **Colleague Abstract Class:** Define an `Aircraft` abstract class with a reference to an `AirTrafficControl` mediator. It would have methods like `send_message(message: str)` (which delegates to the mediator) and `receive_message(message: str)`.
    4.  **Concrete Colleagues:** Implement specific `Aircraft` types (e.g., `PassengerJet`, `CargoPlane`, `Helicopter`) that inherit from the `Aircraft` abstract class. These aircraft would only communicate with the `ControlTower`.
    5.  **Interaction:** When an `Aircraft` needs to communicate (e.g., report its position or request clearance), it sends a message to the `ControlTower`. The `ControlTower` then mediates the communication, ensuring that relevant messages are delivered to other `Aircraft` without direct, chaotic peer-to-peer connections.

