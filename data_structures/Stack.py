from Node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """Appends an element on top."""
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        """Removes and returns the element on top."""
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return "The stack is empty"

    def peek(self):
        """Returns top node data."""
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        """Clears the stack."""
        while self.top:
            self.pop()


if __name__ == '__main__':
    myStack = Stack()

    myStack.push("item")
    myStack.push("item 2")
    myStack.push("item 3")
    myStack.push("item 4")
    myStack.pop()

    print(myStack.peek())

    for item in myStack:
        print(item)
