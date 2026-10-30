from handler import BaseHandler


class AuthenticationHandler(BaseHandler):
    def handle(self, email: str, password: str, role: str, request_count: int) -> bool:
        if email != "admin@app.com" or password != "secret123":
            print("Error: Invalid email or password!")
            return False
        print("Authentication successful.")
        return super().handle(email, password, role, request_count)