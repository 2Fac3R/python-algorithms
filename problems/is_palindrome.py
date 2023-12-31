def is_palindrome(s: str) -> bool:
    """Is Palindrome

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.

    Alphanumeric characters include letters and numbers.

    Args:
        s (str): a text

    Returns:
        bool: True if it is palindrome, or False otherwise

    Tests:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome(" ")
        True
    """
    # text = ''.join(filter(str.isalnum, s)).lower()
    text: list[str] = [c for c in s.lower() if c.isalnum()]
    return text == text[::-1]


if __name__ == '__main__':
    from doctest import testmod
    testmod()
