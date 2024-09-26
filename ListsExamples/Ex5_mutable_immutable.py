# Chap 3 Lists
# J. Sun

## Mutable and immutable objects
print('\nMutable and immutable objects\n')

L = [5, 6]              #list
n = 2                   #number
s = "Python"            #string
t = ('a', 'b', 'c')     #tuple

print(L, id(L))
L.append(7)
print(L, id(L))
print()

print(n, id(n))
n += 1
print(n, id(n))
print()

print(s, id(s))
s = s.upper()
print(s, id(s))
print()

print(t, id(t))
t = t[1:]
print(t, id(t))
print()
