from handler import BaseHandler


class ThrottlingHandler(BaseHandler):
    def __init__(self, request_limit: int) -> None:
        super().__init__()
        self._request_limit = request_limit

    def handle(self, email: str, password: str, role: str, request_count: int) -> bool:
        if request_count > self._request_limit:
            print("Error: Request limit exceeded!")
            return False
        print("Throttling check passed.")
        return super().handle(email, password, role, request_count)