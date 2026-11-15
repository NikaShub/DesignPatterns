from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from pos.core.pos import POS


@dataclass
class Simulation:
    pos: POS

    print_fn: Callable[[str], None] = print

    def run(self) -> None:
        self.pos.scan("1234567")
        self.pos.scan("3456789")
        self.pos.scan("0987632")
        self.pos.scan("1234567")

        total = self.pos.checkout()

        self.print_fn(f"Total payable amount is {total}")
