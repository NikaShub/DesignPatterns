from decimal import Decimal

import pytest

from pos.core.basket import Product
from pos.core.catalog import Catalog
from pos.infra.storage import InMemoryStorage


@pytest.fixture
def catalog(storage: InMemoryStorage) -> Catalog[Product]:
    result = storage.products()
    result.register(
        Product(
            id="1",
            barcode="123",
            name="Apple",
            price=Decimal("7.0"),
        ),
    )
    result.register(
        Product(
            id="2",
            barcode="321",
            name="Banana",
            price=Decimal("15.0"),
        ),
    )

    return result
