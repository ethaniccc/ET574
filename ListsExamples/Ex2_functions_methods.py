#Chap 3 Lists
# J. Sun

## Using lists functions/methods
print('\nLists functions/methods\n')

# built-in functions and keyword
team = ["SeaHawks", 2014, "centuryLink Field"]
nums = [5, 10, 4, 5]
words = ["spam", "ni"]

# number of items in list
print("Use len():")
print("Number of words =", len(words), '\n')

# greatest (items must have same type)
print("Use max():")
print("The maximum number of nums =", max(nums), '\n')

# least (items must have same type)
print("Use min():")
print("The minimum number of nums =", min(nums), '\n')

# total (items must be numbers)
print("Use sum():")
print("nums =", nums, "\nSum of nums =", sum(nums), '\n')

# remove the item with index[#]
print("Use del:")
del words[-1]
print('words =', words, '\n')

# create an empty list
fruits = []
print('fruits =', fruits, '\n')
# delete the entire list
del fruits
#print('fruits =', fruits, '\n')     #NameError is produced


## List methods
# removes the element at the specified position
print("Use pop():")
nums.pop(2)     # remove the item on index[2] of the list
print("nums =", nums, '\n')

# pop() method returns removed value
nums.append(100)
n = nums.pop()  # remove the last item from the list
print("The popped number =", n,"\nnums =", nums, '\n')

# removes first occurrence of the specified value
print("Use remove():")
nums.remove(5)
print("nums =", nums, '\n')
team.remove(2014)
print("team =", team, '\n')

# empty the list to produce []
print("Use clear():")
team.clear()
print("team =", team, '\n')

# add the object to the end of the list
print("Use append():")
nums.append(7)
print("nums =", nums, '\n')

#insert new item before item of given index
print("Use insert():")
words.insert(1, "eggs")
print("words =", words, '\n')

#insert new list's items to the end of the list
print("Use extend():")
nums.extend([1, 2])
print("nums =", nums, '\n')

# number of occurrences of an object
print("Use count():")
print("How many 7 in the list?", nums.count(7), '\n')

# index of first occurrence of an object
print("Use index():")
print("Index # of 7 in the list:", nums.index(7), '\n')

# list concatenation
print("Use +:")
print("['a', 1]+[2, 'b'] =", ['a', 1]+[2, 'b'], '\n')

# list repetition
print("Use *:")
print("[0]*3 =", [0]*3, '\n')

# permanent alphabetical sort of the list
print("Use sort():")
print("words =", words, '\n')
words.sort()
print("words =", words, '\n')
#print(words.sort())     #produce None

print("nums =", nums, '\n')
nums.sort(reverse = True)
print("nums =", nums, '\n')
#print(nums.sort(reverse = True))   #produce None

# reverses the order of the items
print("Use reverse():")
nums.reverse()
print("nums =", nums, '\n')

fruits = ["orange", "apple", "mango"]
print("Original fruits =", fruits, '\n')
#print (fruits.reverse())    #produce None
fruits.reverse()
print("Updated fruits =", fruits, '\n')


# temporary alphabetical sorted the copy of the list
print("Use sorted():")
words.append('python')
print("words =", words, '\n')
print("sorted words =", sorted(words), '\n')
print("words =", words, '\n')

words[0] = "c++"
words[1] = "java"
print("words =", words, '\n')
print("sorted words =", sorted(words, reverse = True), '\n')
print("words =", words, '\n')


# a type error is produced if sorted() is applied to
# the list containing both string values AND numeric values
#l = [1,2,3, 'a','b','c']
#print("sorted words =", sorted(l), '\n')
