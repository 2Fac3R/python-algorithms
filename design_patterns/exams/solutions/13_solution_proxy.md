
# Solutions: Exam - Proxy Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Proxy pattern aims to solve?

-   **Answer:** The Proxy pattern aims to solve the problem of controlling access to an object, adding a layer of indirection, or performing additional actions (like lazy loading, access control, logging, caching, or security checks) before or after accessing the real object. It provides a surrogate or placeholder for another object to manage its access.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Proxy pattern.

-   **Answer:**
    -   **Subject:** Declares the common interface for both the `RealSubject` and the `Proxy`. This ensures that the `Proxy` can be used interchangeably with the `RealSubject` by the client (e.g., `Image`).
    -   **Real Subject:** The actual object that the `Proxy` represents. It contains the core business logic or resource-intensive operations (e.g., `RealImage`).
    -   **Proxy:** Maintains a reference to the `RealSubject`. It implements the `Subject` interface and controls access to the `RealSubject`. It can perform additional tasks (e.g., lazy initialization, access control, logging, caching) before or after forwarding a request to the `RealSubject` (e.g., `ProxyImage`).
    -   **Client:** Interacts with the `Subject` interface, unaware of whether it's dealing with a `RealSubject` or a `Proxy`.

---

### Question 3 (Types of Proxies)

Briefly describe three common types of proxies and their use cases.

-   **Answer:**
    1.  **Virtual Proxy:** Used for lazy initialization. It defers the creation and loading of a resource-intensive object until it's actually needed. 
        -   **Use Case:** Loading large images, complex reports, or remote objects only when they are first accessed.
    2.  **Protection Proxy:** Controls access to the real object based on permissions or security rules. It can grant or deny access to certain methods or data.
        -   **Use Case:** Implementing security checks for sensitive operations, restricting access to certain parts of an API based on user roles.
    3.  **Remote Proxy:** Provides a local representation of an object that resides in a different address space (e.g., on a remote server). It handles the communication details between the client and the remote object.
        -   **Use Case:** Interacting with web services, remote method invocation (RMI), or distributed objects.
    4.  **Caching Proxy:** Stores the results of operations from the real object and returns cached results for subsequent identical requests, avoiding redundant computations or network calls.
        -   **Use Case:** Caching database query results, web service responses, or computationally expensive calculations.
    5.  **Logging Proxy:** Logs all incoming requests and outgoing responses to the real object, useful for auditing or debugging.
        -   **Use Case:** Monitoring API calls, tracking user interactions, or debugging complex systems.

---

### Question 4 (Scenario)

Imagine you are building a document management system where users can view large PDF files. Loading an entire PDF into memory can be slow and consume a lot of resources, especially if the user only views a few pages. How would you apply the Proxy pattern to implement lazy loading for these PDF files, ensuring that the full document is only loaded when a specific page is requested?

-   **Answer:**
    1.  **Subject Interface:** Define an abstract `PDFDocument` class with methods like `get_page(page_number: int)` and `get_total_pages()`. This is the interface your client code will interact with.
    2.  **Real Subject:** Implement a `RealPDFDocument` class that inherits from `PDFDocument`. Its constructor would take the `file_path` of the PDF. In its constructor, it would perform the actual heavy loading of the entire PDF document into memory. The `get_page` method would then return the requested page from the loaded document.
    3.  **Proxy:** Implement a `LazyPDFProxy` class that also inherits from `PDFDocument`. Its constructor would take the `file_path` of the PDF but would *not* load the document immediately. It would maintain an internal reference to a `RealPDFDocument` object, initialized to `None`.
    4.  **Lazy Loading Logic:** When `get_page(page_number)` is called on the `LazyPDFProxy` for the first time, it would check if its internal `_real_pdf_document` is `None`. If it is, it would then create an instance of `RealPDFDocument` (triggering the heavy load) and store it. After ensuring the `RealPDFDocument` is loaded, it would delegate the `get_page` call to the `_real_pdf_document` instance. Subsequent calls to `get_page` would directly delegate without reloading.
    5.  **Client Usage:** The client code would create `LazyPDFProxy` objects for PDF files. The system would appear responsive because the initial object creation is fast. The actual PDF content would only be loaded into memory when the user navigates to a specific page, optimizing resource usage.

