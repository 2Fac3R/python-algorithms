
from abc import ABC, abstractmethod
from typing import List

"""
Challenge: File System Composite

Design a file system structure using the Composite pattern where both individual files
and directories (which can contain files or other directories) can be treated uniformly.

Your task is to:
1.  Define an abstract `FileSystemComponent` class (Component interface) with:
    -   An `__init__` method that takes a `name`.
    -   An abstract `display(indent: int = 0)` method to print the component's structure.
    -   Default implementations for `add()` and `remove()` methods that raise `NotImplementedError`,
as these operations are typically only valid for composite objects.
2.  Implement a `File` class (Leaf) that inherits from `FileSystemComponent`.
    -   It should have an additional `size` attribute.
    -   Its `display` method should print the file's name and size.
3.  Implement a `Directory` class (Composite) that inherits from `FileSystemComponent`.
    -   It should maintain a list of `children` (other `FileSystemComponent` objects).
    -   It should override `add()` and `remove()` to manage its children.
    -   Its `display` method should print the directory's name and then recursively call `display` on its children.

"""

# Component Interface
class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self, indent: int = 0):
        pass

    def add(self, component: 'FileSystemComponent'):
        raise NotImplementedError("Cannot add component to a Leaf.")

    def remove(self, component: 'FileSystemComponent'):
        raise NotImplementedError("Cannot remove component from a Leaf.")

# Leaf
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def display(self, indent: int = 0):
        # TODO: Implement display for File
        pass

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        # TODO: Implement add for Directory
        pass

    def remove(self, component: FileSystemComponent):
        # TODO: Implement remove for Directory
        pass

    def display(self, indent: int = 0):
        # TODO: Implement display for Directory
        pass


# --- Tests ---
def run_tests():
    print("Running Composite Pattern File System Tests...")

    # Create files
    file1 = File("document.txt", 100)
    file2 = File("image.jpg", 500)
    file3 = File("report.pdf", 200)

    # Create directories
    root = Directory("root")
    documents = Directory("documents")
    photos = Directory("photos")

    # Build the hierarchy
    root.add(documents)
    root.add(photos)
    root.add(file1)

    documents.add(file3)

    photos.add(file2)
    photos.add(File("vacation.png", 1200))

    # Test display functionality (output will be printed to console)
    print("\nInitial File System Structure:")
    root.display()

    # Test removing a file
    print("\nRemoving report.pdf...")
    documents.remove(file3)
    print("File System Structure after removal:")
    root.display()

    # Test adding a new file
    print("\nAdding new_file.txt to root...")
    root.add(File("new_file.txt", 50))
    print("File System Structure after addition:")
    root.display()

    # Basic assertions (visual inspection of print output is key for this pattern)
    assert len(root.children) == 3, "Root should have 3 children after operations."
    assert len(documents.children) == 0, "Documents directory should be empty."
    assert len(photos.children) == 2, "Photos directory should have 2 children."

    print("All Composite Pattern File System Tests Passed (visual inspection recommended)!")

if __name__ == "__main__":
    run_tests()
