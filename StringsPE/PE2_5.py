pyramindBaseLength = int(input("Pyramind base length: "))
if pyramindBaseLength%2 == 0:
    print("pls odd number :(")
    exit(0)
elif pyramindBaseLength < 5:
    print("at pleast 5 for the base plz :>")
    exit(0)

# Make the base that will be used for each level - as each needs to be as
# long as the base of the pyramind.
basePyramindLevel = ""
middleIndex = pyramindBaseLength//2 + 1
while len(basePyramindLevel) != pyramindBaseLength:
    # we want a star always at the middle of each level.
    if len(basePyramindLevel)-1 == middleIndex:
        basePyramindLevel += "*"
    else:
        basePyramindLevel += " "

requiredStarsForLevel = 1
while requiredStarsForLevel <= pyramindBaseLength:
    # we start with one star on every level of the pyramind in the middle
    pyramindLevel = basePyramindLevel
    sideOffset = 0
    currentStarsOnLevel = 1

    # we need to set the sides of the pyramind
    while currentStarsOnLevel < requiredStarsForLevel:
        leftBound = middleIndex-sideOffset
        rightBound = middleIndex+sideOffset

        # set the left side of the pyramind
        pyramindLevel = pyramindLevel[:leftBound] + "*" + pyramindLevel[leftBound+1:]
        # set the right side
        pyramindLevel = pyramindLevel[:rightBound+1] + "*" + pyramindLevel[rightBound+1:]

        # increase the offset by one so that we can add more
        # stars to the side as necessary until the current amount
        # of stars on this level is equal to the amount we need.
        sideOffset += 1
        # add the current stars by two because we added one to the left, and one to the right.
        currentStarsOnLevel += 2
    
    # print this level of the pyramind :p
    print(pyramindLevel)
    
    # the level below this current one must have two extra stars - 
    # one left side, and one right.
    requiredStarsForLevel += 2
    

print("i believe this is what you were looking for")