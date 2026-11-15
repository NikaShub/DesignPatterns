from __future__ import annotations

from decimal import Decimal

from pos.core.basket import Basket, DefaultBasketItem, Product


def test_empty_basket_total_is_zero() -> None:
    assert Basket(items=[]).total() == Decimal("0")


def test_basket_with_one_item() -> None:
    items = [
        DefaultBasketItem(
            quantity=1,
            item=Product(
                id="1",
                barcode="123",
                name="Mint Gum",
                price=Decimal("0.50"),
            ),
        )
    ]

    assert Basket(items=items).total() == Decimal("0.50")


def test_basket_with_multiple_items() -> None:
    items = [
        DefaultBasketItem(
            quantity=1,
            item=Product(
                id="1",
                barcode="123",
                name="Mint Gum",
                price=Decimal("0.50"),
            ),
        ),
        DefaultBasketItem(
            quantity=1,
            item=Product(
                id="2",
                barcode="123",
                name="Chocolate Bar",
                price=Decimal("1.00"),
            ),
        ),
    ]

    assert Basket(items=items).total() == Decimal("1.50")


def test_basket_item_quantity() -> None:
    items = [
        DefaultBasketItem(
            quantity=2,
            item=Product(
                id="1",
                barcode="123",
                name="Mint Gum",
                price=Decimal("0.50"),
            ),
        )
    ]

    assert Basket(items=items).total() == Decimal("1.00")
