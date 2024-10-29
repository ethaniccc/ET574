import time

runs = []
while len(runs) != 10_000:
    t = time.time_ns()
    nums = []
    mul_sum = 0

    for num in range(6, 1000, 6):
        mul_sum += num
        print(f"{num}", end=" ")
        nums.append(num)
    else:
        print(f"\nSum: {mul_sum}")
    runs.append(time.time_ns() - t)

print("Avg:", sum(runs)/10_000)

    