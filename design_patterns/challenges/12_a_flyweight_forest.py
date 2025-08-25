
from typing import Dict

"""
Challenge: Forest Rendering with Flyweight

Design a system to render a large forest with many trees, optimizing memory usage
by sharing common tree properties (Flyweights).

Your task is to:
1.  Define a `TreeType` class (Flyweight) that stores the intrinsic (shared) state of a tree:
    -   `name` (e.g., "Oak", "Pine")
    -   `color` (e.g., "Green", "Dark Green")
    -   `texture` (e.g., "Rough Bark", "Needle Texture")
    -   It should have a `draw(canvas: str, x: int, y: int)` method that uses its intrinsic state and the passed extrinsic state (`x`, `y`).
2.  Define a `TreeFactory` class (Flyweight Factory) that manages and reuses `TreeType` objects:
    -   It should have a static method `get_tree_type(name: str, color: str, texture: str)`.
    -   This method should return an existing `TreeType` if one with the same properties already exists, otherwise, it creates a new one and stores it.
3.  Define a `Tree` class (Context) that stores the extrinsic (unique) state of a tree:
    -   `x` (coordinate)
    -   `y` (coordinate)
    -   A reference to a `TreeType` object (the Flyweight).
    -   It should have a `draw(canvas: str)` method that delegates to its `TreeType`'s `draw` method, passing its own `x` and `y`.
4.  Define a `Forest` class (Client) that manages a collection of `Tree` objects:
    -   It should have a `plant_tree(x: int, y: int, name: str, color: str, texture: str)` method that uses the `TreeFactory` to get a `TreeType` and then creates a `Tree` object.
    -   It should have a `draw(canvas: str)` method that iterates through its trees and calls their `draw` method.

"""

# Flyweight: TreeType (Intrinsic State)
class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas: str, x: int, y: int) -> str:
        # TODO: Implement draw method
        pass

# Flyweight Factory
class TreeFactory:
    _tree_types: Dict[str, TreeType] = {}

    @staticmethod
    def get_tree_type(name: str, color: str, texture: str) -> TreeType:
        key = f"{name}_{color}_{texture}"
        # TODO: Implement logic to return existing or create new TreeType
        pass

# Context: Tree (Extrinsic State)
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type # Reference to a Flyweight object

    def draw(self, canvas: str) -> str:
        # TODO: Implement draw method
        pass

# Client: Forest
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        # TODO: Implement plant_tree method using TreeFactory
        pass

    def draw(self, canvas: str):
        # TODO: Implement draw method for the forest
        pass


# --- Tests ---
def run_tests():
    print("Running Flyweight Pattern Forest Rendering Tests...")

    forest = Forest()

    # Plant many trees, observe TreeType creation
    forest.plant_tree(10, 20, "Oak", "Green", "Rough Bark")
    forest.plant_tree(20, 30, "Pine", "Dark Green", "Needle Texture")
    forest.plant_tree(15, 25, "Oak", "Green", "Rough Bark") # Should reuse existing Oak TreeType
    forest.plant_tree(30, 40, "Pine", "Dark Green", "Needle Texture") # Should reuse existing Pine TreeType
    forest.plant_tree(5, 10, "Maple", "Red", "Smooth Bark")

    # Draw the forest (output will be printed to console)
    forest.draw("Game Canvas")

    # Verify the number of unique tree types created
    assert len(TreeFactory._tree_types) == 3, f"Expected 3 unique tree types, got {len(TreeFactory._tree_types)}"
    print(f"Total unique tree types created: {len(TreeFactory._tree_types)}")

    # Verify specific tree drawing output
    # This requires inspecting the printed output, but we can check the first tree's output
    first_tree_output = forest.trees[0].draw("Test Canvas")
    assert first_tree_output == "Drawing Green Oak tree with Rough Bark texture at (10,20) on Test Canvas"
    print("Specific tree drawing output test passed.")

    print("All Flyweight Pattern Forest Rendering Tests Passed (visual inspection recommended for full output)!")

if __name__ == "__main__":
    run_tests()
