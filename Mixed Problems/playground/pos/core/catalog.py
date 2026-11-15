from collections.abc import Callable, Iterable, MutableMapping
from dataclasses import dataclass, field
from typing import Protocol


def default_key_fn(item: object) -> str:
    return str(item.id)


@dataclass
class InMemoryCatalog[T]:
    items: MutableMapping[str, T] = field(default_factory=dict)

    key_fn: Callable[[T], str] = default_key_fn

    def register(self, item: T) -> None:
        self.items[self.key_fn(item)] = item

    def lookup(self, item_id: str) -> T:
        return self.items[item_id]

    def all(self) -> Iterable[T]:
        return self.items.values()


class Catalog[T](Protocol):
    def register(self, item: T) -> None:
        pass

    def lookup(self, item_id: str) -> T:
        pass

    def all(self) -> Iterable[T]:
        pass
