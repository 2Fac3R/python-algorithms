from abc import ABC, abstractmethod

"""
Challenge: Fundamental OOP Concepts

This challenge aims to assess your understanding of the fundamental concepts of Object-Oriented Programming (OOP) in Python: Classes, Objects, Encapsulation, Inheritance, Polymorphism, and Abstraction.

Your task is to implement the classes and functions according to the descriptions and OOP principles.

1.  **Classes and Objects:**
    -   Define a `Book` class with instance attributes `title` and `author`.
    -   Add a `display_info()` method that returns a string with the title and author.

2.  **Encapsulation:**
    -   Modify the `Book` class so that the `_isbn` (protected) and `__price` (private) attributes are accessible only through public `get_isbn()` and `get_price()` methods.

3.  **Inheritance:**
    -   Create a base class `Publication` with a method `get_type()`.
    -   Make `Book` inherit from `Publication` and override `get_type()` to return "Book".
    -   Create a new `Magazine` class that also inherits from `Publication` and overrides `get_type()` to return "Magazine".

4.  **Polymorphism:**
    -   Create a function `print_publication_type(publication)` that takes a `Publication` object (or its subclasses) and calls its `get_type()` method.

5.  **Abstraction:**
    -   Modify the `Publication` class to be an abstract class with `get_type()` as an abstract method.

"""

# 1. Classes and Objects
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # TODO: Add encapsulated attributes for _isbn and __price

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

    # TODO: Add get_isbn and get_price methods

# 3. Inheritance and 5. Abstraction
from abc import ABC, abstractmethod

class Publicacion(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

# Modifica Book to inherit from Publicacion
class Book(Publicacion):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, author) # Call superclass constructor
        self._isbn = isbn
        self.__price = price

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self._isbn}, Price: {self.__price:.2f}"

    def get_isbn(self):
        return self._isbn

    def get_price(self):
        return self.__price

    def get_type(self):
        return "Book"

class Magazine(Publicacion):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def get_type(self):
        return "Magazine"

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Issue: {self.issue_number}"

# 4. Polymorphism
def print_publication_type(publication: Publicacion):
    return publication.get_type()


# --- Tests ---
def run_tests():
    print("Running OOP Concepts Challenge Tests...")

    # Test 1: Classes and Objects
    book1 = Book("One Hundred Years of Solitude", "Gabriel García Márquez", "978-0307474278", 15.99)
    assert book1.display_info() == "Title: One Hundred Years of Solitude, Author: Gabriel García Márquez, ISBN: 978-0307474278, Price: 15.99"
    print("Test 1 (Classes and Objects) Passed.")

    # Test 2: Encapsulation
    assert book1.get_isbn() == "978-0307474278"
    assert book1.get_price() == 15.99
    try:
        _ = book1.__price # Direct access should fail
        assert False, "Direct access to __price should raise AttributeError"
    except AttributeError:
        pass
    print("Test 2 (Encapsulation) Passed.")

    # Test 3 & 5: Inheritance and Abstraction
    magazine1 = Magazine("National Geographic", "Various", 250)
    assert isinstance(book1, Publicacion)
    assert isinstance(magazine1, Publicacion)
    try:
        # Publicacion() should be abstract
        Publicacion("Test", "Test")
        assert False, "Publicacion class should be abstract and not instantiable."
    except TypeError as e:
        assert "Can't instantiate abstract class Publicacion with abstract methods 'display_info', 'get_type'" in str(e) or \
               "Can't instantiate abstract class Publicacion with abstract method get_type" in str(e)
    print("Test 3 & 5 (Inheritance and Abstraction) Passed.")

    # Test 4: Polymorphism
    assert print_publication_type(book1) == "Book"
    assert print_publication_type(magazine1) == "Magazine"
    print("Test 4 (Polymorphism) Passed.")

    print("All OOP Concepts Challenge Tests Passed!")

if __name__ == "__main__":
    run_tests()