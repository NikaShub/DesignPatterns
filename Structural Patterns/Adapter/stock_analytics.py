from abc import ABC, abstractmethod


class StockAnalytics(ABC):
    @abstractmethod
    def analyze_stock_data(self, xml_data: str) -> None:
        pass