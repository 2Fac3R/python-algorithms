# Book: Fluent Python. Example 3-2. creator.py: get_creators()
def get_creators(record: dict) -> list:
    """Get creators

    Extracts names of creators from media records

    Args:
        record (dict): media records

    Raises:
        ValueError: any other mapping with 'type': 'book' is invalid
        ValueError: any other subject is invalid

    Returns:
        list: names of creators

    Tests:
        >>> b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Godel, Escher, Bach')
        >>> get_creators(b1)
        ['Douglas Hofstadter']
        >>> b2 = dict(api=2, authors='Martelli Ravenscroft Holden'.split(), type='book', title='Python in a Nutshell')
        >>> get_creators(b2)
        ['Martelli', 'Ravenscroft', 'Holden']
        >>> get_creators({'type': 'book', 'pages': 770})
        Traceback (most recent call last):
            ...
        ValueError: Invalid 'book' record: {'type': 'book', 'pages': 770}
        >>> get_creators('Spam, spam, spam')
        Traceback (most recent call last):
            ...
        ValueError: Invalid record: 'Spam, spam, spam'
    """
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')


if __name__ == '__main__':
    from doctest import testmod
    testmod()
