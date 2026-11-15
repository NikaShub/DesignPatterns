from collections.abc import Iterable
from dataclasses import dataclass
from typing import Annotated
from uuid import uuid4

from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.requests import Request

from pos.core.basket import Product
from pos.core.catalog import Catalog
from pos.infra.storage import InMemoryStorage

api = FastAPI()


@dataclass
class CreateProductRequest:
    name: str
    barcode: str
    price: str


def id_generator():
    while True:
        yield str(uuid4())


def get_generator(request: Request) -> Iterable[str]:
    return request.app.state.ids


def get_products(request: Request) -> Catalog[Product]:
    return request.app.state.storage.products()


@api.post(path="/products", status_code=201)
def create_product(
    ids: Annotated[Iterable[str], Depends(get_generator)],
    products: Annotated[Catalog[Product], Depends(get_products)],
    request: CreateProductRequest,
):
    product = Product(
        id=next(ids),
        name=request.name,
        barcode=request.barcode,
        price=request.price,
    )
    products.register(product)

    return product


@api.get(path="/products/{item_id}")
def read_product(
    item_id: str,
    products: Annotated[Catalog[Product], Depends(get_products)],
):
    return products.lookup(item_id)


def setup() -> FastAPI:
    api.state.storage = InMemoryStorage()
    api.state.ids = id_generator()

    return api
