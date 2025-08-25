
from typing import List
from abc import ABC, abstractmethod

"""
Challenge: Notification System with Factory Method

Design a notification system that can send different types of messages (e.g., Email, SMS).
The system should allow adding new notification types in the future without modifying the core sending logic.

Implement the Factory Method pattern to achieve this.

Your task is to:
1.  Define an abstract `Notification` class with an abstract `send` method.
2.  Implement concrete `EmailNotification` and `SMSNotification` classes that inherit from `Notification`.
3.  Define an abstract `NotificationCreator` class with an abstract `factory_method` that returns a `Notification` object.
4.  Implement concrete `EmailNotificationCreator` and `SMSNotificationCreator` classes that inherit from `NotificationCreator` and override `factory_method` to return their respective notification types.
5.  The `NotificationCreator` should also have a `deliver_notification` method that uses `factory_method` to send a message.

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
        # Implement this method to use the factory_method
        pass

# 4. Concrete Creators
class EmailNotificationCreator(NotificationCreator):
    def factory_method(self) -> Notification:
        return EmailNotification()

class SMSNotificationCreator(NotificationCreator):
    def factory_method(self) -> Notification:
        return SMSNotification()


# --- Tests ---
def run_tests():
    print("Running Factory Method Notification System Tests...")

    # Test Email Notification
    email_creator = EmailNotificationCreator()
    email_result = email_creator.deliver_notification("Hello from Email!")
    expected_email = "Email sent: Hello from Email!"
    print(f"Email Test: {'PASSED' if email_result == expected_email else 'FAILED'} (Got: {email_result})")

    # Test SMS Notification
    sms_creator = SMSNotificationCreator()
    sms_result = sms_creator.deliver_notification("Hello from SMS!")
    expected_sms = "SMS sent: Hello from SMS!"
    print(f"SMS Test: {'PASSED' if sms_result == expected_sms else 'FAILED'} (Got: {sms_result})")

    # Test adding a new type (conceptual check)
    try:
        class PushNotification(Notification):
            def send(self, message: str):
                return f"Push notification sent: {message}"

        class PushNotificationCreator(NotificationCreator):
            def factory_method(self) -> Notification:
                return PushNotification()
        
        push_creator = PushNotificationCreator()
        push_result = push_creator.deliver_notification("Hello from Push!")
        expected_push = "Push notification sent: Hello from Push!"
        print(f"Push Test (conceptual): {'PASSED' if push_result == expected_push else 'FAILED'} (Got: {push_result})")

    except Exception as e:
        print(f"Push Test (conceptual): FAILED due to exception: {e}")

if __name__ == "__main__":
    run_tests()
