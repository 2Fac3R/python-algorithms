
from abc import ABC, abstractmethod

"""
Challenge: Coffee Shop Decorator

Design a coffee shop system where you can order a basic coffee and then add various condiments
(e.g., Milk, Sugar, Caramel) to it. Each condiment should add to the cost and description of the coffee.

Your task is to:
1.  Define an abstract `Coffee` class (Component interface) with abstract methods:
    -   `get_cost() -> float`: Returns the cost of the coffee.
    -   `get_description() -> str`: Returns the description of the coffee.
2.  Implement a `SimpleCoffee` class (Concrete Component) that inherits from `Coffee`.
    -   It should have a base cost and description.
3.  Define an abstract `CoffeeDecorator` class (Decorator) that inherits from `Coffee`.
    -   Its constructor should take a `decorated_coffee` object (another `Coffee` instance).
    -   Its `get_cost()` and `get_description()` methods should be abstract.
4.  Implement concrete decorators:
    -   `Milk`: Adds a cost and appends ", Milk" to the description.
    -   `Sugar`: Adds a cost and appends ", Sugar" to the description.
    -   `Caramel`: Adds a cost and appends ", Caramel" to the description.

"""

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 5.0

    def get_description(self) -> str:
        return "Simple Coffee"

# Decorator Abstract Class
class CoffeeDecorator(Coffee, ABC):
    def __init__(self, decorated_coffee: Coffee):
        self._decorated_coffee = decorated_coffee

    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# Concrete Decorators
class Milk(CoffeeDecorator):
    def __init__(self, decorated_coffee: Coffee):
        super().__init__(decorated_coffee)

    def get_cost(self) -> float:
        # TODO: Implement cost for Milk
        pass

    def get_description(self) -> str:
        # TODO: Implement description for Milk
        pass

class Sugar(CoffeeDecorator):
    def __init__(self, decorated_coffee: Coffee):
        super().__init__(decorated_coffee)

    def get_cost(self) -> float:
        # TODO: Implement cost for Sugar
        pass

    def get_description(self) -> str:
        # TODO: Implement description for Sugar
        pass

class Caramel(CoffeeDecorator):
    def __init__(self, decorated_coffee: Coffee):
        super().__init__(decorated_coffee)

    def get_cost(self) -> float:
        # TODO: Implement cost for Caramel
        pass

    def get_description(self) -> str:
        # TODO: Implement description for Caramel
        pass


# --- Tests ---
def run_tests():
    print("Running Decorator Pattern Coffee Shop Tests...")

    # Test Simple Coffee
    coffee = SimpleCoffee()
    assert coffee.get_description() == "Simple Coffee"
    assert coffee.get_cost() == 5.0
    print(f"Simple Coffee: {coffee.get_description()}, Cost: ${coffee.get_cost():.2f}")

    # Test Coffee with Milk
    coffee_with_milk = Milk(coffee)
    assert coffee_with_milk.get_description() == "Simple Coffee, Milk"
    assert coffee_with_milk.get_cost() == 6.5 # 5.0 + 1.5
    print(f"Coffee with Milk: {coffee_with_milk.get_description()}, Cost: ${coffee_with_milk.get_cost():.2f}")

    # Test Coffee with Milk and Sugar
    coffee_with_milk_sugar = Sugar(Milk(SimpleCoffee()))
    assert coffee_with_milk_sugar.get_description() == "Simple Coffee, Milk, Sugar"
    assert coffee_with_milk_sugar.get_cost() == 7.0 # 5.0 + 1.5 + 0.5
    print(f"Coffee with Milk & Sugar: {coffee_with_milk_sugar.get_description()}, Cost: ${coffee_with_milk_sugar.get_cost():.2f}")

    # Test Coffee with Caramel and then Milk
    coffee_caramel_milk = Milk(Caramel(SimpleCoffee()))
    assert coffee_caramel_milk.get_description() == "Simple Coffee, Caramel, Milk"
    assert coffee_caramel_milk.get_cost() == 8.5 # 5.0 + 2.0 + 1.5
    print(f"Coffee with Caramel & Milk: {coffee_caramel_milk.get_description()}, Cost: ${coffee_caramel_milk.get_cost():.2f}")

    print("All Decorator Pattern Coffee Shop Tests Passed!")

if __name__ == "__main__":
    run_tests()
