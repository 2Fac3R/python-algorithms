
from abc import ABC, abstractmethod
from typing import List, Any

"""
Solution for: Book Collection Iterator
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
        return self._position < len(self._collection)

    def next(self) -> Any:
        if not self.has_next():
            raise StopIteration()
        item = self._collection[self._position]
        self._position += 1
        return item

# Concrete Aggregate
class Library(BookCollection):
    def __init__(self):
        self._books: List[str] = []

    def add_book(self, book: str):
        self._books.append(book)

    def create_iterator(self) -> BookIterator:
        return ConcreteBookIterator(self._books)
