from decimal import Decimal

from pos.core.basket import Product
from pos.core.catalog import Catalog
from pos.core.pos import POS


def test_should_checkout_zero_without_scanned_barcodes(
    catalog: Catalog[Product],
) -> None:
    pos = POS(catalog)

    total = pos.checkout()

    assert total == Decimal(0)


def test_should_checkout_item_price(catalog: Catalog[Product]) -> None:
    pos = POS(catalog)
    pos.scan("123")

    total = pos.checkout()

    assert total == Decimal("7.0")


def test_should_handle_raising_quantity(catalog: Catalog[Product]) -> None:
    pos = POS(catalog)
    pos.scan("123")
    pos.scan("123")

    total = pos.checkout()

    assert total == Decimal("14.0")


def test_should_checkout_total_amount(catalog: Catalog[Product]) -> None:
    pos = POS(catalog)
    pos.scan("123")
    pos.scan("321")

    total = pos.checkout()

    assert total == Decimal("22.0")
