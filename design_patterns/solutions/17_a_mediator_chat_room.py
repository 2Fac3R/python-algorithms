
from abc import ABC, abstractmethod
from typing import List

"""
Solution for: Chat Room with Mediator Pattern
"""

# Mediator Interface
class ChatRoomMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: 'User'):
        pass

# Colleague Abstract Class
class User(ABC):
    def __init__(self, name: str, mediator: ChatRoomMediator = None):
        self.name = name
        self._mediator = mediator

    def set_mediator(self, mediator: ChatRoomMediator):
        self._mediator = mediator

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str):
        pass

# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self._users: List[User] = []

    def add_user(self, user: User):
        self._users.append(user)
        user.set_mediator(self)

    def send_message(self, message: str, sender: User):
        print(f"[ChatRoom] Message from {sender.name}: {message}")
        for user in self._users:
            if user != sender:
                user.receive(f"[{sender.name}] {message}")

# Concrete Colleagues
class ChatUser(User):
    def __init__(self, name: str, mediator: ChatRoomMediator = None):
        super().__init__(name, mediator)

    def send(self, message: str):
        if self._mediator:
            self._mediator.send_message(message, self)
        else:
            print(f"Error: {self.name} is not connected to a chat room.")

    def receive(self, message: str):
        print(f"[{self.name}] received: {message}")
