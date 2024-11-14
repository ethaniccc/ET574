## Using  dictionaries
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']

for friend in friends:
    friend_favorite_language = favorite_languages.get(friend)
    assert friend_favorite_language != None
    print(f"\t{friend.title()}, I see you love {friend_favorite_language.title()}")