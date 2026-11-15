from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum, auto
from typing import Protocol

from pos.core.basket import Basket, BasketItem, DiscountedBasketItem
from pos.core.catalog import Catalog
from pos.core.receipt import Receipt


class CampaignType(Enum):
    single_item = auto()
    receipt_total = auto()


@dataclass
class Campaign:
    id: str
    order: int
    type: CampaignType
    discount: Decimal

    product_id: str | None = None
    floor: Decimal | None = None

    def processor(self) -> CampaignProcessor:
        if self.type == CampaignType.single_item:
            assert self.product_id is not None
            return SingleItemCampaign(
                discount=self.discount,
                product_id=self.product_id,
            )

        if self.type == CampaignType.receipt_total:
            assert self.floor is not None
            return TotalDiscountCampaign(
                discount=self.discount,
                floor=self.floor,
            )

        return NoCampaign()


def campaign_id(item: Campaign) -> str:
    return item.id


class CampaignProcessor(Protocol):
    def follow_with(self, other: CampaignProcessor) -> CampaignProcessor:
        pass

    def apply_to(self, receipt: Receipt) -> BasketItem:
        pass


class NoCampaign:
    def follow_with(self, other: CampaignProcessor) -> CampaignProcessor:
        return other

    def apply_to(self, receipt: Receipt) -> BasketItem:
        return Basket(receipt.get_items())


@dataclass
class ComboCampaign:
    campaigns: Catalog[Campaign]

    following: CampaignProcessor = field(default_factory=NoCampaign)

    def follow_with(self, other: CampaignProcessor) -> CampaignProcessor:
        return ComboCampaign(self.campaigns, following=other)

    def apply_to(self, item: Receipt) -> BasketItem:
        return self.processor().apply_to(item)

    def processor(self) -> CampaignProcessor:
        ordered = sorted(self.campaigns.all(), key=lambda c: c.order)
        processor: CampaignProcessor = NoCampaign()

        for campaign in ordered:
            processor = processor.follow_with(campaign.processor())

        return processor


@dataclass
class SingleItemCampaign:
    discount: Decimal
    product_id: str

    following: CampaignProcessor = field(default_factory=NoCampaign)

    def follow_with(self, other: CampaignProcessor) -> CampaignProcessor:
        return SingleItemCampaign(self.discount, self.product_id, following=other)

    def apply_to(self, receipt: Receipt) -> BasketItem:
        return Basket(
            [
                DiscountedBasketItem(
                    discount=self.discount,
                    item=receipt.pop(item_id=self.product_id),
                ),
                self.following.apply_to(receipt),
            ]
        )


@dataclass
class TotalDiscountCampaign:
    discount: Decimal
    floor: Decimal

    following: CampaignProcessor = field(default_factory=NoCampaign)

    def follow_with(self, other: CampaignProcessor) -> CampaignProcessor:
        return TotalDiscountCampaign(self.discount, self.floor, following=other)

    def apply_to(self, receipt: Receipt) -> BasketItem:
        return DiscountedBasketItem(
            self.following.apply_to(receipt),
            discount=self.discount,
            floor=self.floor,
        )
