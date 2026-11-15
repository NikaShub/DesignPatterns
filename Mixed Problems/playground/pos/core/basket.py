from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Protocol


@dataclass
class Product:
    id: str
    barcode: str
    name: str
    price: Decimal

    @classmethod
    def unknown(cls) -> Product:
        return cls(
            id="0",
            barcode="",
            name="Unknown",
            price=Decimal("0"),
        )


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

    floor: Decimal = Decimal("0")

    def total(self) -> Decimal:
        total = super().total()

        if total < self.floor:
            return total

        return total * (1 - self.discount)
