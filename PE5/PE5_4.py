months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'] 
shortened = []

for month in months:
    short = month[0:3]
    print(short.upper(), end="|")
    shortened.append(short.capitalize())
print("")
print(shortened)