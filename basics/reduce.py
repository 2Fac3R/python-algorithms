from functools import reduce

items = [
    {
        'product': 'camisa',
        'price': 100,
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
sum = reduce(lambda x, y: x + y, prices)

print(sum)
