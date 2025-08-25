
# Solutions: Exam - Observer Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Observer pattern aims to solve?

-   **Answer:** The Observer pattern aims to solve the problem of maintaining consistency between related objects when one object (the Subject) changes its state, and other objects (the Observers) need to be automatically notified and updated. It prevents tight coupling that would occur if the Subject had to directly know and manage all its dependents.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Observer pattern.

-   **Answer:**
    -   **Subject (or Observable):** The object that holds the state of interest and notifies its dependents when that state changes. It provides methods for observers to register (`register_observer()`) and unregister (`remove_observer()`) themselves, and a method to notify all registered observers (`notify_observers()`).
    -   **Concrete Subject:** Implements the `Subject` interface. It stores the actual state that observers are interested in and triggers the notification process when its state changes.
    -   **Observer:** Defines an updating interface for objects that should be notified of changes in a subject. It typically has an `update()` method that the Subject calls.
    -   **Concrete Observer:** Implements the `Observer` updating interface. It registers itself with a `ConcreteSubject` and updates its own state or performs actions based on the notification received from the Subject.

---

### Question 3 (Loose Coupling)

How does the Observer pattern promote loose coupling between the Subject and its Observers?

-   **Answer:** The Observer pattern promotes loose coupling by ensuring that the `Subject` only knows about the `Observer` interface, not about concrete `Observer` classes. The `Subject` doesn't need to know *who* its observers are or *what* they do, only that they implement the `update()` method. This allows observers to be added, removed, or changed independently of the Subject, and vice-versa, without requiring modifications to the other component. This separation of concerns makes the system more flexible and easier to maintain.

---

### Question 4 (Scenario)

Imagine you are building a news application. When a new article is published (Subject), various components (e.g., a news feed display, an email notification service, a push notification service) need to be updated. How would you apply the Observer pattern to ensure all relevant components are notified when a new article is published?

-   **Answer:**
    1.  **Subject (NewsPublisher):** Create a `NewsPublisher` class that acts as the Subject. It would have methods like `add_subscriber(observer)`, `remove_subscriber(observer)`, and `publish_article(article_title, content)`. When `publish_article` is called, it would update its internal state (e.g., store the new article) and then call `notify_subscribers()`.
    2.  **Observer Interface (NewsSubscriber):** Define an abstract `NewsSubscriber` class with an abstract `update(article_title, content)` method.
    3.  **Concrete Observers:**
        -   **`NewsFeedDisplay`:** Implements `NewsSubscriber`. It registers with `NewsPublisher` and updates its display when `update()` is called.
        -   **`EmailNotificationService`:** Implements `NewsSubscriber`. It registers with `NewsPublisher` and sends an email to subscribed users when `update()` is called.
        -   **`PushNotificationService`:** Implements `NewsSubscriber`. It registers with `NewsPublisher` and sends a push notification to mobile devices when `update()` is called.
    4.  **Client Usage:** The main application would create a `NewsPublisher` instance. Then, it would create instances of `NewsFeedDisplay`, `EmailNotificationService`, and `PushNotificationService` and register them with the `NewsPublisher`. Whenever a new article is published by calling `news_publisher.publish_article(...)`, all registered observers would automatically receive the update and perform their respective actions.

