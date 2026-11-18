
# Q1 - Lists and Slicing: Daily Rainfall Records

import random
import time

# Generate 365 daily rainfall readings
random.seed(42)
readings = [round(random.uniform(0, 40), 1) for _ in range(365)]

# Calculate weekly totals using slicing
weekly_totals = []

for i in range(0, len(readings), 7):
    weekly_totals.append(sum(readings[i:i + 7]))

print("Weekly rainfall totals:")
print(weekly_totals)

# Find wettest and driest weeks
wettest_week = weekly_totals.index(max(weekly_totals)) + 1
driest_week = weekly_totals.index(min(weekly_totals)) + 1

print("\nWettest week:", wettest_week)
print("Driest week:", driest_week)

# Find maximum and minimum daily rainfall
print("Maximum rainfall:", max(readings))
print("Minimum rainfall:", min(readings))

# Find dry days
dry_days = []

for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i + 1)

print("Dry days:", dry_days)

# Explain slicing
print("\nSlicing examples:")
print("readings[7:14]:", readings[7:14])
print("readings[-7:]:", readings[-7:])
print("readings[::7]:", readings[::7])

# Naive moving average
def naive_average(data):
    result = []

    for i in range(len(data) - 6):
        result.append(sum(data[i:i + 7]) / 7)

    return result

# Running sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    total = sum(data[:7])
    result.append(total / 7)

    for i in range(7, len(data)):
        total = total + data[i] - data[i - 7]
        result.append(total / 7)

    return result

print("\nMoving average:")
print(naive_average(readings)[:10])

# Benchmark comparison
print("\nBENCHMARK")

for size in [365, 36500, 365000]:

    data = [random.uniform(0, 40) for _ in range(size)]

    start = time.perf_counter()
    naive_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running_average(data)
    running_time = time.perf_counter() - start

    print("Readings:", size)
    print("Naive time:", naive_time)
    print("Running sum time:", running_time)

# Edge cases
print("\nEdge cases:")
print("Empty list:", naive_average([]))
print("Short list:", naive_average([2, 4, 5]))

print("\nComplexity:")
print("Naive moving average: O(7n) = O(n)")
print("Running sum moving average: O(n)")
print("List insertion: O(n) in the general case")
