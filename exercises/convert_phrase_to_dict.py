from typing import Dict


def convert_phrase_to_dict(phrase: str) -> Dict[str, int]:
    """Convert a phrase to a dict

    Args:
        phrase (str): a text phrase to convert

    Returns:
        Dict[str, int]: a dict {word: len}

    Tests:
        >>> convert_phrase_to_dict("My test")
        {'My': 2, 'test': 4}
        >>> convert_phrase_to_dict("test running my test")
        {'test': 4, 'running': 7, 'my': 2}
        >>> convert_phrase_to_dict("What do you do?")
        {'What': 4, 'do': 2, 'you': 3, 'do?': 3}
    """
    split: list = phrase.split()
    my_dict: Dict[str, int] = {word: len(word) for word in split}

    return my_dict


if __name__ == '__main__':
    import doctest
    doctest.testmod()
