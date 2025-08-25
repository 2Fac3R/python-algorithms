
# Solutions: UML Class Diagram Interpretation

"""
Solution for: UML Class Diagram Interpretation
"""

# --- Answers to Challenge Questions ---

# 1. Interpret Relationships:
#    - Vehicle <|-- Car: Inheritance (Generalization). A `Car` is a `Vehicle`.
#    - Car o-- Engine: Aggregation. A `Car` has an `Engine`, but the `Engine` can exist independently of the `Car`.
#    - Engine *-- Piston: Composition. An `Engine` is composed of `Piston`s. A `Piston` cannot exist independently of its `Engine`.
#    - Driver -- Car: Association. A `Driver` is associated with a `Car`. This is a general relationship, often implying usage or interaction.
#    - Car --..> FuelPump: Dependency. A `Car` depends on a `FuelPump` (e.g., a method in `Car` might take a `FuelPump` as a parameter). This is a weaker, often temporary, relationship.

# 2. Conceptual Design:
#    - Customer and Order: Association. A `Customer` places `Orders`. An order is associated with a customer, and a customer can have multiple orders. (Multiplicity: Customer 1 -- * Order)
#    - Order and Product: Association (or Composition/Aggregation depending on specifics). An `Order` contains `Products`. If the `Product` items are specific to that order (e.g., a custom configuration), it might be composition. If they are references to general catalog products, it's aggregation or a simple association. Often modeled as an `OrderLineItem` class that composes a `Product` and is composed by an `Order`.
#    - ShoppingCart and Product: Aggregation. A `ShoppingCart` contains `Products`. Products can exist independently of the shopping cart.
#    - ShoppingCart and Customer: Association. A `ShoppingCart` is associated with a `Customer`. A customer can have one shopping cart.

