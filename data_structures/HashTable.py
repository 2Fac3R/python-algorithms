from typing import Any


BLANK = object()


class HashTable:
    """Represents a Hash Table."""

    def __init__(self, capacity: int):
        """
        Args:
            capacity (int): static size of the hash table.
        """
        self.values = capacity * [BLANK]

    def __len__(self) -> int:
        """
        Returns the length of the Hash Table.
        >>> hashmap = HashTable(5)
        >>> len(hashmap)
        5
        """
        return len(self.values)

    def __hash__(self, key) -> int:
        """
        Returns the hash function.
        Hash mapping function: hash(key) % len(self)
        """
        return hash(key) % len(self)

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
        >>> hashed_key = hashmap.__hash__(key)
        >>> hashmap[hashed_key] = value
        >>> hashmap.__getitem__(hashed_key)
        'test'
        >>> hashmap[hashed_key]
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
        >>> key = 'hello'
        >>> hashed_key = hashmap.__hash__(key)
        >>> hashmap[hashed_key] = 'world'
        >>> hashmap.__contains__(hashed_key)
        True
        >>> hashed_key in hashmap
        True
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
        >>> hashed_key = hashmap.__hash__(key)
        >>> hashmap[hashed_key] = value
        >>> hashmap.get(hashed_key)
        'test'
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
        >>> hashed_key = hashmap.__hash__(key)
        >>> hashmap[hashed_key] = value
        >>> hashmap.get(hashed_key)
        'test'
        >>> hashmap.__delitem__(hashed_key)
        >>> hashmap.get(hashed_key)
        >>> hashmap.__delitem__('aaaa')
        Traceback (most recent call last):
        ...
        KeyError: 'aaaa'
        >>> del hashmap['bbbb']
        Traceback (most recent call last):
        ...
        KeyError: 'bbbb'
        """
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
