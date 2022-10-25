def roman_to_int(s: str) -> int:
    """
    Given a roman numeral, convert it to an integer.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

    >>> roman_to_int("III")
    3
    >>> roman_to_int("LVIII")
    58
    >>> roman_to_int("MCMXCIV")
    1994
    """
    roman_to_integer = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    s = s.replace('IV', 'IIII') \
         .replace('IX', 'VIIII') \
         .replace('XL', 'XXXX') \
         .replace('XC', 'LXXXX') \
         .replace('CD', 'CCCC') \
         .replace('CM', 'DCCCC')

    return sum(map(roman_to_integer.get, s))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(roman_to_int('MCMXCIV'))
