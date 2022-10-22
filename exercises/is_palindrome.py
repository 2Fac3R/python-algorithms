def is_palindrome(s: str) -> bool:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.

    Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome(" ")
    True
    """
    # s = [i for i in s.lower() if i.isalnum()]
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
