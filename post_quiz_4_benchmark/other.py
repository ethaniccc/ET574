import time

runs = []

while len(runs) != 10_000:
    t = time.time_ns()
    even_multiples_of_3 = [x for x in range(1, 1000) if x % 6 == 0]
    for num in even_multiples_of_3:
        print(num, end=" ")
    print(f"\nSum: {sum(even_multiples_of_3)}")
    runs.append(time.time_ns() - t)

print("Avg:", sum(runs)/10_000)