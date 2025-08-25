
# Solutions: Exam - Iterator Pattern

---

### Question 1 (Problem Solved)

What is the primary problem that the Iterator pattern aims to solve?

-   **Answer:** The Iterator pattern aims to solve the problem of accessing the elements of a collection (or aggregate object) sequentially without exposing its underlying representation. It decouples the traversal logic from the collection itself, allowing for uniform traversal across different collection types and preventing client code from breaking if the collection's internal structure changes.

---

### Question 2 (Key Components)

Identify and briefly describe the main components of the Iterator pattern.

-   **Answer:**
    -   **Iterator:** Declares an interface for accessing and traversing elements. It typically defines methods like `has_next()` (to check if there are more elements) and `next()` (to retrieve the next element and advance the iterator).
    -   **Concrete Iterator:** Implements the `Iterator` interface for a specific `ConcreteAggregate`. It keeps track of the current position in the traversal of the aggregate.
    -   **Aggregate:** Declares an interface for creating an `Iterator` object. It provides a method (e.g., `create_iterator()`) that returns an instance of the appropriate `ConcreteIterator`.
    -   **Concrete Aggregate:** Implements the `createIterator()` method to return an instance of its corresponding `ConcreteIterator`. It holds the collection of objects that need to be traversed.
    -   **Client:** Uses the `Iterator` interface to traverse the `Aggregate` without needing to know its internal structure or the specific `ConcreteIterator` being used.

---

### Question 3 (Pythonic Iterators)

How is the Iterator pattern typically implemented in Python using its built-in protocol? What methods are involved?

-   **Answer:** In Python, the Iterator pattern is typically implemented implicitly using the built-in iterator protocol. This involves two special methods:
    -   **`__iter__(self)`:** This method makes an object *iterable*. It should return an iterator object. Often, for simple cases, the object itself can be its own iterator, in which case `__iter__` simply returns `self`. For more complex scenarios or to support multiple independent traversals, `__iter__` would return a new instance of a separate iterator class.
    -   **`__next__(self)`:** This method makes an object an *iterator*. It should return the next item from the container. If there are no more items, it should raise the `StopIteration` exception.
    When you use a `for` loop in Python (e.g., `for item in collection:`), Python internally calls `collection.__iter__()` to get an iterator, and then repeatedly calls `iterator.__next__()` until `StopIteration` is raised.

---

### Question 4 (Scenario)

Imagine you are building a music player application. You have different ways to store playlists: one might be a simple list of song titles, another might be a linked list of song objects, and a third might be a tree structure representing albums and tracks. You want to allow the user to play songs from any playlist sequentially without knowing how each playlist is internally structured. How would you apply the Iterator pattern to achieve this?

-   **Answer:**
    1.  **Iterator Interface:** Define an abstract `PlaylistIterator` class with `has_next()` and `next()` methods.
    2.  **Aggregate Interface:** Define an abstract `Playlist` class with a `create_iterator()` method that returns a `PlaylistIterator`.
    3.  **Concrete Iterators:**
        -   `ListIterator`: Implements `PlaylistIterator` for playlists stored as Python lists.
        -   `LinkedListIterator`: Implements `PlaylistIterator` for playlists stored as linked lists.
        -   `TreeIterator`: Implements `PlaylistIterator` for playlists stored as tree structures (e.g., performing an in-order traversal).
    4.  **Concrete Aggregates:**
        -   `SimplePlaylist`: Stores songs in a Python list and returns a `ListIterator` from `create_iterator()`.
        -   `AlbumTreePlaylist`: Stores songs in a tree structure and returns a `TreeIterator` from `create_iterator()`.
    5.  **Client (Music Player):** The music player (client) would receive any object that implements the `Playlist` interface. To play songs, it would call `playlist.create_iterator()` to get a `PlaylistIterator`, and then use `has_next()` and `next()` to sequentially access and play songs, regardless of the playlist's internal storage mechanism.

