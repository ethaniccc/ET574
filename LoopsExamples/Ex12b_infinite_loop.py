## Avoiding infinite loop

# initialize a variable to 1
n = 1

# infinite loop (a loop that never ends)
# hit Ctrl-C to stop the execution of the loop
# if this does not work, "kill" the Python process
# using Task Manager (Windows) or Top (OSX)
while n <= 5:
    n -= 1  # n keeps reducing so condition is always true (infinite loop)
