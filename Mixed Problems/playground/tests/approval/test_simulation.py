from __future__ import annotations

from decimal import Decimal

import pytest
from approvaltests import verify

from pos.core.campaigns import Campaign, CampaignType, ComboCampaign
from pos.core.pos import POS
from pos.core.receipt import Product
from pos.infra.storage import Storage
from pos.runner.simulation import Simulation


@pytest.fixture
def pos(storage: Storage) -> POS:
    catalog = storage.products()
    catalog.register(
        Product(
            id="1",
            barcode="1234567",
            name="Apple",
            price=Decimal("0.50"),
        ),
    )
    catalog.register(
        Product(
            id="2",
            barcode="3456789",
            name="Banana",
            price=Decimal("1.00"),
        ),
    )
    catalog.register(
        Product(
            id="3",
            barcode="0987632",
            name="Orange",
            price=Decimal("0.40"),
        ),
    )

    campaigns = storage.campaigns()
    campaigns.register(
        Campaign(
            id="1",
            order=1,
            type=CampaignType.single_item,
            discount=Decimal("0.2"),
            product_id="1",
        )
    )
    campaigns.register(
        Campaign(
            id="3",
            order=3,
            type=CampaignType.receipt_total,
            discount=Decimal("0.1"),
            floor=Decimal("0.2"),
        )
    )
    campaigns.register(
        Campaign(
            id="2",
            order=2,
            type=CampaignType.single_item,
            discount=Decimal("0.1"),
            product_id="2",
        )
    )

    return POS(catalog, campaign=ComboCampaign(campaigns))


def test_log(pos: POS) -> None:
    log: list[str] = []
    sim = Simulation(pos, print_fn=log.append)

    sim.run()

    verify(log)
