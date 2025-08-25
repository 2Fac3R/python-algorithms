
from abc import ABC, abstractmethod

"""
Challenge: Traffic Light with State Pattern

Design a traffic light system where the traffic light changes its behavior (color) based on its internal state.

Your task is to:
1.  Define an abstract `TrafficLightState` class (State interface) with:
    -   An abstract `handle(light: 'TrafficLight')` method to define state-specific behavior and transitions.
    -   An abstract `get_status() -> str` method to return the current color/status.
2.  Implement concrete state classes:
    -   `RedLightState`
    -   `YellowLightState`
    -   `GreenLightState`
    Each concrete state's `handle` method should transition the `TrafficLight` to the next appropriate state.
3.  Implement a `TrafficLight` class (Context) with:
    -   A private attribute `_state` to hold the current `TrafficLightState`.
    -   An `__init__` method to set an initial state (e.g., `RedLightState`).
    -   A `set_state(state: TrafficLightState)` method to change the current state.
    -   A `change()` method that delegates to the current state's `handle()` method.
    -   A `get_current_status()` method that delegates to the current state's `get_status()` method.

"""

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, light: 'TrafficLight'):
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

# Concrete States
class RedLightState(TrafficLightState):
    def handle(self, light: 'TrafficLight'):
        # TODO: Implement state transition to GreenLightState
        pass

    def get_status(self) -> str:
        return "Red"

class YellowLightState(TrafficLightState):
    def handle(self, light: 'TrafficLight'):
        # TODO: Implement state transition to RedLightState
        pass

    def get_status(self) -> str:
        return "Yellow"

class GreenLightState(TrafficLightState):
    def handle(self, light: 'TrafficLight'):
        # TODO: Implement state transition to YellowLightState
        pass

    def get_status(self) -> str:
        return "Green"

# Context
class TrafficLight:
    def __init__(self):
        self._state: TrafficLightState = RedLightState() # Initial state

    def set_state(self, state: TrafficLightState):
        self._state = state

    def change(self):
        # TODO: Delegate to current state's handle method
        pass

    def get_current_status(self) -> str:
        # TODO: Delegate to current state's get_status method
        pass


# --- Tests ---
def run_tests():
    print("Running State Pattern Traffic Light Tests...")

    traffic_light = TrafficLight()

    # Test initial state
    assert traffic_light.get_current_status() == "Red"
    print(f"Initial status: {traffic_light.get_current_status()}")

    # Test Red -> Green
    traffic_light.change()
    assert traffic_light.get_current_status() == "Green"
    print(f"Current status: {traffic_light.get_current_status()}")

    # Test Green -> Yellow
    traffic_light.change()
    assert traffic_light.get_current_status() == "Yellow"
    print(f"Current status: {traffic_light.get_current_status()}")

    # Test Yellow -> Red
    traffic_light.change()
    assert traffic_light.get_current_status() == "Red"
    print(f"Current status: {traffic_light.get_current_status()}")

    # Test Red -> Green again
    traffic_light.change()
    assert traffic_light.get_current_status() == "Green"
    print(f"Current status: {traffic_light.get_current_status()}")

    print("All State Pattern Traffic Light Tests Passed!")

if __name__ == "__main__":
    run_tests()
