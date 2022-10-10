def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


if __name__ == '__main__':
    my_string: str = 'Anita lava la tina'
    print(is_palindrome(my_string))
