
from abc import ABC, abstractmethod
from typing import List

"""
Challenge: Chat Room with Mediator Pattern

Design a simple chat room application where users can send messages to each other.
Instead of users communicating directly, they should communicate through a central chat room (Mediator).

Your task is to:
1.  Define an abstract `ChatRoomMediator` class (Mediator interface) with an abstract `send_message(message: str, user: 'User')` method.
2.  Define an abstract `User` class (Colleague abstract class) with:
    -   An `__init__` method that takes a `name` and an optional `mediator`.
    -   A `set_mediator(mediator: ChatRoomMediator)` method.
    -   Abstract `send(message: str)` and `receive(message: str)` methods.
3.  Implement a `ChatRoom` class (Concrete Mediator) that implements `ChatRoomMediator`.
    -   It should maintain a list of registered users.
    -   Its `add_user(user: User)` method should register a user and set its mediator.
    -   Its `send_message(message: str, sender: User)` method should forward the message to all other users in the chat room.
4.  Implement a `ChatUser` class (Concrete Colleague) that inherits from `User`.
    -   Its `send()` method should use the mediator to send a message.
    -   Its `receive()` method should print the received message.

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
        # TODO: Implement message forwarding logic
        pass

# Concrete Colleagues
class ChatUser(User):
    def __init__(self, name: str, mediator: ChatRoomMediator = None):
        super().__init__(name, mediator)

    def send(self, message: str):
        # TODO: Implement send using the mediator
        pass

    def receive(self, message: str):
        # TODO: Implement receive
        pass


# --- Tests ---
def run_tests():
    print("Running Mediator Pattern Chat Room Tests...")

    chat_room = ChatRoom()

    john = ChatUser("John")
    jane = ChatUser("Jane")
    mike = ChatUser("Mike")

    chat_room.add_user(john)
    chat_room.add_user(jane)
    chat_room.add_user(mike)

    # Capture print output for testing
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        john.send("Hi everyone!")
    output = f.getvalue()
    assert "[ChatRoom] Message from John: Hi everyone!" in output
    assert "[Jane] received: [John] Hi everyone!" in output
    assert "[Mike] received: [John] Hi everyone!" in output
    assert "[John] received:" not in output # Sender should not receive their own message
    print("Test: John sends message passed.")

    f = io.StringIO()
    with redirect_stdout(f):
        jane.send("Hello John!")
    output = f.getvalue()
    assert "[ChatRoom] Message from Jane: Hello John!" in output
    assert "[John] received: [Jane] Hello John!" in output
    assert "[Mike] received: [Jane] Hello John!" in output
    print("Test: Jane sends message passed.")

    f = io.StringIO()
    with redirect_stdout(f):
        mike.send("What's up?")
    output = f.getvalue()
    assert "[ChatRoom] Message from Mike: What's up?" in output
    assert "[John] received: [Mike] What's up?" in output
    assert "[Jane] received: [Mike] What's up?" in output
    print("Test: Mike sends message passed.")

    print("\nAll Mediator Pattern Chat Room Tests Passed!")

if __name__ == "__main__":
    run_tests()
