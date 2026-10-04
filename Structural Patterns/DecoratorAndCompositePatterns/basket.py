from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Iterable, Protocol


@dataclass
class Product:
    id: int
    name: str
    price: Decimal


@dataclass
class Basket:
    items: Iterable[BasketItem] = field(default_factory=list)

    def total(self) -> Decimal:
        total = Decimal("0")

        for item in self.items:
            total += item.total()

        return total


class BasketItem(Protocol):
    def total(self) -> Decimal:
        pass


@dataclass
class DefaultBasketItem:
    quantity: int
    item: Product

    def total(self) -> Decimal:
        return self.item.price * self.quantity


@dataclass
class BaseBasketItemDecorator:
    item: BasketItem

    def total(self) -> Decimal:
        return self.item.total()


@dataclass
class DiscountedBasketItem(BaseBasketItemDecorator):
    discount: Decimal

    def total(self) -> Decimal:
        return super().total() * (1 - self.discount)