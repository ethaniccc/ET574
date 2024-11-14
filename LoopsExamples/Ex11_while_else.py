## Using while & else

n = []              #define a list
i = 1               #define a counter
total = 0           #define an accumulator
while i < 6:        #validate the continuation condition
    total+=i        #use the accumulator to hold the sum
    n.append(i)     #populate the list
    print(i)        #display each number
    i += 1          #update counter
else:
    print(f"\nSum = {total}")
    print(f"Sum = {sum(n)}")
    print(n)
