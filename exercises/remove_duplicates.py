def remove_duplicates(lista: list = []) -> list:
    return list(set(lista))

if __name__ == '__main__':
    lista: list = [1, 3, 6, 2, 1, 2, 8, 0]
    print(lista)
    print(remove_duplicates(lista))