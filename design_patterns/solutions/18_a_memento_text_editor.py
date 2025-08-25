
"""
Solution for: Text Editor Undo/Redo with Memento Pattern
"""

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
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento):
        self._content = memento.get_saved_content()
        return f"Content restored to: {self._content}"

# Caretaker
class History:
    def __init__(self):
        self._mementos = []

    def save(self, editor: TextEditor):
        self._mementos.append(editor.save())
        print("State saved.")

    def undo(self, editor: TextEditor):
        if not self._mementos:
            print("No states to undo.")
            return
        memento = self._mementos.pop()
        editor.restore(memento)
        print("Undo successful.")
