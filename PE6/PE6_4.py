# verify_user ensures that the wanted username isn't already taken. checking if a username
# is taken is case-insensitive.
def verify_user(existing, wanted):
    for existing_user in existing:
        if wanted.lower() == existing_user.lower():
            return False
    return True

current_users = ["ethaniccc", "someRandomGuy", "idk_user42", "python_enjoyer", "0xff"]
wanted_username = input("What do you want your username to be?\n> ")

# verify that the username isn't taken
if verify_user(current_users, wanted_username):
    print(f"Great, {wanted_username} is still available!")
    current_users.append(wanted_username) # add the new username to the current users list.
else:
    print(f"Sorry {wanted_username}, that name is taken :<")