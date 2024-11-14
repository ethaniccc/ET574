## Using while with lists
# use a while loop to remove all cats in the list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
print()

#use a for loop to remove all dogs from the list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
for x in pets:
    if x == 'cat':
        pets.remove(x)
print(pets)
print()
