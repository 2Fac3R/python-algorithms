from abc import ABC, abstractmethod

"""
Challenge: GUI Abstract Factory

Design a GUI system that can create families of UI elements (Button and Checkbox)
for different operating systems (Windows and macOS).

Your task is to:
1.  Define abstract `Button` and `Checkbox` product interfaces.
2.  Implement concrete `WindowsButton`, `WindowsCheckbox`, `MacOSButton`, and `MacOSCheckbox` classes.
3.  Define an abstract `GUIFactory` that declares methods for creating a Button and a Checkbox.
4.  Implement concrete `WindowsFactory` and `MacOSFactory` classes that produce the respective UI elements.
5.  Implement a `client_application` function that takes a `GUIFactory` and uses it to create and paint a button and a checkbox.

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
    # TODO: Implement the client application logic here
    # It should create a button and a checkbox using the provided factory
    # and then call their paint methods.
    pass

# --- Tests ---
def run_tests():
    print("Running Abstract Factory GUI Tests...")

    # Test with Windows Factory
    print("\nTesting with Windows factory:")
    windows_factory = WindowsFactory()
    windows_button = windows_factory.create_button()
    windows_checkbox = windows_factory.create_checkbox()

    assert windows_button.paint() == "Rendering a button in Windows style."
    assert windows_checkbox.paint() == "Rendering a checkbox in Windows style."
    print("Windows UI elements created and painted correctly.")

    # Test with macOS Factory
    print("\nTesting with macOS factory:")
    macos_factory = MacOSFactory()
    macos_button = macos_factory.create_button()
    macos_checkbox = macos_factory.create_checkbox()

    assert macos_button.paint() == "Rendering a button in macOS style."
    assert macos_checkbox.paint() == "Rendering a checkbox in macOS style."
    print("macOS UI elements created and painted correctly.")

    # Test client application
    print("\nTesting client application:")
    # This part will require you to implement client_application first
    # For now, we'll just call it and expect it not to crash.
    try:
        print("Client application with Windows factory:")
        client_application(WindowsFactory())
        print("Client application with macOS factory:")
        client_application(MacOSFactory())
        print("Client application calls completed.")
    except Exception as e:
        print(f"Client application test failed: {e}")

if __name__ == "__main__":
    run_tests()
