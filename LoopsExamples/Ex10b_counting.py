## Using while loop with continue

current_number = 0
while current_number < 20:
    current_number += 1
    if current_number % 2 == 0:
        continue    #ignore the rest of code and return to the beginning of the loop
    print(current_number)
