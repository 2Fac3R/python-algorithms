# List is a collection which is ordered and changeable. Allows duplicate members. []
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
# Set is a collection which is unordered and unindexed. No duplicate members. {}
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

myList = ['item 1', 'item 2', 'item 3']
myTuple = ('item 1' 'item 2')
mySet = {'item 1', 'item 2'}
thisdict = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }
}

myList.append('new item')
myList.insert(2, 'inserted item')

mySet.add('item 0')

print(myList)

myList.remove('inserted item')
myList.pop(-1)

print(myList)
print(myTuple)
print(mySet)