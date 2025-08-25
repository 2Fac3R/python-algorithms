from abc import ABC, abstractmethod
from typing import List

"""
Solution for: Document Converter with Visitor Pattern
"""

# Element Interface
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: 'DocumentVisitor'):
        pass

# Concrete Elements
class Paragraph(DocumentElement):
    def __init__(self, text: str):
        self.text = text

    def accept(self, visitor: 'DocumentVisitor'):
        visitor.visit_paragraph(self)

class Heading(DocumentElement):
    def __init__(self, text: str, level: int):
        self.text = text
        self.level = level

    def accept(self, visitor: 'DocumentVisitor'):
        visitor.visit_heading(self)

# Visitor Interface
class DocumentVisitor(ABC):
    @abstractmethod
    def visit_paragraph(self, paragraph: Paragraph):
        pass

    @abstractmethod
    def visit_heading(self, heading: Heading):
        pass

# Concrete Visitors
class HTMLConverter(DocumentVisitor):
    def __init__(self):
        self.output = []

    def visit_paragraph(self, paragraph: Paragraph):
        self.output.append(f"<p>{paragraph.text}</p>")

    def visit_heading(self, heading: Heading):
        self.output.append(f"<h{heading.level}>{heading.text}</h{heading.level}>")

    def get_html(self) -> str:
        return "\n".join(self.output)

class MarkdownConverter(DocumentVisitor):
    def __init__(self):
        self.output = []

    def visit_paragraph(self, paragraph: Paragraph):
        self.output.append(paragraph.text)

    def visit_heading(self, heading: Heading):
        self.output.append("#" * heading.level + f" {heading.text}")

    def get_markdown(self) -> str:
        return "\n".join(self.output)

# Object Structure (Document)
class Document:
    def __init__(self, elements: List[DocumentElement]):
        self.elements = elements

    def accept(self, visitor: DocumentVisitor):
        for element in self.elements:
            element.accept(visitor)
