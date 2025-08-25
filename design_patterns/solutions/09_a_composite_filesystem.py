
from abc import ABC, abstractmethod
from typing import List

"""
Solution for: File System Composite
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
        print('  ' * indent + f"- File: {self.name} ({self.size}KB)")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent: int = 0):
        print('  ' * indent + f"- Directory: {self.name}/")
        for child in self.children:
            child.display(indent + 1)
