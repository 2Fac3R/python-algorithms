from typing import Any


BLANK = object()


class HashTable:
    """Represents a Hash Table."""

    def __init__(self, capacity):
        self.values = capacity * [BLANK]

    def __len__(self) -> int:
        """
        Returns the length of the Hash Table.
        >>> hashmap = HashTable(5)
        >>> len(hashmap)
        5
        """
        return len(self.values)

    def __setitem__(self, key, value) -> None:
        """
        Inserts a hashed key with value.
        >>> hashmap = HashTable(5)
        >>> key = 'key_test'
        >>> value = 'test'
        >>> # hashmap.__setitem__(key, value)
        >>> hashmap[key] = value
        >>> hashmap[key]
        'test'
        """
        self.values[self.__hash__(key)] = value

    def __getitem__(self, key) -> Any:
        """
        Returns item from its key.
        >>> hashmap = HashTable(5)
        >>> key = 'key_test'
        >>> value = 'test'
        >>> hashmap[key] = value
        >>> # hashmap.__getitem__(key)
        >>> hashmap[key]
        'test'
        """
        value = self.values[self.__hash__(key)]
        if value is BLANK:
            raise KeyError(key)
        return value

    def __contains__(self, key) -> bool:
        """
        Returns bool if key is in the hashmap.
        >>> hashmap = HashTable(5)
        >>> hashmap['hello'] = 'world'
        >>> hashmap.__contains__('hello')
        True
        >>> hashmap.__contains__('non-existing')
        False
        """
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key) -> Any:
        """
        Returns the value for that key,
        or None if not found.
        >>> hashmap = HashTable(5)
        >>> key = 'key_test'
        >>> value = 'test'
        >>> hashmap[key] = value
        >>> hashmap.get(key)
        'test'
        >>> hashmap.get('non-existing')
        """
        try:
            return self[key]
        except KeyError:
            return None

    def __delitem__(self, key) -> None:
        """
        Deletes (rewrites to BLANK) item.
        >>> hashmap = HashTable(5)
        >>> key = 'key_test'
        >>> value = 'test'
        >>> hashmap[key] = value
        >>> hashmap.get(key)
        'test'
        >>> hashmap.__delitem__(key)
        >>> hashmap.get(key)
        >>> hashmap.get('non-existing')
        """
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    def __hash__(self, key) -> int:
        """
        Returns the hash function.
        Hash mapping function: hash(key) % len(self)
        """
        return hash(key) % len(self)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
