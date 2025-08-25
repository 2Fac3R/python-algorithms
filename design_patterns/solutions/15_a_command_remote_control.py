
from abc import ABC, abstractmethod
from typing import List

"""
Solution for: Simple Remote Control with Command Pattern
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
        self._previous_state = None

    def execute(self):
        # Store current state before changing it for undo functionality
        # This is a simplification; in a real scenario, you'd query the light's actual state
        self._previous_state = "OFF" if self._light.on() == "Light is ON" else "ON"
        return self._light.on()

    def undo(self):
        if self._previous_state == "OFF":
            return self._light.off()
        elif self._previous_state == "ON":
            return self._light.on()
        return "Light state unknown for undo."

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light
        self._previous_state = None

    def execute(self):
        self._previous_state = "ON" if self._light.off() == "Light is OFF" else "OFF"
        return self._light.off()

    def undo(self):
        if self._previous_state == "ON":
            return self._light.on()
        elif self._previous_state == "OFF":
            return self._light.off()
        return "Light state unknown for undo."

class GarageDoorUpCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self._garage_door = garage_door

    def execute(self):
        return self._garage_door.up()

    def undo(self):
        return self._garage_door.down()

class GarageDoorDownCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self._garage_door = garage_door

    def execute(self):
        return self._garage_door.down()

    def undo(self):
        return self._garage_door.up()

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
        if self._on_commands[slot]:
            result = self._on_commands[slot].execute()
            self._undo_command = self._on_commands[slot]
            return result
        return "No command assigned to ON button."

    def off_button_was_pressed(self, slot: int):
        if self._off_commands[slot]:
            result = self._off_commands[slot].execute()
            self._undo_command = self._off_commands[slot]
            return result
        return "No command assigned to OFF button."

    def undo_button_was_pressed(self):
        return self._undo_command.undo()
