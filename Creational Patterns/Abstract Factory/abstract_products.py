from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        pass