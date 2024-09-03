# Intro Examples
# using print() function to display

def nonsense(message, count):
    buffer = ""
    i = 0
    while i != count:
        i += 1
        buffer += message
    print(buffer)

print("Hello Benjamin!")
print("Hello python World")
print("Hello ET574")

nonsense("ET574", 1000)