from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, origin: str, destination: str) -> list[str]:
        pass