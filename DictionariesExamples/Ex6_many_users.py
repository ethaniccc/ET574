## A dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    'bens456': {
        'first': 'benjamin',
        'last': 'saulon',
        'location': 'new york city'
    },
    'olduser001': {
        'first': 'nathan',
        'location': 'new york',
    },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")

    first_name = user_info.get('first')
    last_name = user_info.get('last')
    location = user_info.get('location')

    # Ensure all fields are present in the user data.
    try:
        assert first_name != None
        assert last_name != None
        assert location != None
    except:
        print(f"\tUser is malformed - please update this {username}'s data")
        continue

    full_name = f"{first_name} {last_name}"
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
