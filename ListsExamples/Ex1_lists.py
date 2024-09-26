# Chap 3 Lists
# J. Sun

## Intro to lists
print('\nLists\n')

# Create lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ['a', 'b', 'c']
numLets = [1, 2, 3, 'a', 'b', 'c', "python", 3.14, 12.34]

# prints the entire lists with brackets
print('numbers =', numbers)
print('letters =', letters)
print('numLets =', numLets)
print()

# print the length of the list numbers (total number of elements)
print("Use len():")
print(len(numbers))
print(len(letters))
print(len(numLets))
print()
print('Last item in the list = ', numbers[len(numbers)-1])
print('Middle item in the list = ', letters[len(letters)//2])
print()

# greatest (items must have same type)
print("Use max():")
print("The maximum number of numbers =", max(numbers), '\n')

# least (items must have same type)
print("Use min():")
print("The minimum number of numbers =", min(numbers), '\n')

# total (items must be numbers)
print("Use sum():")
print("numbers =", numbers, "\nSum of numbers =", sum(numbers), '\n')
