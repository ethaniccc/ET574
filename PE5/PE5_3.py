multiples_of4 = []
for i in range(0, 11):
    multiples_of4.append(i * 4)
print(multiples_of4)

multiples_of2 = []
for multiple in multiples_of4:
    multiples_of2.append(multiple // 2)
print(multiples_of2)

multiples_of1 = multiples_of2.copy()
index = 0
cap = len(multiples_of1)
while index != cap:
    multiples_of1[index] = multiples_of1[index] // 2
    index += 1
print(multiples_of1)