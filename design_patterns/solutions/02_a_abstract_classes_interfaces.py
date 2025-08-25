
from abc import ABC, abstractmethod

"""
Solution for: Abstract Classes and Interfaces in Python
"""

# 1. Abstract Class Definition
class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> str:
        pass

    def get_info(self) -> str:
        return f"Make: {self.make}, Model: {self.model}"

# 2. Concrete Subclass
class Car(Vehicle):
    def __init__(self, make: str, model: str, num_doors: int):
        super().__init__(make, model)
        self.num_doors = num_doors

    def start_engine(self) -> str:
        return "Car engine started."

# 3. Interface Definition (using ABC)
class Flyable(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass

# 4. Class Implementing Interface
class Airplane(Vehicle, Flyable):
    def __init__(self, make: str, model: str, max_altitude: int):
        super().__init__(make, model)
        self.max_altitude = max_altitude

    def start_engine(self) -> str:
        return "Airplane engine started."

    def fly(self) -> str:
        return f"Airplane flying at {self.max_altitude} feet."
