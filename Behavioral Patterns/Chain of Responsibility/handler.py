from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass

    @abstractmethod
    def handle(self, email: str, password: str, role: str, request_count: int) -> bool:
        pass


class BaseHandler(Handler):
    def __init__(self) -> None:
        self._next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, email: str, password: str, role: str, request_count: int) -> bool:
        if self._next_handler:
            return self._next_handler.handle(email, password, role, request_count)
        return True