
from abc import ABC, abstractmethod
from typing import List

"""
Challenge: Simple Remote Control with Command Pattern

Design a simple remote control that can operate various devices (e.g., Light, Garage Door).
Your remote control should be able to turn lights on/off and open/close the garage door.
It should also support an undo functionality for the last executed command.

Your task is to:
1.  Define a `Command` abstract class with `execute()` and `undo()` abstract methods.
2.  Define `Light` and `GarageDoor` classes (Receivers) with methods like `on()`, `off()`, `up()`, `down()`.
3.  Implement concrete `Command` classes for each action:
    -   `LightOnCommand`, `LightOffCommand`
    -   `GarageDoorUpCommand`, `GarageDoorDownCommand`
    Each command should store a reference to its respective receiver and implement `execute()` and `undo()`.
    For `LightOnCommand` and `LightOffCommand`, ensure `undo()` restores the *previous* state of the light.
4.  Implement an `Invoker` class, `RemoteControl`.
    -   It should have slots to hold `on` and `off` commands.
    -   It should have methods `set_command(slot, on_command, off_command)`.
    -   It should have methods `on_button_was_pressed(slot)`, `off_button_was_pressed(slot)` that execute the command and store it for undo.
    -   It should have an `undo_button_was_pressed()` method that executes the `undo()` of the last command.
5.  Implement a `NoCommand` (Null Object) for unassigned slots or no undoable action.

"""

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver: Light
class Light:
    def on(self):
        return "Light is ON"

    def off(self):
        return "Light is OFF"

# Receiver: GarageDoor
class GarageDoor:
    def up(self):
        return "Garage Door is OPEN"

    def down(self):
        return "Garage Door is CLOSED"

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light
        self._previous_state = None # To store state for undo

    def execute(self):
        # TODO: Implement execute and store previous state
        pass

    def undo(self):
        # TODO: Implement undo based on previous state
        pass

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light
        self._previous_state = None # To store state for undo

    def execute(self):
        # TODO: Implement execute and store previous state
        pass

    def undo(self):
        # TODO: Implement undo based on previous state
        pass

class GarageDoorUpCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self._garage_door = garage_door

    def execute(self):
        # TODO: Implement execute
        pass

    def undo(self):
        # TODO: Implement undo
        pass

class GarageDoorDownCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self._garage_door = garage_door

    def execute(self):
        # TODO: Implement execute
        pass

    def undo(self):
        # TODO: Implement undo
        pass

# Null Object for no command
class NoCommand(Command):
    def execute(self):
        return "No command assigned."

    def undo(self):
        return "No command to undo."

# Invoker: RemoteControl
class RemoteControl:
    def __init__(self):
        self._on_commands: List[Command] = [NoCommand()] * 7
        self._off_commands: List[Command] = [NoCommand()] * 7
        self._undo_command: Command = NoCommand()

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pressed(self, slot: int):
        # TODO: Implement execute and store for undo
        pass

    def off_button_was_pressed(self, slot: int):
        # TODO: Implement execute and store for undo
        pass

    def undo_button_was_pressed(self):
        # TODO: Implement undo
        pass


# --- Tests ---
def run_tests():
    print("Running Command Pattern Remote Control Tests...")

    remote = RemoteControl()

    living_room_light = Light()
    garage_door = GarageDoor()

    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    remote.set_command(0, light_on, light_off)
    remote.set_command(1, garage_door_up, garage_door_down)

    # Test Light On/Off and Undo
    print("\n--- Testing Light ---")
    assert remote.on_button_was_pressed(0) == "Light is ON"
    assert remote.undo_button_was_pressed() == "Light is OFF"
    assert remote.off_button_was_pressed(0) == "Light is OFF"
    assert remote.undo_button_was_pressed() == "Light is ON"
    print("Light tests passed.")

    # Test Garage Door Up/Down and Undo
    print("\n--- Testing Garage Door ---")
    assert remote.on_button_was_pressed(1) == "Garage Door is OPEN"
    assert remote.undo_button_was_pressed() == "Garage Door is CLOSED"
    assert remote.off_button_was_pressed(1) == "Garage Door is CLOSED"
    assert remote.undo_button_was_pressed() == "Garage Door is OPEN"
    print("Garage Door tests passed.")

    # Test unassigned slot
    print("\n--- Testing Unassigned Slot ---")
    assert remote.on_button_was_pressed(2) == "No command assigned to ON button."
    assert remote.undo_button_was_pressed() == "No command to undo."
    print("Unassigned slot test passed.")

    print("All Command Pattern Remote Control Tests Passed!")

if __name__ == "__main__":
    run_tests()
