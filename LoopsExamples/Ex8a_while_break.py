## Using while loop with break

i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # the loop is immediately exited when i is 3
    i += 1


i = 0
while i < 6:
    i += 1
    print(i, end = " ")
    if i == 3:
        break
