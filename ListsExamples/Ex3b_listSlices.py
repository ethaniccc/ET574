#Chap 3 Lists
# J. Sun

## list Slices
print('\nList Slices\n')

grades = ['A', 'B', 'C', 'D', 'F']
print("grades =", grades, '\n')

# range of Indexes
print("grades[1:3] =", grades[1:3], '\n')

# range negative indexes
print("grades[-4:-2] =", grades[-4:-2], '\n')

# start at index 0 (included) and end at index 3 (4-1)
print("grades[:4] =", grades[:4],'\n')

# start at index 2 (included) and go on to the end of the list
print("grades[2:] =", grades[2:], '\n')

# By leaving out the start value and the end value, the range covers the whole list
print("grades[:] =", grades[:], '\n')

# use len() to determine the start/end value
print("grades[2:len(grades)] =", grades[2:len(grades)], '\n')

# use [][] to access specified list items
print("(grades[1:3])[1] =", grades[1:3][1], '\n')

# produce an empty list if start value is less than or equal the end value
print("grades[3:2] =", grades[3:2], '\n')


del (grades[-1])
del (grades[1:3])
print(grades)

del grades  # the list, grades is deleted
#print(grades)
