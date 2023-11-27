def is_parentheses_valid(s: str) -> bool:
    """Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

    Args:
        s (str): A string containing parentheses bracket characters.

    Returns:
        bool: True if the input string is valid, False otherwise.

    Tests:
        >>> is_parentheses_valid("()")
        True
        >>> is_parentheses_valid("()[]{}")
        True
        >>> is_parentheses_valid("(]")
        False
        >>> is_parentheses_valid("([])")
        True
    """
    # Create a dictionary to map open brackets to their corresponding close brackets.
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    # Create a stack to store the open brackets.
    stack = []

    # Iterate over the characters in the string.
    for char in s:
        # If the character is an open bracket, push it onto the stack.
        if char in brackets:
            stack.append(char)

        # If the character is a close bracket, check if the stack is empty or if the
        # top element of the stack is not the corresponding open bracket. If either of
        # these conditions is true, the string is not valid.
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    # If the stack is not empty, the string is not valid.
    return len(stack) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
