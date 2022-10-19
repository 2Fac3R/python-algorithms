numbers = [i for i in range(1, 11)]
numbers_squared = dict({i: i**2 for i in numbers})
numbers_cube = [i**3 for i in numbers]
numbers_cube2 = dict({number: cube for (number, cube)
                     in zip(numbers, numbers_cube)})
odd_numbers = [i*2 for i in numbers if i % 2 == 0]

print(numbers)
print(numbers_squared)
print(numbers_cube)
print(numbers_cube2)
# print(dict(zip(numbers, numbers_cube)))
print(odd_numbers)
