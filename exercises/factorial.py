def factorial(n: int) -> int:
    if n <= 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n: int = 5
    print(factorial(n))
