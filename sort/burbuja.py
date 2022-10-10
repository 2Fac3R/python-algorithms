def ordenamiento_de_burbuja(lista: list) -> list:
    n: int = len(lista)

    for i in range(n):
        print(lista)
        for j in range(0, n - i - 1):  # O(n) * O(n) = O(n * n) = O(n**2)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == '__main__':
    import random
    
    tamano_de_lista: int = int(input('De que tamano sera la lista? '))

    lista: list = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada: list = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
