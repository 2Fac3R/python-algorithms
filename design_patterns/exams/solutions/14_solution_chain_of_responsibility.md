
# Solutions: Exam - Chain of Responsibility Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Chain of Responsibility pattern aims to solve?

-   **Answer:** The Chain of Responsibility pattern aims to solve the problem of decoupling the sender of a request from its receiver. It allows multiple objects to have a chance to handle a request without the sender explicitly knowing which object will ultimately process it. This avoids tight coupling and provides flexibility in assigning responsibilities.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Chain of Responsibility pattern.

-   **Answer:**
    -   **Handler:** Declares an interface for handling requests. It typically defines a method for processing the request and a method for setting the next handler in the chain (e.g., `SupportHandler`).
    -   **Abstract Handler (Optional):** Provides a default implementation for the `Handler` interface, often including the linking mechanism for the chain (e.g., `AbstractSupportHandler`). This allows concrete handlers to focus on their specific processing logic.
    -   **Concrete Handler:** Implements the `handle()` method. It contains the actual logic to process a request. If it can handle the request, it does so; otherwise, it forwards the request to its successor in the chain (e.g., `Level1Support`, `Level2Support`, `TechnicalLead`).
    -   **Client:** Initiates the request by sending it to the first handler in the chain. The client does not need to know which specific handler will process the request, only that it will be handled by some part of the chain.

---

### Question 3 (Loose Coupling)

How does the Chain of Responsibility pattern achieve loose coupling between the sender and receiver of a request?

-   **Answer:** The Chain of Responsibility pattern achieves loose coupling by eliminating the direct connection between the sender and the receiver of a request. The sender only knows about the first handler in the chain and sends the request to it. Each handler in the chain then decides whether to process the request or pass it to its successor. This means the sender doesn't need to know which specific handler will ultimately process the request, and new handlers can be added or removed from the chain without modifying the sender's code or the existing handlers (as long as they adhere to the `Handler` interface).

---

### Question 4 (Scenario)

Imagine you are building a logging system where log messages (e.g., INFO, WARNING, ERROR) need to be processed differently. INFO messages might just be printed to console, WARNING messages might be printed to console and saved to a file, and ERROR messages might be printed to console, saved to a file, and sent as an email alert. How would you apply the Chain of Responsibility pattern to handle these log messages?

-   **Answer:**
    1.  **Handler Interface:** Define a `LogHandler` interface with a `set_next()` method and a `handle_log(message_type, message)` method.
    2.  **Concrete Handlers:**
        -   **`ConsoleLogger`:** Implements `handle_log`. If `message_type` is INFO, WARNING, or ERROR, it prints the message to the console. If it's not an INFO message, it passes to the next handler.
        -   **`FileLogger`:** Implements `handle_log`. If `message_type` is WARNING or ERROR, it saves the message to a file. If it's an ERROR message, it passes to the next handler.
        -   **`EmailLogger`:** Implements `handle_log`. If `message_type` is ERROR, it sends an email alert. It doesn't pass to a next handler as it's the last in this specific chain for ERRORs.
    3.  **Chain Construction:** The client (or a configuration component) would construct the chain:
        `console_logger = ConsoleLogger()`
        `file_logger = FileLogger()`
        `email_logger = EmailLogger()`

        `console_logger.set_next(file_logger).set_next(email_logger)`
    4.  **Client Usage:** When a log message needs to be processed, the client simply calls `console_logger.handle_log(message_type, message)`. The request then traverses the chain, and each handler performs its specific action based on the message type, or passes it along.

