from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from pos.core.basket import Product
from pos.core.campaigns import CampaignProcessor, ComboCampaign, NoCampaign
from pos.core.catalog import Catalog
from pos.core.receipt import Receipt
from pos.infra.storage import Storage


@dataclass
class POS:
    catalog: Catalog[Product]
    campaign: CampaignProcessor = field(default_factory=NoCampaign)

    _receipt: Receipt = field(init=False)

    @classmethod
    def create(cls, storage: Storage):
        return cls(
            catalog=storage.products(),
            campaign=ComboCampaign(storage.campaigns()),
        )

    def __post_init__(self) -> None:
        self._receipt = Receipt(self.catalog)

    def scan(self, barcode: str) -> None:
        self._receipt.add(barcode)

    def checkout(self) -> Decimal:
        return self.campaign.apply_to(self._receipt).total()
