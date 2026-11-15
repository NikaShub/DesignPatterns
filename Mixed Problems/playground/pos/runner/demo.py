import httpx
import uvicorn

from pos.infra.api import setup


def demo_request():
    httpx.post(
        "http://localhost:8000/products",
        json={
            "name": "Banana",
            "barcode": "12345677890",
            "price": "5.12",
        },
    ).raise_for_status()

    response = (
        httpx.get("http://localhost:8000/products/12345677890")
        .raise_for_status()
        .json()
    )

    print(response)


if __name__ == "__main__":
    uvicorn.run(app=setup())
