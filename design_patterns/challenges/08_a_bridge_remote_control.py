from abc import ABC, abstractmethod

"""
Challenge: Remote Control with Bridge Pattern

Design a system for controlling different types of electronic devices (e.g., TV, Radio) 
using various remote controls (e.g., Basic Remote, Advanced Remote).

Your task is to:
1.  Define an abstract `Device` class (Implementation interface) with methods like:
    -   `is_enabled() -> bool`
    -   `enable()`
    -   `disable()`
    -   `get_volume() -> int`
    -   `set_volume(percent: int)`
    -   `get_channel() -> int`
    -   `set_channel(channel: int)`
2.  Implement concrete `TV` and `Radio` classes that inherit from `Device`.
3.  Define an abstract `RemoteControl` class (Abstraction) that takes a `Device` object in its constructor.
    It should have methods like `toggle_power()`, `volume_up()`, `volume_down()`, `channel_up()`, `channel_down()`
    that delegate to the `Device`.
4.  Implement a `AdvancedRemoteControl` class (Refined Abstraction) that inherits from `RemoteControl`
    and adds a new method, `mute()`.

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
        # TODO: Implement power toggle logic
        pass

    def volume_up(self):
        # TODO: Implement volume up logic
        pass

    def volume_down(self):
        # TODO: Implement volume down logic
        pass

    def channel_up(self):
        # TODO: Implement channel up logic
        pass

    def channel_down(self):
        # TODO: Implement channel down logic
        pass

# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        # TODO: Implement mute logic
        pass


# --- Tests ---
def run_tests():
    print("Running Bridge Pattern Remote Control Tests...")

    # Test Basic Remote with TV
    tv = TV()
    basic_remote_tv = RemoteControl(tv)
    print("\nTesting Basic Remote with TV:")
    assert basic_remote_tv.toggle_power() == "TV: ON"
    assert basic_remote_tv.volume_up() == "TV: Volume set to 40"
    assert basic_remote_tv.channel_up() == "TV: Channel set to 2"
    assert basic_remote_tv.toggle_power() == "TV: OFF"
    print("Basic Remote with TV tests passed.")

    # Test Advanced Remote with Radio
    radio = Radio()
    advanced_remote_radio = AdvancedRemoteControl(radio)
    print("\nTesting Advanced Remote with Radio:")
    assert advanced_remote_radio.toggle_power() == "Radio: ON"
    assert advanced_remote_radio.volume_up() == "Radio: Volume set to 60"
    assert advanced_remote_radio.channel_up() == "Radio: Channel set to 100"
    assert advanced_remote_radio.mute() == "Radio: Volume set to 0"
    assert advanced_remote_radio.toggle_power() == "Radio: OFF"
    print("Advanced Remote with Radio tests passed.")

    print("All Bridge Pattern Remote Control Tests Passed!")

if __name__ == "__main__":
    run_tests()
