
import copy
from abc import ABC, abstractmethod

"""
Solution for: Document Prototype
"""

# Prototype Interface
class Document(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return f"Document: {self.name}"

# Concrete Prototype: Report
class Report(Document):
    def __init__(self, name: str, content: str, author: str):
        super().__init__(name)
        self.content = content
        self.author = author

    def clone(self):
        # Perform a deep copy to ensure mutable attributes are also copied
        return copy.deepcopy(self)

    def __str__(self):
        return f"Report: {self.name}, Author: {self.author}, Content: {self.content[:20]}..."

# Concrete Prototype: Presentation
class Presentation(Document):
    def __init__(self, name: str, slides: list, presenter: str):
        super().__init__(name)
        self.slides = slides
        self.presenter = presenter

    def clone(self):
        # Perform a deep copy to ensure mutable attributes are also copied
        return copy.deepcopy(self)

    def __str__(self):
        return f"Presentation: {self.name}, Slides: {len(self.slides)}, Presenter: {self.presenter}"
