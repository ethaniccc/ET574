vechiles = ['car', 'Truck', 'boat', 'PLANE', 'cAAr']
letter = (input("Input search letter:\n> "))[:1].upper()
print("Searching for " + letter)
for vechile in vechiles:
    vechile_uppercase = vechile.upper()
    pos = -1
    found_inital = False

    while True:
        # Set the starting position of find to pos+1 to avoid infinite recursion.
        pos = vechile_uppercase.find(letter, pos+1)
        if pos == -1:
            if not found_inital:
                print(f"{vechile} does not have the letter \"{letter}\"")
            break # Get out of the loop, there's nothin else to search for.
        else:
            if not found_inital:
                print(f"{vechile} has the letter \"{letter}\" at position {pos}!")
                found_inital = True
            else:
                print(f"{vechile} also has the letter \"{letter}\" at position {pos}!")