
Challenge: Text Editor Undo/Redo with Memento Pattern

Design a simple text editor that supports undo functionality. The editor should be able to save its current state
and restore to a previously saved state.

Your task is to:
1.  Implement an `EditorMemento` class (Memento) that stores the content of the editor at a specific point in time.
    -   It should have a private attribute `_content` to store the string content.
    -   It should have a method `get_saved_content()` to retrieve the content.
2.  Implement a `TextEditor` class (Originator) with:
    -   A private attribute `_content` to hold the current text.
    -   A `type(words: str)` method to append text to the current content.
    -   A `get_content()` method to return the current content.
    -   A `save() -> EditorMemento` method that creates and returns an `EditorMemento` object with the current content.
    -   A `restore(memento: EditorMemento)` method that restores the editor's content from the provided memento.
3.  Implement a `History` class (Caretaker) with:
    -   A private list `_mementos` to store `EditorMemento` objects.
    -   A `save(editor: TextEditor)` method that takes a `TextEditor` object, calls its `save()` method, and adds the returned memento to its list.
    -   An `undo(editor: TextEditor)` method that retrieves the last memento from its list (if any), calls the editor's `restore()` method with that memento, and removes the memento from its list.


# Memento
class EditorMemento:
    def __init__(self, content: str):
        self._content = content

    def get_saved_content(self) -> str:
        return self._content

# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def type(self, words: str):
        self._content += words
        return f"Current content: {self._content}"

    def get_content(self) -> str:
        return self._content

    def save(self) -> EditorMemento:
        # TODO: Implement save method
        pass

    def restore(self, memento: EditorMemento):
        # TODO: Implement restore method
        pass

# Caretaker
class History:
    def __init__(self):
        self._mementos = []

    def save(self, editor: TextEditor):
        # TODO: Implement save method
        pass

    def undo(self, editor: TextEditor):
        # TODO: Implement undo method
        pass


# --- Tests ---
def run_tests():
    print("Running Memento Pattern Text Editor Tests...")

    editor = TextEditor()
    history = History()

    # Initial state
    print(editor.type("Hello. "))
    history.save(editor)
    assert editor.get_content() == "Hello. "

    # State 2
    print(editor.type("How are you? "))
    history.save(editor)
    assert editor.get_content() == "Hello. How are you? "

    # State 3 (not saved)
    print(editor.type("I am fine."))
    assert editor.get_content() == "Hello. How are you? I am fine."

    # Undo to State 2
    print("\nPerforming undo...")
    history.undo(editor)
    assert editor.get_content() == "Hello. How are you? "
    print(f"Editor content after undo: {editor.get_content()}")

    # Undo to State 1
    print("\nPerforming another undo...")
    history.undo(editor)
    assert editor.get_content() == "Hello. "
    print(f"Editor content after second undo: {editor.get_content()}")

    # Try to undo again (no more states)
    print("\nTrying to undo again (no more states)...")
    history.undo(editor)
    assert editor.get_content() == "Hello. " # Should remain at last available state
    print(f"Editor content after third undo attempt: {editor.get_content()}")

    print("All Memento Pattern Text Editor Tests Passed!")

if __name__ == "__main__":
    run_tests()
