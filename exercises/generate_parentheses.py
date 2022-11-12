from typing import List


def generate_parentheses(n: int) -> List[str]:
    """Generate Parentheses

    Args:
        n (int): n pairs of parentheses

    Returns:
        List[str]: all combinations of well-formed parentheses

    Tests:
        >>> generate_parentheses(-1)
        ['']
        >>> generate_parentheses(0)
        ['']
        >>> generate_parentheses(1)
        ['()']
        >>> generate_parentheses(3)
        ['()()()', '()(())', '(())()', '(()())', '((()))']
    """
    output: List[str] = []

    if n <= 0:
        return ['']

    for c in range(n):
        for left in generate_parentheses(c):
            for right in generate_parentheses(n-1-c):
                output.append(f"({left}){right}")

    return output


if __name__ == '__main__':
    from doctest import testmod
    testmod()
