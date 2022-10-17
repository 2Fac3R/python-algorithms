"""
Write a function that receives a phrase and returns a dictionary with the words it contains and its length.
"""


def convert_phrase_into_dict(phrase: str) -> dict:
    """Split a string into a dict {word: len}"""
    my_dict: dict = {}
    split: list = phrase.split()

    # for word in split:
    #     my_dict[word] = len(word)
    my_dict = {word: len(word) for word in split}

    return my_dict


if __name__ == '__main__':
    phrase: str = "Testing my function function"

    print(convert_phrase_into_dict(phrase))
