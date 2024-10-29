# A: [0, 1, 2, 3, 4]
# B: [0, 1, 2, 3, 4]
# C: [-10, -9, ..., 8, 9]
# C: -10 9 -10
# D: 2 10

# E
odd_num = list(range(1, 10, 2))
print(odd_num)

# F
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
for cube in cubes:
    print(cube)

# G
for cube in cubes:
    print(cube, end="|")