from throttling_handler import ThrottlingHandler
from authentication_handler import AuthenticationHandler
from role_check_handler import RoleCheckHandler


if __name__ == "__main__":
    chain = ThrottlingHandler(5)
    chain.set_next(AuthenticationHandler()).set_next(RoleCheckHandler())

    print("=== Test 1: Valid Admin Request ===")
    res1 = chain.handle("admin@app.com", "secret123", "ADMIN", 2)
    print(f"Result: {'Access Granted' if res1 else 'Access Denied'}\n")

    print("=== Test 2: Invalid Password ===")
    res2 = chain.handle("admin@app.com", "wrong_pass", "ADMIN", 1)
    print(f"Result: {'Access Granted' if res2 else 'Access Denied'}\n")

    print("=== Test 3: Insufficient Permissions ===")
    res3 = chain.handle("admin@app.com", "secret123", "USER", 3)
    print(f"Result: {'Access Granted' if res3 else 'Access Denied'}\n")

    print("=== Test 4: Rate Limit Exceeded ===")
    res4 = chain.handle("admin@app.com", "secret123", "ADMIN", 10)
    print(f"Result: {'Access Granted' if res4 else 'Access Denied'}")