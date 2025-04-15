from dataclass import dataclass

# Dataclass is a decorator that automatically generates special methods for classes
# such as __init__, __repr__, __eq__, and __hash__ based on class attributes.


@dataclass(frozen=True) # frozen=True makes the class immutable
class Coordinate:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}"{ns}, {abs(self.lon):.1f}"{we}'
