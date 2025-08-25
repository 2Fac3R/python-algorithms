
from abc import ABC, abstractmethod

"""
Challenge: Abstract Classes and Interfaces in Python

This challenge aims to assess your understanding of Abstract Classes and Interfaces in Python using the `abc` module.

Your task is to:

1.  **Abstract Class Definition:**
    -   Define an abstract class `Vehicle` that inherits from `ABC`.
    -   It should have an `__init__` method that takes `make` and `model`.
    -   It should have an abstract method `start_engine()` that returns a string.
    -   It should have a concrete method `get_info()` that returns a string with make and model.

2.  **Concrete Subclass:**
    -   Implement a concrete class `Car` that inherits from `Vehicle`.
    -   `Car` should have an additional attribute `num_doors`.
    -   `Car` must implement the `start_engine()` method to return a specific message for a car.

3.  **Interface Definition (using ABC):**
    -   Define an abstract class `Flyable` that inherits from `ABC`.
    -   It should have an abstract method `fly()` that returns a string.

4.  **Class Implementing Interface:**
    -   Implement a class `Airplane` that inherits from `Vehicle` (from step 1) and `Flyable` (from step 3).
    -   `Airplane` should have an additional attribute `max_altitude`.
    -   `Airplane` must implement both `start_engine()` and `fly()`.

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
        # TODO: Implement start_engine for Car
        pass

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
        # TODO: Implement start_engine for Airplane
        pass

    def fly(self) -> str:
        # TODO: Implement fly for Airplane
        pass


# --- Tests ---
def run_tests():
    print("Running Abstract Classes and Interfaces Tests...")

    # Test 1 & 2: Vehicle and Car
    try:
        # Vehicle should be abstract
        Vehicle("Test", "Vehicle")
        assert False, "Vehicle class should be abstract and not instantiable."
    except TypeError as e:
        assert "Can't instantiate abstract class Vehicle with abstract method start_engine" in str(e)

    car = Car("Toyota", "Camry", 4)
    assert car.get_info() == "Make: Toyota, Model: Camry"
    assert car.start_engine() == "Car engine started."
    print("Test 1 & 2 (Vehicle and Car) Passed.")

    # Test 3 & 4: Flyable and Airplane
    try:
        # Flyable should be abstract
        Flyable()
        assert False, "Flyable class should be abstract and not instantiable."
    except TypeError as e:
        assert "Can't instantiate abstract class Flyable with abstract method fly" in str(e)

    airplane = Airplane("Boeing", "747", 40000)
    assert airplane.get_info() == "Make: Boeing, Model: 747"
    assert airplane.start_engine() == "Airplane engine started."
    assert airplane.fly() == "Airplane flying at 40000 feet."
    print("Test 3 & 4 (Flyable and Airplane) Passed.")

    print("All Abstract Classes and Interfaces Tests Passed!")

if __name__ == "__main__":
    run_tests()
