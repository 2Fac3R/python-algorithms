
from abc import ABC, abstractmethod

"""
Solution for: Composition vs. Inheritance
"""

# 1. Implement using Inheritance
class Vehicle:
    def start_engine(self):
        return "Vehicle engine started."

class Car(Vehicle):
    def drive(self):
        return "Car is driving."

class ElectricCar(Car):
    def start_engine(self):
        return "Electric car engine started silently."


# 2. Implement using Composition
class Engine(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

class GasolineEngine(Engine):
    def start(self) -> str:
        return "Gasoline engine roaring to life."

class ElectricEngine(Engine):
    def start(self) -> str:
        return "Electric motor humming to life."

class CarComposition:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self) -> str:
        return self.engine.start()

    def set_engine(self, new_engine: Engine):
        self.engine = new_engine
