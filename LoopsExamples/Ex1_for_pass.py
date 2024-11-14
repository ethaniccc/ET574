## Using for loop

#else block of code to be executed when the loop is finished
for x in range(6):
    print(x, end = " ")
else:
    print("Finally finished!")

#pass is a do-nothing placeholder
for x in range(6):
    pass

#List Comprehensions
squares = [value**2 for value in range(1, 11)]
for x in squares:
    print(x, end = " ")

for x in squares:
    pass
