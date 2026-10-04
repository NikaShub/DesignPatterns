from __future__ import annotations

from decimal import Decimal

from basket import Product, Basket, DefaultBasketItem


def test_empty_basket_total_is_zero():
    items = []

    assert Basket(items=items).total() == Decimal("0")


def test_basket_with_one_item():
    items = [
        DefaultBasketItem(
            quantity=1, item=Product(id=1, name="Mint Gum", price=Decimal("0.50"))
        )
    ]

    assert Basket(items=items).total() == Decimal("0.50")


def test_basket_with_multiple_items():
    items = [
        DefaultBasketItem(
            quantity=1,
            item=Product(
                id=1,
                name="Mint Gum",
                price=Decimal("0.50"),
            ),
        ),
        DefaultBasketItem(
            quantity=1,
            item=Product(
                id=2,
                name="Chocolate Bar",
                price=Decimal("1.00"),
            ),
        ),
    ]

    assert Basket(items=items).total() == Decimal("1.50")


def test_basket_item_quantity():
    items = [
        DefaultBasketItem(
            quantity=2, item=Product(id=1, name="Mint Gum", price=Decimal("0.50"))
        )
    ]

    assert Basket(items=items).total() == Decimal("1.00")