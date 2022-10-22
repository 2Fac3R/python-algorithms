from functools import reduce
from functools import reduce

numbers = [1, 2, 3, 4]
sum = reduce(lambda counter, x: counter + x, numbers)