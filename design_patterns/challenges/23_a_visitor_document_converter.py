from abc import ABC, abstractmethod
from typing import List

"""
Challenge: Document Converter with Visitor Pattern

Design a document processing system that can convert a document composed of different elements
(e.g., Paragraphs, Headings) into various output formats (e.g., HTML, Markdown).

Your task is to:
1.  Define an abstract `DocumentElement` class (Element interface) with an abstract `accept(visitor: 'DocumentVisitor')` method.
2.  Implement concrete element classes:
    -   `Paragraph`: Stores `text` (string). Its `accept` method should call `visitor.visit_paragraph(self)`.
    -   `Heading`: Stores `text` (string) and `level` (int). Its `accept` method should call `visitor.visit_heading(self)`.
3.  Define an abstract `DocumentVisitor` class (Visitor interface) with abstract `visit()` methods for each concrete element type:
    -   `visit_paragraph(paragraph: Paragraph)`
    -   `visit_heading(heading: Heading)`
4.  Implement concrete visitor classes:
    -   `HTMLConverter`: Implements `DocumentVisitor`. Its `visit_paragraph` should append `<p>{text}</p>` to an internal output list. Its `visit_heading` should append `<h{level}>{text}</h{level}>`. It should have a `get_html()` method to return the combined HTML string.
    -   `MarkdownConverter`: Implements `DocumentVisitor`. Its `visit_paragraph` should append the raw text. Its `visit_heading` should append `#{level} {text}`. It should have a `get_markdown()` method to return the combined Markdown string.
5.  Implement a `Document` class (Object Structure) that holds a list of `DocumentElement` objects and has an `accept(visitor: DocumentVisitor)` method that iterates through its elements, calling `element.accept(visitor)` on each.

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
        # TODO: Call the appropriate visit method on the visitor
        pass

class Heading(DocumentElement):
    def __init__(self, text: str, level: int):
        self.text = text
        self.level = level

    def accept(self, visitor: 'DocumentVisitor'):
        # TODO: Call the appropriate visit method on the visitor
        pass

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
        # TODO: Append HTML for paragraph
        pass

    def visit_heading(self, heading: Heading):
        # TODO: Append HTML for heading
        pass

    def get_html(self) -> str:
        return "\n".join(self.output)

class MarkdownConverter(DocumentVisitor):
    def __init__(self):
        self.output = []

    def visit_paragraph(self, paragraph: Paragraph):
        # TODO: Append Markdown for paragraph
        pass

    def visit_heading(self, heading: Heading):
        # TODO: Append Markdown for heading
        pass

    def get_markdown(self) -> str:
        return "\n".join(self.output)

# Object Structure (Document)
class Document:
    def __init__(self, elements: List[DocumentElement]):
        self.elements = elements

    def accept(self, visitor: DocumentVisitor):
        # TODO: Iterate through elements and call accept on each
        pass


# --- Tests ---
def run_tests():
    print("Running Visitor Pattern Document Converter Tests...")

    document = Document([
        Heading("Introduction", 1),
        Paragraph("This is a sample paragraph."),
        Heading("Conclusion", 2),
        Paragraph("End of document.")
    ])

    # Test HTML Conversion
    html_converter = HTMLConverter()
    document.accept(html_converter)
    expected_html = (
        "<h1>Introduction</h1>\n" +
        "<p>This is a sample paragraph.</p>\n" +
        "<h2>Conclusion</h2>\n" +
        "<p>End of document.</p>"
    )
    assert html_converter.get_html() == expected_html, f"HTML conversion failed.\nExpected:\n{expected_html}\nGot:\n{html_converter.get_html()}"
    print("HTML conversion test passed.")

    # Test Markdown Conversion
    markdown_converter = MarkdownConverter()
    document.accept(markdown_converter)
    expected_markdown = (
        "# Introduction\n" +
        "This is a sample paragraph.\n" +
        "## Conclusion\n" +
        "End of document."
    )
    assert markdown_converter.get_markdown() == expected_markdown, f"Markdown conversion failed.\nExpected:\n{expected_markdown}\nGot:\n{markdown_converter.get_markdown()}"
    print("Markdown conversion test passed.")

    print("All Visitor Pattern Document Converter Tests Passed!")

if __name__ == "__main__":
    run_tests()
