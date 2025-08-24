
# Technique: Stacks (LIFO)

A **Stack** is a linear data structure that follows a particular order in which operations are performed. The order is **LIFO (Last-In, First-Out)**. Think of it like a stack of plates: you can only add a new plate to the top, and you can only remove the top plate.

In Python, you can easily implement a stack using the built-in `list` type. 

- **Push (Add an item):** `stack.append(item)`
- **Pop (Remove an item):** `stack.pop()`
- **Peek (Look at the top item):** `stack[-1]` (if the stack is not empty)

## Core Properties

- **LIFO Principle:** The last element added to the stack will be the first one to be removed.
- **Key Operations:**
    - `push`: Adds an element to the top of the stack.
    - `pop`: Removes and returns the top element of the stack.
    - `peek` or `top`: Returns the top element without removing it.
    - `isEmpty`: Checks if the stack is empty.

## Why are they useful in interviews?

Stacks are particularly useful for problems that involve parsing, reversing order, or handling nested structures. Any time you need to process items in a reversed order of their appearance, a stack should come to mind.

**Common Use Case: Matching Pairs or Nested Structures**

The most famous example is validating parentheses. When you encounter an opening bracket, you `push` it onto the stack. When you see a closing bracket, you `pop` from the stack and check if it's the matching opening bracket. 

- If you see `(`, you push `)` onto the stack.
- If you see `{`, you push `}` onto the stack.
- If you see `[`, you push `]` onto the stack.

When you encounter a closing bracket, you check if the stack is empty or if the top element doesn't match. If either is true, the string is invalid. After iterating through the whole string, the stack must be empty for the string to be valid.

**Code Example (Valid Parentheses):**
```python
stack = []
bracket_map = { ")": "(", "}": "{", "]": "[" }

for char in s:
    if char in bracket_map.values(): # Is an open bracket
        stack.append(char)
    elif char in bracket_map.keys(): # Is a close bracket
        if not stack or stack.pop() != bracket_map[char]:
            return False # Invalid
# Final check: stack must be empty
return not stack
```

**Other Common Applications:**
- **Function Call Stack:** Programming languages use a stack to manage function calls.
- **Undo/Redo functionality:** Stacks can store previous states.
- **Evaluating postfix/prefix expressions.**
- **Depth-First Search (DFS):** An iterative DFS implementation uses a stack to keep track of nodes to visit.
