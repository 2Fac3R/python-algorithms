from utils.execution_time import execution_time


@execution_time
def busqueda_lineal(lista: list, objetivo: int) -> bool:
    for elemento in lista:  # O(n)
        if elemento == objetivo:
            return True
    return False


if __name__ == '__main__':
    import random

    tamano_de_lista: int = int(input('De que tamano sera la lista? '))
    objetivo: int = int(input('Que numero quieres encontrar? '))

    lista: list = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado: bool = busqueda_lineal(lista, objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
