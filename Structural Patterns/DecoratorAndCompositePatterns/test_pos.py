from decimal import Decimal

import pytest

from basket import Product
from pos import ProductCatalog, POS


@pytest.fixture
def catalog() -> ProductCatalog:
    result = ProductCatalog()
    result.register("123", Product(id=1, name="Apple", price=Decimal("7.0")))
    result.register("321", Product(id=2, name="Banana", price=Decimal("15.0")))

    return result


def test_should_checkout_zero_without_scanned_barcodes(catalog: ProductCatalog) -> None:
    pos = POS(catalog)

    total = pos.checkout()

    assert total == Decimal(0)


def test_should_checkout_item_price(catalog: ProductCatalog) -> None:
    pos = POS(catalog)
    pos.scan("123")

    total = pos.checkout()

    assert total == Decimal("7.0")


def test_should_handle_raising_quantity(catalog: ProductCatalog) -> None:
    pos = POS(catalog)
    pos.scan("123")
    pos.scan("123")

    total = pos.checkout()

    assert total == Decimal("14.0")


def test_should_checkout_total_amount(catalog: ProductCatalog) -> None:
    pos = POS(catalog)
    pos.scan("123")
    pos.scan("321")

    total = pos.checkout()

    assert total == Decimal("22.0")