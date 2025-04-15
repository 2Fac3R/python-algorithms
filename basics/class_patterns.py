# Book: Fluent Python. Example 5-22. City class and a few instances
from typing import NamedTuple, List


class City(NamedTuple):
    continent: str
    name: str
    country: str


def match_asian_cities(cities: List[City]) -> List[City]:
    """Match Asian Cities

    Args:
        cities (List[City]): list of cities

    Returns:
        List[City]: list of asian cities

    Tests:
        >>> city1 = City('Asia', 'Tokyo', 'JP')
        >>> city2 = City('North America', 'Mexico City', 'MX')
        >>> city3 = City('Asia', 'Beijing', 'CN')
        >>> city4 = City('North America', 'Los Angeles', 'US')
        >>> cities = [city1, city2, city3, city4]
        >>> match_asian_cities(cities)
        [City(continent='Asia', name='Tokyo', country='JP'), City(continent='Asia', name='Beijing', country='CN')]
    """
    results: List[City] = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results


if __name__ == '__main__':
    from doctest import testmod
    testmod()
