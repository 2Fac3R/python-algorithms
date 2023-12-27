"""
    Tuples are not just immutable lists
"""
from collections import namedtuple

# typing
City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])

# Tuples as records

# Latitude and longitude of the Los Angeles International Airport.
lax_coordinates: Coordinate = Coordinate(33.9425, -118.408056)
# Tokyo: name, year, population (thousands), population change (%), and area (km²).
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
# (country_code, passport_number)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)


# Unpacking
latitude, longitude = lax_coordinates
print(latitude, longitude)

# Using * to grab excess items
first, second, *body, last = range(10)
print(first, second, body, last)

# Unpacking nested tuples
metro_areas: list[City] = [
    City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    City('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    City('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    City('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    City('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print(f'{"city":15} | {"latitude":>9} | {"longitude":>9}')
for name, _, _, (lat, lon) in metro_areas:
    if lon <= 0:
        """Selects only cities in the Western hemisphere."""
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
