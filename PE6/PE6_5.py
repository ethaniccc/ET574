vechiles = ['car', 'Truck', 'boat', 'PLANE']
letter = (input("Input search letter:\n> "))[:1].upper()
print("Searching for " + letter)
for vechile in vechiles:
    pos = vechile.upper().find(letter)
    if pos == -1:
        print(f"{vechile} does not have the letter \"{letter}\".")
    else:
        print(f"{vechile} has the letter \"{letter}\" at position {pos}.")