
from abc import ABC, abstractmethod

"""
Solution for: Beverage Preparation with Template Method
"""

# Abstract Class
class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        # This is the template method
        print("\n--- Preparing Beverage ---")
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
        print("--- Beverage Ready! ---")

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Concrete Class: Coffee
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

# Concrete Class: Tea
class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea bag")

    def add_condiments(self):
        print("Adding lemon")

