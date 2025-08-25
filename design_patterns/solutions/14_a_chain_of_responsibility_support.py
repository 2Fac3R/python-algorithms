
from abc import ABC, abstractmethod
from typing import Optional

"""
Solution for: Customer Support System with Chain of Responsibility
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
        if "simple" in request.lower() or "basic" in request.lower():
            return f"Level 1 Support handled: {request}"
        else:
            print(f"Level 1 Support cannot handle '{request}'. Passing to next...")
            return super().handle_request(request)

class Level2Support(AbstractSupportHandler):
    def handle_request(self, request: str) -> Optional[str]:
        if "technical" in request.lower() or "complex" in request.lower():
            return f"Level 2 Support handled: {request}"
        else:
            print(f"Level 2 Support cannot handle '{request}'. Passing to next...")
            return super().handle_request(request)

class TechnicalLead(AbstractSupportHandler):
    def handle_request(self, request: str) -> Optional[str]:
        if "critical" in request.lower() or "urgent" in request.lower():
            return f"Technical Lead handled: {request}"
        else:
            print(f"Technical Lead cannot handle '{request}'. Passing to next...")
            return super().handle_request(request)
