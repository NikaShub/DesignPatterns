from decimal import Decimal

from basket import Product
from pos import ProductCatalog, SingleItemCampaign, POS, ComboCampaign

catalog = ProductCatalog()
catalog.register("1234567", Product(id=1, name="Apple", price=Decimal("0.50")))
catalog.register("3456789", Product(id=2, name="Banana", price=Decimal("1.00")))
catalog.register("0987632", Product(id=3, name="Orange", price=Decimal("0.40")))

pos = POS(
    catalog,
    campaign=(
        ComboCampaign()
        .add(
            SingleItemCampaign(
                id=1,
                discount=Decimal("0.2"),
                product_id=1,
            )
        )
        .add(
            SingleItemCampaign(
                id=2,
                discount=Decimal("0.1"),
                product_id=2,
            )
        )
    ),
)
pos.scan("1234567")
pos.scan("3456789")
pos.scan("0987632")
pos.scan("1234567")
total = pos.checkout()

print(f"Total payable amount is {total}")