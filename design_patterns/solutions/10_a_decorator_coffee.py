
from abc import ABC, abstractmethod

"""
Solution for: Coffee Shop Decorator
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
        return self._decorated_coffee.get_cost() + 1.5

    def get_description(self) -> str:
        return self._decorated_coffee.get_description() + ", Milk"

class Sugar(CoffeeDecorator):
    def __init__(self, decorated_coffee: Coffee):
        super().__init__(decorated_coffee)

    def get_cost(self) -> float:
        return self._decorated_coffee.get_cost() + 0.5

    def get_description(self) -> str:
        return self._decorated_coffee.get_description() + ", Sugar"

class Caramel(CoffeeDecorator):
    def __init__(self, decorated_coffee: Coffee):
        super().__init__(decorated_coffee)

    def get_cost(self) -> float:
        return self._decorated_coffee.get_cost() + 2.0

    def get_description(self) -> str:
        return self._decorated_coffee.get_description() + ", Caramel"
