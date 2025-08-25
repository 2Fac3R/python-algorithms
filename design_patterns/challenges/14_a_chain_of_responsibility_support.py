
from abc import ABC, abstractmethod
from typing import Optional

"""
Challenge: Customer Support System with Chain of Responsibility

Design a customer support system where different types of requests are handled by different levels of support.
If a support level cannot handle a request, it passes it to the next level in the chain.

Your task is to:
1.  Define an abstract `SupportHandler` class (Handler interface) with:
    -   An abstract `set_next(handler: 'SupportHandler') -> 'SupportHandler'` method to set the next handler.
    -   An abstract `handle_request(request: str) -> Optional[str]` method to process or pass the request.
2.  Implement an `AbstractSupportHandler` (Base Handler) that provides a default implementation for `set_next`
    and a default `handle_request` that passes the request to the next handler if one exists.
3.  Implement concrete handlers:
    -   `Level1Support`: Handles "simple" or "basic" requests.
    -   `Level2Support`: Handles "technical" or "complex" requests.
    -   `TechnicalLead`: Handles "critical" or "urgent" requests.
    Each concrete handler should print a message if it cannot handle the request and passes it on.
4.  In the client code, set up a chain of responsibility and send various requests through it.

"""

# Handler Interface
class SupportHandler(ABC):
    @abstractmethod
    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        pass

    @abstractmethod
    def handle_request(self, request: str) -> Optional[str]:
        pass

# Abstract Handler (Base Handler)
class AbstractSupportHandler(SupportHandler):
    _next_handler: Optional[SupportHandler] = None

    def set_next(self, handler: SupportHandler) -> SupportHandler:
        self._next_handler = handler
        return handler

    def handle_request(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return None # No handler could process the request

# Concrete Handlers
class Level1Support(AbstractSupportHandler):
    def handle_request(self, request: str) -> Optional[str]:
        # TODO: Implement handling for simple/basic requests
        pass

class Level2Support(AbstractSupportHandler):
    def handle_request(self, request: str) -> Optional[str]:
        # TODO: Implement handling for technical/complex requests
        pass

class TechnicalLead(AbstractSupportHandler):
    def handle_request(self, request: str) -> Optional[str]:
        # TODO: Implement handling for critical/urgent requests
        pass


# --- Tests ---
def run_tests():
    print("Running Chain of Responsibility Pattern Support System Tests...")

    # Set up the chain
    level1 = Level1Support()
    level2 = Level2Support()
    tech_lead = TechnicalLead()

    level1.set_next(level2).set_next(tech_lead)

    requests = [
        "basic query",
        "technical issue with network",
        "urgent critical server down",
        "simple password reset",
        "unknown request type"
    ]

    expected_results = {
        "basic query": "Level 1 Support handled: basic query",
        "technical issue with network": "Level 2 Support handled: technical issue with network",
        "urgent critical server down": "Technical Lead handled: urgent critical server down",
        "simple password reset": "Level 1 Support handled: simple password reset",
        "unknown request type": None
    }

    for req in requests:
        print(f"\nSending request: '{req}'")
        result = level1.handle_request(req)
        assert result == expected_results[req], f"Test Failed for '{req}': Expected '{expected_results[req]}', Got '{result}'"
        if result:
            print(f"Result: {result}")
        else:
            print(f"Result: Request '{req}' could not be handled by any support level.")

    print("All Chain of Responsibility Pattern Support System Tests Passed!")

if __name__ == "__main__":
    run_tests()
