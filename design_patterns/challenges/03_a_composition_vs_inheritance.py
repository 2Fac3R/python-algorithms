from abc import ABC, abstractmethod

"""
Challenge: Composition vs. Inheritance

This challenge aims to illustrate the differences and trade-offs between composition and inheritance.
You will implement a scenario using both approaches and observe their characteristics.

Your task is to:

1.  **Implement using Inheritance (Bad Example for Flexibility):**
    -   Create a base class `Vehicle` with a `start_engine()` method.
    -   Create a subclass `Car` that inherits from `Vehicle` and adds a `drive()` method.
    -   Create another subclass `ElectricCar` that inherits from `Car` and overrides `start_engine()` to reflect electric starting.

2.  **Implement using Composition (Good Example for Flexibility):**
    -   Define an abstract class `Engine` with an abstract `start()` method.
    -   Create concrete `GasolineEngine` and `ElectricEngine` classes that implement `Engine`.
    -   Create a `CarComposition` class that *composes* an `Engine` object.
    -   The `CarComposition` class should have a `start()` method that delegates to its `Engine`.
    -   The `CarComposition` class should have a `set_engine()` method to change the engine at runtime.

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
        # TODO: Delegate start to the composed engine
        pass

    def set_engine(self, new_engine: Engine):
        # TODO: Allow changing the engine at runtime
        pass


# --- Tests ---
def run_tests():
    print("Running Composition vs. Inheritance Tests...")

    # Test 1: Inheritance
    print("\n--- Testing Inheritance ---")
    vehicle = Vehicle()
    car = Car()
    electric_car = ElectricCar()

    assert vehicle.start_engine() == "Vehicle engine started."
    assert car.start_engine() == "Vehicle engine started."
    assert car.drive() == "Car is driving."
    assert electric_car.start_engine() == "Electric car engine started silently."
    assert electric_car.drive() == "Car is driving."
    print("Inheritance tests passed.")

    # Test 2: Composition
    print("\n--- Testing Composition ---")
    gas_engine = GasolineEngine()
    electric_engine = ElectricEngine()

    car_with_gas_engine = CarComposition(gas_engine)
    assert car_with_gas_engine.start() == "Gasoline engine roaring to life."
    print("Car with Gasoline Engine started.")

    car_with_electric_engine = CarComposition(electric_engine)
    assert car_with_electric_engine.start() == "Electric motor humming to life."
    print("Car with Electric Engine started.")

    # Test changing engine at runtime
    print("\n--- Testing Runtime Engine Change ---")
    car_runtime = CarComposition(gas_engine)
    assert car_runtime.start() == "Gasoline engine roaring to life."
    print("Initial engine: Gasoline.")

    car_runtime.set_engine(electric_engine)
    assert car_runtime.start() == "Electric motor humming to life."
    print("Engine changed to Electric at runtime.")

    print("Composition tests passed.")

    print("All Composition vs. Inheritance Tests Passed!")

if __name__ == "__main__":
    run_tests()
