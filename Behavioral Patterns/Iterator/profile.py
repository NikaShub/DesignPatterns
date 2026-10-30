class Profile:
    def __init__(self, profile_id: str, email: str):
        self._id = profile_id
        self._email = email

    @property
    def id(self) -> str:
        return self._id

    @property
    def email(self) -> str:
        return self._email