
from abc import ABC, abstractmethod
from typing import List

"""
Solution for: Pizza Builder
"""

# Product: Pizza
class Pizza:
    def __init__(self):
        self.parts = []

    def add(self, part: str):
        self.parts.append(part)

    def list_parts(self) -> str:
        return f"Pizza parts: {', '.join(self.parts)}"

# Builder Interface
class PizzaBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_topping(self):
        pass

    @abstractmethod
    def get_product(self) -> Pizza:
        pass

# Concrete Builder: Margherita Pizza Builder
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.product = Pizza()

    def reset(self):
        self.product = Pizza()

    def build_dough(self):
        self.product.add("thin crust dough")

    def build_sauce(self):
        self.product.add("tomato sauce")

    def build_topping(self):
        self.product.add("mozzarella cheese")
        self.product.add("fresh basil")

    def get_product(self) -> Pizza:
        product = self.product
        self.reset()
        return product

# Concrete Builder: Pepperoni Pizza Builder
class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.product = Pizza()

    def reset(self):
        self.product = Pizza()

    def build_dough(self):
        self.product.add("thick crust dough")

    def build_sauce(self):
        self.product.add("spicy tomato sauce")

    def build_topping(self):
        self.product.add("mozzarella cheese")
        self.product.add("pepperoni slices")
        self.product.add("oregano")

    def get_product(self) -> Pizza:
        product = self.product
        self.reset()
        return product

# Director
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder

    def set_builder(self, builder: PizzaBuilder):
        self._builder = builder

    def build_margherita_pizza(self):
        self._builder.reset()
        self._builder.build_dough()
        self._builder.build_sauce()
        self._builder.build_topping()

    def build_pepperoni_pizza(self):
        self._builder.reset()
        self._builder.build_dough()
        self._builder.build_sauce()
        self._builder.build_topping()
