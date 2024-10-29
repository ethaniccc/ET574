users = ["tom", "jerry", "bob", "dora", "admin"]
for user in users:
    if user == "admin":
        print(f"Hello {user.upper()}, would you like to see a status report?")
    else:
        print(f"Hello {user.capitalize()}, thank you for logging in again!")