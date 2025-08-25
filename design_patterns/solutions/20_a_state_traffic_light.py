
from abc import ABC, abstractmethod

"""
Solution for: Traffic Light with State Pattern
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
        print("Traffic Light: Red -> Green")
        light.set_state(GreenLightState())

    def get_status(self) -> str:
        return "Red"

class YellowLightState(TrafficLightState):
    def handle(self, light: 'TrafficLight'):
        print("Traffic Light: Yellow -> Red")
        light.set_state(RedLightState())

    def get_status(self) -> str:
        return "Yellow"

class GreenLightState(TrafficLightState):
    def handle(self, light: 'TrafficLight'):
        print("Traffic Light: Green -> Yellow")
        light.set_state(YellowLightState())

    def get_status(self) -> str:
        return "Green"

# Context
class TrafficLight:
    def __init__(self):
        self._state: TrafficLightState = RedLightState() # Initial state

    def set_state(self, state: TrafficLightState):
        self._state = state

    def change(self):
        self._state.handle(self)

    def get_current_status(self) -> str:
        return self._state.get_status()
