## Using % modulo operator

#import random
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

#number = random.randint(-1000, 1000)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
