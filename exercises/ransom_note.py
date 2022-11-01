def can_construct(ransom_note: str, magazine: str) -> bool:
    """Ransom Note

    Each letter in magazine can only be used once in ransom_note.

    Args:
        ransom_note (str): a str to be constructed by magazine
        magazine (str): a str to construct ransom_note

    Returns:
        bool: True if ransom_note can be constructed by using the letters from magazine,
                or False otherwise.

    Tests:
        >>> can_construct("a", "b")
        False
        >>> can_construct("aa", "ab")
        False
        >>> can_construct("aa", "aab")
        True
        >>> can_construct("aa", "aba")
        True
    """
    for i in set(ransom_note):
        if magazine.count(i) < ransom_note.count(i):
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
