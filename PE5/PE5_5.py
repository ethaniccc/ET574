rnge = int(input("Enter a range: "))
num = int(input("Enter an integer number: "))
for i in range(0, rnge+1):
    print(f"{i:<6}*{num:>6}{'=':>6}{num*i:>6}")