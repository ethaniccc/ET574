from math import fmod

while True:
    num1 = int(input("Give me a numerator\n> "))
    num2 = int(input("Give me a denominator\n> "))
    print("Let's make sure everything is right here...")

    if num2 == 0:
        print("Hey! The denominator cannot be zero. Let's try this again...")
        continue

    remainder = int(fmod(num1, num2))
    print(f"{num1} mod {num2} = {remainder}")

    # Break out of the loop as we have completed our task.
    break


