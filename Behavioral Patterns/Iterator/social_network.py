from abc import ABC, abstractmethod
from typing import List
from profile import Profile
from iterators import ProfileIterator, FacebookIterator


class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, profile_id: str) -> ProfileIterator:
        pass

    @abstractmethod
    def create_coworkers_iterator(self, profile_id: str) -> ProfileIterator:
        pass


class Facebook(SocialNetwork):
    def social_graph_request(self, profile_id: str, req_type: str) -> List[Profile]:
        profiles = []
        if req_type == "friends":
            profiles.append(Profile("1", "friend1@facebook.com"))
            profiles.append(Profile("2", "friend2@facebook.com"))
        elif req_type == "coworkers":
            profiles.append(Profile("3", "coworker1@facebook.com"))
        return profiles

    def create_friends_iterator(self, profile_id: str) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id: str) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "coworkers")