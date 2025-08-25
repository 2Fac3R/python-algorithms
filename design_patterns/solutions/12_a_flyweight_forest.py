from typing import Dict

"""
Solution for: Forest Rendering with Flyweight
"""

# Flyweight: TreeType (Intrinsic State)
class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas: str, x: int, y: int) -> str:
        # Extrinsic state (x, y) is passed by the client
        return f"Drawing {self.color} {self.name} tree with {self.texture} texture at ({x},{y}) on {canvas}"

# Flyweight Factory
class TreeFactory:
    _tree_types: Dict[str, TreeType] = {}

    @staticmethod
    def get_tree_type(name: str, color: str, texture: str) -> TreeType:
        key = f"{name}_{color}_{texture}"
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(name, color, texture)
            print(f"Created new TreeType: {name} ({color}, {texture})")
        return TreeFactory._tree_types[key]

# Context: Tree (Extrinsic State)
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type # Reference to a Flyweight object

    def draw(self, canvas: str) -> str:
        return self.tree_type.draw(canvas, self.x, self.y)

# Client: Forest
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas: str):
        print(f"\nDrawing forest on {canvas}:")
        for tree in self.trees:
            print(tree.draw(canvas))
