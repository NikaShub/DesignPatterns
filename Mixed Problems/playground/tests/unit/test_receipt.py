from pos.core.basket import Product
from pos.core.catalog import Catalog
from pos.core.receipt import Receipt


def test_should_pop(catalog: Catalog[Product]) -> None:
    receipt = Receipt(catalog=catalog)
    receipt.add("123")
    receipt.add("321")

    item = receipt.pop(item_id="1")

    assert item
    assert item.quantity == 1
