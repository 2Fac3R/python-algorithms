# List is a collection which is ordered and changeable. Allows duplicate members. []
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
# Set is a collection which is unordered and unindexed. No duplicate members. {}
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. {}

my_list = ['item 1', 'item 2', 'item 3']
my_tuple = ('item 1' 'item 2')
my_set = {'item 1', 'item 2'}
my_set2 = {'item 0', 'item 1', 'item 2', 'item 4'}
my_dict = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    }
}

# List
my_list.append('new item')
my_list.insert(2, 'inserted item')
my_list.remove('inserted item')
print(my_list)
my_list.pop(-1)

# Set
my_set.add('item 0')
my_set.update({'item 1', 'item 4'})


# OPERATIONS
# Union
items_union = my_set | my_set2  # items_union = my_set.union(my_list)
# Intersection
items_intersection = my_set & my_set2  # my_set.intersection(my_set2)
# Difference
items_diff = my_set - my_set2  # my_set.difference(my_set2)
# Symmetric difference
items_sym_diff = my_set ^ my_set2  # my_set.symmetric_difference(my_set2)

print(my_list)
print(my_tuple)
print(my_set)
print(items_union)
print(items_intersection)
print(items_diff)
print(items_sym_diff)

# Traversing a dict
for key, value in my_dict.items():
    print(f"{key}\n\tName: {value['name']}\n\tYear: {value['year']}")
