# List is a collection which is ordered and changeable. Allows duplicate members. []
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
# Set is a collection which is unordered and unindexed. No duplicate members. {}
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

myList = ['item 1', 'item 2', 'item 3']
myTuple = ('item 1' 'item 2')
mySet = {'item 1', 'item 2'}
mySet2 = {'item 0', 'item 1', 'item 2', 'item 4'}
thisdict = {
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
myList.append('new item')
myList.insert(2, 'inserted item')
myList.remove('inserted item')
print(myList)
myList.pop(-1)

# Set
mySet.add('item 0')
mySet.update({'item 1', 'item 4'})


# OPERATIONS
# Union
items_union = mySet | mySet2  # items_union = mySet.union(myList)
# Intersection
items_intersection = mySet & mySet2  # mySet.intersection(mySet2)
# Difference
items_diff = mySet - mySet2  # mySet.difference(mySet2)
# Symmetric difference
items_sym_diff = mySet ^ mySet2  # mySet.symmetric_difference(mySet2)

print(myList)
print(myTuple)
print(mySet)
print(items_union)
print(items_intersection)
print(items_diff)
print(items_sym_diff)

# Traversing a dict
for key, value in thisdict.items():
    print(f"{key}:{value}")
