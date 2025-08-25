
from abc import ABC, abstractmethod
from typing import List

"""
Challenge: Pizza Builder

Design a system to construct different types of pizzas step-by-step using the Builder pattern.

Your task is to:
1.  Define a `Pizza` class (the Product) that can hold various parts (dough, sauce, toppings).
2.  Define an abstract `PizzaBuilder` interface with methods for:
    -   `reset()`: To clear the current pizza being built.
    -   `build_dough()`: To set the dough type.
    -   `build_sauce()`: To set the sauce type.
    -   `build_topping()`: To add toppings.
    -   `get_product()`: To retrieve the constructed `Pizza` object.
3.  Implement two concrete builders:
    -   `MargheritaPizzaBuilder`: Builds a Margherita pizza (thin crust, tomato sauce, mozzarella, basil).
    -   `PepperoniPizzaBuilder`: Builds a Pepperoni pizza (thick crust, spicy tomato sauce, mozzarella, pepperoni, oregano).
4.  Implement a `PizzaDirector` class that can construct predefined pizza types using a `PizzaBuilder`.
    -   It should have a `set_builder` method to set the current builder.
    -   It should have methods like `build_margherita_pizza()` and `build_pepperoni_pizza()` that orchestrate the builder's steps.

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
        # TODO: Implement the steps to build a Margherita pizza using the builder
        pass

    def build_pepperoni_pizza(self):
        # TODO: Implement the steps to build a Pepperoni pizza using the builder
        pass


# --- Tests ---
def run_tests():
    print("Running Builder Pattern Pizza Tests...")

    # Test Margherita Pizza
    margherita_builder = MargheritaPizzaBuilder()
    director = PizzaDirector(margherita_builder)
    director.build_margherita_pizza()
    margherita_pizza = margherita_builder.get_product()
    expected_margherita = "Pizza parts: thin crust dough, tomato sauce, mozzarella cheese, fresh basil"
    assert margherita_pizza.list_parts() == expected_margherita, f"Margherita Test Failed: {margherita_pizza.list_parts()}"
    print(f"Margherita Pizza Test Passed: {margherita_pizza.list_parts()}")

    # Test Pepperoni Pizza
    pepperoni_builder = PepperoniPizzaBuilder()
    director.set_builder(pepperoni_builder)
    director.build_pepperoni_pizza()
    pepperoni_pizza = pepperoni_builder.get_product()
    expected_pepperoni = "Pizza parts: thick crust dough, spicy tomato sauce, mozzarella cheese, pepperoni slices, oregano"
    assert pepperoni_pizza.list_parts() == expected_pepperoni, f"Pepperoni Test Failed: {pepperoni_pizza.list_parts()}"
    print(f"Pepperoni Pizza Test Passed: {pepperoni_pizza.list_parts()}")

    # Test custom pizza construction without director
    custom_pizza_builder = MargheritaPizzaBuilder() # Can reuse any builder
    custom_pizza_builder.reset()
    custom_pizza_builder.build_dough()
    custom_pizza_builder.build_sauce()
    custom_pizza_builder.product.add("extra cheese")
    custom_pizza_builder.product.add("olives")
    custom_pizza = custom_pizza_builder.get_product()
    expected_custom = "Pizza parts: thin crust dough, tomato sauce, extra cheese, olives"
    assert custom_pizza.list_parts() == expected_custom, f"Custom Pizza Test Failed: {custom_pizza.list_parts()}"
    print(f"Custom Pizza Test Passed: {custom_pizza.list_parts()}")

    print("All Builder Pattern Pizza Tests Passed!")

if __name__ == "__main__":
    run_tests()
