numbers = [i for i in range(1, 11)]  # [x for x in iter]
numbers_squared = dict({i: i**2 for i in numbers})  # {x: expr for x in iter}
numbers_cube = [i**3 for i in numbers]  # [expr for x in iter]
numbers_cube2 = dict({number: cube for (number, cube)  # dict({x:y for (x, y) in zip(iter1, iter2)})
                     in zip(numbers, numbers_cube)})
odd_numbers = [i*2 for i in numbers if i %
               2 == 0]  # [expr for x in iter if expr]

print(numbers)
print(numbers_squared)
print(numbers_cube)
print(numbers_cube2)
# print(dict(zip(numbers, numbers_cube)))
print(odd_numbers)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [
    (color, size)
    for color in colors
    for size in sizes
]
print(tshirts)

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    # Using a generator expression would save the cost of building a list
    print(tshirt)

symbols = '$¢£¥€¤'
ords = tuple(ord(symbol) for symbol in symbols)
print(ords)
