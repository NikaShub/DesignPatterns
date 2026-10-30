from iterators import ProfileIterator


class SocialSpammer:
    def send(self, iterator: ProfileIterator, message: str) -> None:
        while iterator.has_next():
            profile = iterator.get_next()
            if profile:
                print(f"Email sent to: {profile.email} | Message: {message}")