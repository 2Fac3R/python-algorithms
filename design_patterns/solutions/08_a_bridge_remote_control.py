
from abc import ABC, abstractmethod

"""
Solution for: Remote Control with Bridge Pattern
"""

# Implementation Interface
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percent: int):
        pass

    @abstractmethod
    def get_channel(self) -> int:
        pass

    @abstractmethod
    def set_channel(self, channel: int):
        pass

# Concrete Implementations
class TV(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 30
        self._channel = 1

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self):
        self._enabled = True
        return "TV: ON"

    def disable(self):
        self._enabled = False
        return "TV: OFF"

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self._volume = percent
            return f"TV: Volume set to {self._volume}"
        return "TV: Invalid volume."

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int):
        self._channel = channel
        return f"TV: Channel set to {self._channel}"

class Radio(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 50
        self._channel = 99

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self):
        self._enabled = True
        return "Radio: ON"

    def disable(self):
        self._enabled = False
        return "Radio: OFF"

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self._volume = percent
            return f"Radio: Volume set to {self._volume}"
        return "Radio: Invalid volume."

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int):
        self._channel = channel
        return f"Radio: Channel set to {self._channel}"

# Abstraction
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            return self._device.disable()
        else:
            return self._device.enable()

    def volume_up(self):
        return self._device.set_volume(self._device.get_volume() + 10)

    def volume_down(self):
        return self._device.set_volume(self._device.get_volume() - 10)

    def channel_up(self):
        return self._device.set_channel(self._device.get_channel() + 1)

    def channel_down(self):
        return self._device.set_channel(self._device.get_channel() - 1)

# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        return self._device.set_volume(0)
