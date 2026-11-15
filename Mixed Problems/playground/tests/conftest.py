from __future__ import annotations

import pytest

from pos.infra.storage import InMemoryStorage


@pytest.fixture
def storage() -> InMemoryStorage:
    return InMemoryStorage()
