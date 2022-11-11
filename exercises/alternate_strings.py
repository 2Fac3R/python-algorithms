def alternate_strings(first_str: str, second_str: str) -> str:
    """
    Args:
        first_str (str): first string
        second_str (str): second string

    Returns:
        str: return the alternative arrangements of the two strings.

    Tests:
        >>> alternate_strings("ABCD", "XY")
        'AXBYCD'
        >>> alternate_strings("XY", "ABCD")
        'XAYBCD'
        >>> alternate_strings("AB", "XYZ")
        'AXBYZ'
        >>> alternate_strings("ABC", "")
        'ABC'
    """
    first_str_length: int = len(first_str)
    second_str_length: int = len(second_str)
    longer_length: int = (
        first_str_length if first_str_length > second_str_length else second_str_length
    )
    output_list: list = []
    for index in range(longer_length):
        if index < first_str_length:
            output_list.append(first_str[index])
        if index < second_str_length:
            output_list.append(second_str[index])
    return "".join(output_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(alternate_strings("AB", "XYZ"))
