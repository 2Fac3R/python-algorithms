class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleNode(object):
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous
