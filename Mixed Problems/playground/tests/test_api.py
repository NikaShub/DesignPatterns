import pytest
from fastapi.testclient import TestClient

from pos.infra.api import setup
from pos.infra.storage import InMemoryStorage


@pytest.fixture
def client():
    app = setup()
    app.state.storage = InMemoryStorage()
    app.state.id_generator = iter(["1"])

    return TestClient(app)


def test_should_create(client: TestClient):
    # Give
    product = {
        "name": "Banana",
        "barcode": "12345677890",
        "price": "5.12",
    }

    # When
    response = client.post("/products", json=product)

    # Then
    assert response.status_code == 201
    assert response.json() == {
        "id": "1",
        "name": "Banana",
        "barcode": "12345677890",
        "price": "5.12",
    }


def test_should_persist(client: TestClient):
    # Give
    product = {
        "name": "Banana",
        "barcode": "12345677890",
        "price": "5.12",
    }
    client.post("/products", json=product)

    # When
    response = client.get("/products/12345677890")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "id": "1",
        "name": "Banana",
        "barcode": "12345677890",
        "price": "5.12",
    }
