from __future__ import annotations

from collections import defaultdict
from collections.abc import MutableMapping
from dataclasses import dataclass, field

from pos.core.basket import DefaultBasketItem, Product
from pos.core.catalog import Catalog


@dataclass
class Receipt:
    catalog: Catalog[Product]

    items: MutableMapping[str, int] = field(default_factory=lambda: defaultdict(int))

    def add(self, barcode: str) -> None:
        self.items[barcode] += 1

    def pop(self, item_id: str) -> DefaultBasketItem:
        for barcode, quantity in self.items.items():
            product = self.catalog.lookup(barcode)
            if product.id == item_id:
                self.items.pop(barcode)
                return DefaultBasketItem(
                    item=product,
                    quantity=quantity,
                )

        return DefaultBasketItem(quantity=0, item=Product.unknown())

    def get_items(self) -> list[DefaultBasketItem]:
        result = []

        for barcode, quantity in self.items.items():
            product = self.catalog.lookup(barcode)
            item = DefaultBasketItem(item=product, quantity=quantity)
            result.append(item)

        return result
