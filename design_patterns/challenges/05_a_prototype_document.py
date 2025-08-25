
import copy
from abc import ABC, abstractmethod

"""
Challenge: Document Prototype

Design a system for creating and duplicating various types of documents (e.g., Report, Presentation)
using the Prototype pattern. The system should allow efficient creation of new documents by cloning existing ones.

Your task is to:
1.  Define an abstract `Document` class (the Prototype interface) with:
    -   An `__init__` method that takes a `name`.
    -   An abstract `clone()` method.
    -   A `__str__` method for representation.
2.  Implement two concrete document types:
    -   `Report`: Inherits from `Document`, with additional attributes like `content` (string) and `author` (string).
    -   `Presentation`: Inherits from `Document`, with additional attributes like `slides` (list of strings) and `presenter` (string).
3.  Implement the `clone()` method for both `Report` and `Presentation` to perform a deep copy of the object.

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
        # TODO: Implement deep copy
        pass

    def __str__(self):
        return f"Report: {self.name}, Author: {self.author}, Content: {self.content[:20]}..."

# Concrete Prototype: Presentation
class Presentation(Document):
    def __init__(self, name: str, slides: list, presenter: str):
        super().__init__(name)
        self.slides = slides
        self.presenter = presenter

    def clone(self):
        # TODO: Implement deep copy
        pass

    def __str__(self):
        return f"Presentation: {self.name}, Slides: {len(self.slides)}, Presenter: {self.presenter}"


# --- Tests ---
def run_tests():
    print("Running Prototype Pattern Document Tests...")

    # Test Report Cloning
    original_report = Report("Annual Sales", "Detailed sales figures for Q1-Q4...", "Alice Smith")
    cloned_report = original_report.clone()

    assert original_report is not cloned_report, "Cloned report should be a new object."
    assert original_report.name == cloned_report.name, "Name should be copied."
    assert original_report.content == cloned_report.content, "Content should be copied."
    assert original_report.author == cloned_report.author, "Author should be copied."

    cloned_report.name = "Q1 Sales Summary"
    cloned_report.author = "Bob Johnson"
    cloned_report.content = "Summary of Q1 sales..."

    assert original_report.name == "Annual Sales", "Original report name should not change."
    assert original_report.author == "Alice Smith", "Original report author should not change."
    assert original_report.content == "Detailed sales figures for Q1-Q4...", "Original report content should not change."
    print("Report cloning test passed.")

    # Test Presentation Cloning
    original_slides = ["Intro", "Data", "Conclusion"]
    original_presentation = Presentation("Project Alpha", original_slides, "Charlie Brown")
    cloned_presentation = original_presentation.clone()

    assert original_presentation is not cloned_presentation, "Cloned presentation should be a new object."
    assert original_presentation.name == cloned_presentation.name, "Name should be copied."
    assert original_presentation.presenter == cloned_presentation.presenter, "Presenter should be copied."
    assert original_presentation.slides is not cloned_presentation.slides, "Slides list should be a deep copy."
    assert original_presentation.slides == cloned_presentation.slides, "Slides content should be the same."

    cloned_presentation.name = "Project Beta"
    cloned_presentation.presenter = "Diana Prince"
    cloned_presentation.slides.append("New Slide")

    assert original_presentation.name == "Project Alpha", "Original presentation name should not change."
    assert original_presentation.presenter == "Charlie Brown", "Original presentation presenter should not change."
    assert len(original_presentation.slides) == 3, "Original slides list should not be modified."
    print("Presentation cloning test passed.")

    print("All Prototype Pattern Document Tests Passed!")

if __name__ == "__main__":
    run_tests()
