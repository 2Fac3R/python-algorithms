
"""
Solution for: Valid Parentheses
"""

def is_valid(s: str) -> bool:
    """
    This solution uses a stack (implemented with a Python list) and a hash map.

    1. We create a hash map `bracket_map` that maps each closing bracket to its
       corresponding opening bracket. This makes lookups easy.
    2. We initialize an empty list `stack`.
    3. We iterate through each character in the input string `s`.
       - If the character is an opening bracket (i.e., it's a value in our map),
         we push it onto the stack.
       - If the character is a closing bracket (i.e., it's a key in our map):
         - We first check if the stack is empty. If it is, there's no opening
           bracket to match with, so the string is invalid.
         - If the stack is not empty, we `pop` the top element and check if it
           matches the expected opening bracket from our map. If it doesn't
           match, the string is invalid.
       - If the character is not a bracket, we ignore it (though the problem
         statement says it only contains brackets).
    4. After the loop finishes, the string is valid only if the stack is empty.
       If there are any opening brackets left on the stack, it means they were
       never closed.
    """
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map.values(): # It's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys(): # It's a closing bracket
            if not stack or bracket_map[char] != stack.pop():
                return False
        else:
            # Character is not a bracket, invalid
            return False

    # The string is valid if and only if the stack is empty at the end
    return not stack
