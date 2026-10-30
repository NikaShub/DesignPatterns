from handler import BaseHandler


class RoleCheckHandler(BaseHandler):
    def handle(self, email: str, password: str, role: str, request_count: int) -> bool:
        if role.upper() != "ADMIN":
            print("Error: Access denied! Admin role required.")
            return False
        print("Admin permissions confirmed.")
        return super().handle(email, password, role, request_count)