
from abc import ABC, abstractmethod

"""
Solution for: GUI Abstract Factory
"""

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass

# Concrete Products for Windows
class WindowsButton(Button):
    def paint(self) -> str:
        return "Rendering a button in Windows style."

class WindowsCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a checkbox in Windows style."

# Concrete Products for macOS
class MacOSButton(Button):
    def paint(self) -> str:
        return "Rendering a button in macOS style."

class MacOSCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a checkbox in macOS style."

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Client Code
def client_application(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.paint())
    print(checkbox.paint())
