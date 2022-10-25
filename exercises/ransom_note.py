def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Ransom Note
    Given two strings ransomNote and magazine,
    return true if ransomNote can be constructed by using the letters from magazine
    and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    >>> canConstruct("a", "b")
    False
    >>> canConstruct("aa", "ab")
    False
    >>> canConstruct("aa", "aab")
    True
    >>> canConstruct("aa", "aba")
    True
    """
    for i in set(ransomNote):
        if magazine.count(i) < ransomNote.count(i):
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
