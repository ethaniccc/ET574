## Using while loop with continue

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

'''
# continue is used to skip the current iteration
# and jump to the next iteration in the loop
# an infinite loop has occoured due to updating counter value is skipped
i = 1
while i < 6:
    print(i)
    if i == 3:
        continue
    i += 1
'''
