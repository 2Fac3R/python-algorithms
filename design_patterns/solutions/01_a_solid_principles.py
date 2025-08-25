
# Solución: Principios SOLID

"""
Solución para: Principios SOLID
"""

from abc import ABC, abstractmethod

# 1. SRP (Single Responsibility Principle)
# Clases refactorizadas para cumplir SRP
class GestorDeTareasSRP:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        return f"Tarea '{tarea}' agregada."

class PersistenciaDeTareas:
    def guardar_tareas(self, tareas, archivo):
        # Lógica para guardar tareas en un archivo
        return f"Tareas guardadas en {archivo}."

class NotificadorDeTareas:
    def enviar_notificacion_tarea(self, tarea):
        # Lógica para enviar una notificación
        return f"Notificación enviada para la tarea '{tarea}'."


# 2. OCP (Open/Closed Principle)
# Refactorizado para cumplir OCP
class ProductoOCP(ABC):
    @abstractmethod
    def get_precio(self):
        pass

    @abstractmethod
    def get_descuento(self):
        pass

class ProductoEstandarOCP(ProductoOCP):
    def __init__(self, precio):
        self.precio = precio

    def get_precio(self):
        return self.precio

    def get_descuento(self):
        return self.precio * 0.10

class ProductoPremiumOCP(ProductoOCP):
    def __init__(self, precio):
        self.precio = precio

    def get_precio(self):
        return self.precio

    def get_descuento(self):
        return self.precio * 0.20

def calcular_descuento_total_ocp(productos):
    total_descuento = 0
    for p in productos:
        total_descuento += p.get_descuento()
    return total_descuento


# 3. LSP (Liskov Substitution Principle)
# Jerarquía corregida para cumplir LSP
class AveLSP(ABC):
    @abstractmethod
    def comer(self):
        pass

class AveVoladoraLSP(AveLSP):
    def comer(self):
        return "Comiendo como ave voladora"

    def volar(self):
        return "Volando"

class PinguinoLSP(AveLSP):
    def comer(self):
        return "Comiendo como pingüino"

    def nadar(self):
        return "Nadando"


# 4. ISP (Interface Segregation Principle)
# Interfaces refactorizadas para cumplir ISP
class TrabajadorISP(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class ComedorISP(ABC):
    @abstractmethod
    def comer(self):
        pass

class DormilonISP(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(TrabajadorISP, ComedorISP, DormilonISP):
    def trabajar(self):
        return "Humano trabajando"
    def comer(self):
        return "Humano comiendo"
    def dormir(self):
        return "Humano durmiendo"

class Robot(TrabajadorISP):
    def trabajar(self):
        return "Robot trabajando"


# 5. DIP (Dependency Inversion Principle)
# Refactorizado para cumplir DIP
class MensajeroDIP(ABC): # Abstracción
    @abstractmethod
    def enviar(self, mensaje):
        pass

class MensajeroEmailDIP(MensajeroDIP): # Detalle
    def enviar(self, mensaje):
        return f"Email enviado: {mensaje}"

class MensajeroSMSDIP(MensajeroDIP): # Otro detalle
    def enviar(self, mensaje):
        return f"SMS enviado: {mensaje}"

class ServicioDeNotificacionDIP: # Módulo de alto nivel
    def __init__(self, mensajero: MensajeroDIP): # Depende de la abstracción
        self.mensajero = mensajero

    def notificar(self, mensaje):
        return self.mensajero.enviar(mensaje)
