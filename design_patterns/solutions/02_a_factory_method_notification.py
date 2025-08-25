
from typing import List
from abc import ABC, abstractmethod

"""
Solution for: Notification System with Factory Method
"""

# 1. Product Interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# 2. Concrete Products
class EmailNotification(Notification):
    def send(self, message: str):
        return f"Email sent: {message}"

class SMSNotification(Notification):
    def send(self, message: str):
        return f"SMS sent: {message}"

# 3. Creator Interface
class NotificationCreator(ABC):
    @abstractmethod
    def factory_method(self) -> Notification:
        pass

    def deliver_notification(self, message: str) -> str:
        # This core logic uses the factory method to get a product
        # and then works with the product interface.
        notification = self.factory_method()
        return notification.send(message)

# 4. Concrete Creators
class EmailNotificationCreator(NotificationCreator):
    def factory_method(self) -> Notification:
        return EmailNotification()

class SMSNotificationCreator(NotificationCreator):
    def factory_method(self) -> Notification:
        return SMSNotification()
