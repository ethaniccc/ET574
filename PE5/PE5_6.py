# A
fruits = ["apple", "banana", "cherry"] 
for item in fruits: # missing colon
    print(item) 

# B
for i in range (1, 4): 
    print(str(i) + '\t' + str(2**i)) # missing typecasts

# C
for j in range (6, 0, -1):  # negative step requires end to be less than start
    print(j) 

# D
letters = ['a', 'b', 'c'] 
upper_letters = []
for letter in letters:
    upper_letters.append(letter.upper())
print(upper_letters)  

# E
fruits = ['apple', 'banana', 'cherry'] # use a list instead of a tuple
print(fruits) 
fruits[0] = 'orange' 
fruits.append('pineapple') 
print(fruits) 