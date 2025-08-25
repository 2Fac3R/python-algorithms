
# Solutions: Exam - Bridge Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Bridge pattern aims to solve?

-   **Answer:** The Bridge pattern aims to solve the problem of tight coupling between an abstraction and its implementation. This tight coupling often leads to a class explosion (e.g., `Shape` and `Renderer` creating `CircleOpenGL`, `CircleDirectX`, etc.) and makes the system rigid, difficult to extend, and hard to maintain when changes are needed in either the abstraction or the implementation.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Bridge pattern.

-   **Answer:**
    -   **Abstraction:** Defines the client-facing interface. It contains a reference to an object from the `Implementation` hierarchy and delegates the actual work to it (e.g., `RemoteControl`).
    -   **Refined Abstraction:** Extends the `Abstraction` interface, providing more specific control or functionality to the client (e.g., `AdvancedRemoteControl`).
    -   **Implementation:** Declares the interface for all concrete implementation classes. This interface does not need to mirror the `Abstraction`'s interface (e.g., `Device`).
    -   **Concrete Implementation:** Implements the `Implementation` interface, providing concrete functionality for a specific platform or technology (e.g., `TV`, `Radio`).

---

### Question 3 (Decoupling)

How does the Bridge pattern achieve decoupling between abstraction and implementation?

-   **Answer:** The Bridge pattern achieves decoupling by separating the abstraction (what the system does) from its implementation (how it does it) into two independent class hierarchies. The `Abstraction` class holds a reference to an object of the `Implementation` interface, rather than inheriting from a concrete implementation. This composition allows clients to work with the `Abstraction` without knowing the specific `ConcreteImplementation` being used, and allows both hierarchies to be extended independently without affecting each other.

---

### Question 4 (Scenario)

Imagine you are designing a cross-platform application that needs to display various types of notifications (e.g., `InfoNotification`, `WarningNotification`, `ErrorNotification`) on different operating systems (e.g., `Windows`, `macOS`, `Linux`). How would you apply the Bridge pattern to handle this scenario, allowing you to add new notification types or new operating systems independently?

-   **Answer:**
    1.  **Abstraction Hierarchy (Notification Types):**
        -   **`Notification` (Abstraction):** An abstract base class with a reference to a `NotificationSender` (Implementation). It would have methods like `send()` that delegate to the `NotificationSender`.
        -   **`InfoNotification`, `WarningNotification`, `ErrorNotification` (Refined Abstractions):** Concrete notification types inheriting from `Notification`, each potentially adding specific logic or formatting before delegating to the sender.
    2.  **Implementation Hierarchy (Operating System Senders):**
        -   **`NotificationSender` (Implementation Interface):** An abstract base class with methods like `display_message(type, message)`.
        -   **`WindowsNotificationSender`, `MacOSNotificationSender`, `LinuxNotificationSender` (Concrete Implementations):** Concrete classes implementing `NotificationSender`, each containing the OS-specific code to display a notification (e.g., using Windows API calls, macOS Notification Center, or a Linux desktop environment notification system).
    3.  **Client Usage:** The client code would create a specific `Notification` object (e.g., `InfoNotification`) and inject the desired `NotificationSender` (e.g., `WindowsNotificationSender`) into its constructor. This way, an `InfoNotification` can be sent on Windows, macOS, or Linux by simply changing the injected sender object, without modifying the `InfoNotification` class itself.

