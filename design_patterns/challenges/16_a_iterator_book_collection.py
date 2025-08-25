
from abc import ABC, abstractmethod
from typing import List, Any

"""
Challenge: Book Collection Iterator

Design a system for managing a collection of books and iterating over them.
Your goal is to provide a way to access the books sequentially without exposing
the internal storage mechanism of the collection.

Your task is to:
1.  Define an abstract `BookIterator` class (Iterator interface) with:
    -   `has_next() -> bool`: Returns `True` if there are more elements to iterate over, `False` otherwise.
    -   `next() -> Any`: Returns the next element in the collection. Raises `StopIteration` if no more elements.
2.  Define an abstract `BookCollection` class (Aggregate interface) with:
    -   `create_iterator() -> BookIterator`: An abstract method to create and return a concrete iterator.
3.  Implement a `ConcreteBookIterator` class that implements `BookIterator`.
    -   Its constructor should take the list of books to iterate over.
    -   It should keep track of its current position.
4.  Implement a `Library` class (Concrete Aggregate) that implements `BookCollection`.
    -   It should internally store a list of book titles (strings).
    -   It should have an `add_book(book: str)` method.
    -   Its `create_iterator()` method should return an instance of `ConcreteBookIterator`.

"""

# Iterator Interface
class BookIterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Any:
        pass

# Aggregate Interface
class BookCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> BookIterator:
        pass

# Concrete Iterator
class ConcreteBookIterator(BookIterator):
    def __init__(self, collection: List[str]):
        self._collection = collection
        self._position = 0

    def has_next(self) -> bool:
        # TODO: Implement has_next
        pass

    def next(self) -> Any:
        # TODO: Implement next
        pass

# Concrete Aggregate
class Library(BookCollection):
    def __init__(self):
        self._books: List[str] = []

    def add_book(self, book: str):
        self._books.append(book)

    def create_iterator(self) -> BookIterator:
        # TODO: Return a ConcreteBookIterator instance
        pass


# --- Tests ---
def run_tests():
    print("Running Iterator Pattern Book Collection Tests...")

    library = Library()
    library.add_book("The Lord of the Rings")
    library.add_book("The Hobbit")
    library.add_book("Silmarillion")

    iterator = library.create_iterator()

    # Test iteration
    books_read = []
    while iterator.has_next():
        books_read.append(iterator.next())

    expected_books = ["The Lord of the Rings", "The Hobbit", "Silmarillion"]
    assert books_read == expected_books, f"Iteration failed. Expected {expected_books}, Got {books_read}"
    print("Basic iteration test passed.")

    # Test StopIteration
    try:
        iterator.next()
        assert False, "StopIteration was not raised."
    except StopIteration:
        print("StopIteration test passed.")

    # Test multiple iterators (should be independent)
    iterator1 = library.create_iterator()
    iterator2 = library.create_iterator()

    assert iterator1.next() == "The Lord of the Rings"
    assert iterator2.next() == "The Lord of the Rings"
    assert iterator1.next() == "The Hobbit"
    assert iterator2.next() == "The Hobbit"
    print("Multiple iterators test passed.")

    print("All Iterator Pattern Book Collection Tests Passed!")

if __name__ == "__main__":
    run_tests()
