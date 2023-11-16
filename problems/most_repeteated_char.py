def most_repeated_character(s: str) -> str:
    """Most Repeated Character O(n)

    Given a string s, return the most frequent character (an alphabet letter) in a string s

    Args:
        s (str): a string 's'

    Returns:
        (str): the most frequent character in s

    Tests:
        >>> most_repeated_character('')
        ''
        >>> most_repeated_character('87@#$6;')
        ''
        >>> most_repeated_character('as765dfff')
        'f'
        >>> most_repeated_character('as76a5dfaffa')
        'a'
        >>> most_repeated_character('Sasss76S5dssfsffS')
        's'
    """
    # Check if s in empty
    if len(s) == 0:
        return ''

    chars: list = list(s)

    # Clear any non-alphabet letters in s
    non_alpha_letters: list = list(filter(lambda c: c.isalpha(), chars))
    # print(non_alpha_letters)

    # Check if the list of non-alphabet letters is empty
    if non_alpha_letters == []:
        return ''

    # Get unique letters
    unique: list = list(set(non_alpha_letters))
    # print(unique)

    # Store in a dict each letter with its number of ocurrencecs in non_alpha_letters
    counter: dict[str, int] = {
        char: non_alpha_letters.count(char) for char in unique}
    # print(counter)

    # Get the key with the higher value
    most_repeated_char = max(counter, key=counter.get)
    # print(most_repeated_char)

    return most_repeated_char


if __name__ == '__main__':
    import doctest
    doctest.testmod()
