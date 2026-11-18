
# Q4 - Sets: Elective Registration Clash Detection

import time

ai_elective = {
    "192311001",
    "192311004",
    "192311007",
    "192311009"
}

iot_elective = {
    "192311002",
    "192311004",
    "192311009",
    "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

# TODO 1: Set operations

# Students in both electives
both = ai_elective & iot_elective

# Students in exactly one elective
exactly_one = ai_elective ^ iot_elective

# Students in neither elective
neither = all_students - (ai_elective | iot_elective)

print("clash :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither :", sorted(neither))

# Using set methods
print("\nUsing set methods:")

both_method = ai_elective.intersection(iot_elective)

exactly_method = ai_elective.symmetric_difference(iot_elective)

neither_method = all_students.difference(
    ai_elective.union(iot_elective)
)

print("Both:", sorted(both_method))
print("Exactly one:", sorted(exactly_method))
print("Neither:", sorted(neither_method))

# Duplicate removal
students = ["A", "B", "A", "C", "B"]

print("\nOriginal list:", students)
print("After converting to set:", set(students))

# Membership testing
print("\nMembership benchmark:")

for size in [10000, 100000, 1000000]:

    numbers = list(range(size))
    number_set = set(numbers)

    target = size - 1

    start = time.perf_counter()
    found_list = target in numbers
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    found_set = target in number_set
    set_time = time.perf_counter() - start

    print("\nSize:", size)
    print("List search:", list_time)
    print("Set search:", set_time)
    print("Same result:", found_list == found_set)

# Nested loop comparison
a = list(range(1000))
b = list(range(500, 1500))

start = time.perf_counter()

common = []

for x in a:
    for y in b:
        if x == y:
            common.append(x)

nested_time = time.perf_counter() - start

start = time.perf_counter()
common_set = set(a) & set(b)
set_time = time.perf_counter() - start

print("\nNested loop time:", nested_time)
print("Set intersection time:", set_time)

# Edge cases
print("\nEdge cases:")
print("Empty elective:", set() & iot_elective)
print("Identical elective:", ai_elective & ai_elective)

# Tuple and list example
print("\nTuple set:", {(1, 2), (3, 4)})

try:
    print({[1, 2], [3, 4]})
except TypeError as error:
    print("List set error:", error)

print("\nComplexity:")
print("Set membership: O(1) average")
print("Nested loops: O(n*m)")
print("Sorting approach: O(n log n + m log m)")
print("Set operations use approximately O(n+m) time.")
