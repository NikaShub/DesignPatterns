from abc import ABC, abstractmethod
from typing import Optional
from profile import Profile


class ProfileIterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def get_next(self) -> Optional[Profile]:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass


class FacebookIterator(ProfileIterator):
    def __init__(self, facebook, profile_id: str, iter_type: str):
        self._facebook = facebook
        self._profile_id = profile_id
        self._type = iter_type
        self._current_position = 0
        self._cache = None

    def _lazy_init(self) -> None:
        if self._cache is None:
            self._cache = self._facebook.social_graph_request(self._profile_id, self._type)

    def has_next(self) -> bool:
        self._lazy_init()
        return self._current_position < len(self._cache)

    def get_next(self) -> Optional[Profile]:
        if not self.has_next():
            return None
        profile = self._cache[self._current_position]
        self._current_position += 1
        return profile

    def reset(self) -> None:
        self._current_position = 0