from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """Longest Common Prefix

    Args:
        strs (List[str]): A list of strings

    Returns:
        str: A string representing the longest common prefix, 
                or an empty string if there is no common prefix.

    Tests
        >>> longest_common_prefix([])
        ''
        >>> longest_common_prefix(["dog","racecar","car"])
        ''
        >>> longest_common_prefix(["dog","Dog","doggy"])
        ''
        >>> longest_common_prefix(["flower","flow","flight"])
        'fl'
    """
    # If the list of strings is empty, return an empty string.
    if not strs:
        return ""

    # Initialize the longest common prefix to the first string in the list.
    longest_common_prefix = strs[0]

    # Iterate over the remaining strings in the list.
    for string in strs[1:]:
        # Find the longest common prefix between the current string and the longest
        # common prefix found so far.
        new_longest_common_prefix = ""
        for i in range(len(longest_common_prefix)):
            if i >= len(string) or longest_common_prefix[i] != string[i]:
                break
            new_longest_common_prefix += longest_common_prefix[i]

        # Update the longest common prefix.
        longest_common_prefix = new_longest_common_prefix

    # Return the longest common prefix.
    return longest_common_prefix


if __name__ == '__main__':
    import doctest
    doctest.testmod()
