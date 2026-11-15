from dataclasses import dataclass, field
from typing import Any, Protocol

from pos.core.basket import Product
from pos.core.campaigns import Campaign
from pos.core.catalog import Catalog, InMemoryCatalog


@dataclass
class InMemoryStorage:
    cache: dict[str, Catalog[Any]] = field(default_factory=dict)

    def products(self) -> Catalog[Product]:
        if "products" not in self.cache:
            self.cache["products"] = InMemoryCatalog[Product](
                key_fn=lambda product: product.barcode
            )

        return self.cache["products"]

    def campaigns(self) -> Catalog[Campaign]:
        return InMemoryCatalog[Campaign]()


class SqliteStorage:
    def products(self) -> Catalog[Product]:
        pass

    def campaigns(self) -> Catalog[Campaign]:
        pass


class Storage(Protocol):
    def products(self) -> Catalog[Product]:
        pass

    def campaigns(self) -> Catalog[Campaign]:
        pass
