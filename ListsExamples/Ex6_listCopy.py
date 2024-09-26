# Chap 3 Lists
# J. Sun

## List copy
print('\nCopying lists\n')
list1 = ['a', 'b']
list2 = list1
list2[1] = 'c'
print(list1, id(list1))
print(list2, id(list2))
print()

#---------------------------
# use list constructor functions, list()
list2 = list(list1)

# use copy() method
#list2 = list1.copy()

#list2 = list(('a','b'))    # convert a tuple to a list
list2 = list("ab")         # convert a string to a list
print(list1, id(list1))
print(list2, id(list2))
print()
