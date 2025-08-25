
from abc import ABC, abstractmethod

"""
Solution for: Conceptos Fundamentales de POO
"""

# 1. Clases y Objetos
# 2. Encapsulamiento
# 3. Herencia y 5. Abstracción
# 4. Polimorfismo

class Publicacion(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def obtener_tipo(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

class Libro(Publicacion):
    def __init__(self, titulo, autor, isbn, precio):
        super().__init__(titulo, autor)
        self._isbn = isbn  # Atributo protegido
        self.__precio = precio # Atributo privado

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self._isbn}, Precio: {self.__precio:.2f}"

    def get_isbn(self):
        return self._isbn

    def get_precio(self):
        return self.__precio

    def obtener_tipo(self):
        return "Libro"

class Revista(Publicacion):
    def __init__(self, titulo, autor, numero):
        super().__init__(titulo, autor)
        self.numero = numero

    def obtener_tipo(self):
        return "Revista"

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Número: {self.numero}"

def imprimir_tipo_publicacion(publicacion: Publicacion):
    return publicacion.obtener_tipo()
