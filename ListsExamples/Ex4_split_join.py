# Chap 3 Lists
# J. Sun

## split() & join()
print('\nsplit() & join() methods\n')

# use split() method to turn a string into a list
print('\nsplit() method\n')
letters = "a,b,c"
print(letters.split(','))
print(letters)
print()

newLets = letters.split(',')
print(type(newLets), "newLets =", newLets)
print()

# any string can be used as a separator
print("Hello**Python**World!".split('**'))
print()
print("Hello Python World!".split(" Python "))
print()
print("Hello Python World!".split(" "))
print()

# if no separator is specified, split() uses whitespace as the separator
# whitespace is any string whose characters are newline, vertical tab or space characters
print("Hello Python World!".split())
print()
print("Hello\nPython\nWorld!".split())
print()
print("Hello\tPython\tWorld!".split())
print()

#-----------------------------------------
# The join method turns a list of strings into a single string
print('\njoin() method\n')
letters = ['a', 'b', 'c']
print(','.join(letters))
print()

line1 = ['to', 'be']
line2 = ['or', 'not']
newLine = line1+line2+line1
print("newLine =", newLine, '\n')
print("newLine[0] =", newLine[0], '\n')
print("newLine[0][0] =", newLine[0][0], '\n')

line = ' '.join(newLine)
print(type(line), '\n')
print("line =", line, '\n')
print("line[0] =", line[0], '\n')
