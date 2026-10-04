from dataclasses import dataclass, field
from decimal import Decimal
from typing import MutableMapping, Protocol, Self

from basket import Product, DefaultBasketItem, BasketItem, DiscountedBasketItem, Basket


@dataclass
class ProductCatalog:
    products: MutableMapping[str, Product] = field(default_factory=dict)

    def register(self, barcode: str, product: Product) -> None:
        self.products[barcode] = product

    def lookup(self, barcode: str) -> Product:
        return self.products[barcode]


class Campaign(Protocol):
    def apply_to(self, item: DefaultBasketItem) -> BasketItem:
        pass


@dataclass
class ComboCampaign:
    campaigns: list[Campaign] = field(default_factory=list)

    def add(self, campaign: Campaign) -> Self:
        self.campaigns.append(campaign)

        return self

    def apply_to(self, item: DefaultBasketItem) -> BasketItem:
        results = []
        for campaign in self.campaigns:
            results.append(campaign.apply_to(item))

        return self._cheapest_of(item, results)

    def _cheapest_of(
        self,
        item: DefaultBasketItem,
        results: list[BasketItem],
    ) -> BasketItem:
        selected = item

        for item in results:
            if item.total() < selected.total():
                selected = item

        return selected


@dataclass
class SingleItemCampaign:
    id: int
    discount: Decimal
    product_id: int

    def apply_to(self, item: DefaultBasketItem) -> BasketItem:
        if item.item.id != self.product_id:
            return item

        return DiscountedBasketItem(discount=self.discount, item=item)


@dataclass
class NoCampaign:
    def apply_to(self, item: DefaultBasketItem) -> BasketItem:
        return item


@dataclass
class POS:
    catalog: ProductCatalog = field(default_factory=ProductCatalog)
    items: list[DefaultBasketItem] = field(default_factory=list)
    campaign: Campaign = field(default_factory=NoCampaign)

    def scan(self, barcode: str):
        product = self.catalog.lookup(barcode)
        for item in self.items:
            if item.item.id == product.id:
                item.quantity += 1
                return
        self.items.append(DefaultBasketItem(item=product, quantity=1))

    def checkout(self) -> Decimal:
        return Basket(self.apply_discount()).total()

    def apply_discount(self) -> list[BasketItem]:
        items = []

        for item in self.items:
            items.append(self.campaign.apply_to(item))

        return items