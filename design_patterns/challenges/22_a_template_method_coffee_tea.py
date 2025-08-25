from abc import ABC, abstractmethod

"""
Challenge: Beverage Preparation with Template Method

Design a system for preparing different types of beverages (e.g., Coffee, Tea).
Both beverages follow a similar preparation algorithm, but some steps differ.

Your task is to:
1.  Define an abstract `CaffeineBeverage` class (Abstract Class) with:
    -   A concrete `prepare_recipe()` method (the template method) that defines the overall algorithm:
        -   `boil_water()` (concrete method)
        -   `brew()` (abstract method)
        -   `pour_in_cup()` (concrete method)
        -   `add_condiments()` (abstract method)
    -   Concrete implementations for `boil_water()` and `pour_in_cup()`.
2.  Implement concrete beverage classes:
    -   `Coffee`: Implements `brew()` (e.g., "Dripping coffee through filter") and `add_condiments()` (e.g., "Adding sugar and milk").
    -   `Tea`: Implements `brew()` (e.g., "Steeping the tea bag") and `add_condiments()` (e.g., "Adding lemon").

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
        # TODO: Implement brew for Coffee
        pass

    def add_condiments(self):
        # TODO: Implement add_condiments for Coffee
        pass

# Concrete Class: Tea
class Tea(CaffeineBeverage):
    def brew(self):
        # TODO: Implement brew for Tea
        pass

    def add_condiments(self):
        # TODO: Implement add_condiments for Tea
        pass


# --- Tests ---
def run_tests():
    print("Running Template Method Pattern Beverage Tests...")

    # Test Coffee preparation
    print("\nTesting Coffee:")
    coffee_maker = Coffee()
    # Capture print output for testing
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        coffee_maker.prepare_recipe()
    output = f.getvalue()
    expected_output_coffee = (
        "\n--- Preparing Beverage ---\\n"
        "Boiling water\\n"
        "Dripping coffee through filter\\n"
        "Pouring into cup\\n"
        "Adding sugar and milk\\n"
        "--- Beverage Ready! ---\\n"
    )
    assert output == expected_output_coffee, f"Coffee preparation failed.\nExpected:\n{expected_output_coffee}\nGot:\n{output}"
    print("Coffee preparation test passed.")

    # Test Tea preparation
    print("\nTesting Tea:")
    tea_maker = Tea()
    f = io.StringIO()
    with redirect_stdout(f):
        tea_maker.prepare_recipe()
    output = f.getvalue()
    expected_output_tea = (
        "\n--- Preparing Beverage ---\\n"
        "Boiling water\\n"
        "Steeping the tea bag\\n"
        "Pouring into cup\\n"
        "Adding lemon\\n"
        "--- Beverage Ready! ---\\n"
    )
    assert output == expected_output_tea, f"Tea preparation failed.\nExpected:\n{expected_output_tea}\nGot:\n{output}"
    print("Tea preparation test passed.")

    print("All Template Method Pattern Beverage Tests Passed!")

if __name__ == "__main__":
    run_tests()
