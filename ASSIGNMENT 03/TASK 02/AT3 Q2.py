
import copy
import sys

# 1. Tuple as dictionary key
stops = {
    (10, 20): "Bus Stop A",
    (30, 40): "Bus Stop B"
}
print("Bus Stop:", stops[(10, 20)])

# 2. Aliasing problem
bad = [[0] * 3] * 3
bad[0][0] = 9
print("\nAliasing Problem:", bad)

# 3. Correct grid using list comprehension
good = [[0 for j in range(3)] for i in range(3)]
good[0][0] = 9
print("Correct Grid:", good)

# 4. Shallow copy and deep copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

original[0][0] = 99

print("\nOriginal:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

# 5. Tuple unpacking
student = ("Ravi", 20, "ECE")
name, age, department = student
print("\nName:", name)
print("Age:", age)
print("Department:", department)

# 6. Identity and memory
a = [1, 2, 3]
b = a
c = a.copy()

print("\nID of a:", id(a))
print("ID of b:", id(b))
print("ID of c:", id(c))
print("a is b:", a is b)
print("a is c:", a is c)

# 7. List and tuple memory comparison
list_data = list(range(100000))
tuple_data = tuple(range(100000))

print("\nList Memory:", sys.getsizeof(list_data), "bytes")
print("Tuple Memory:", sys.getsizeof(tuple_data), "bytes")

# 8. Mutable list inside tuple
data = ([10, 20], "Python")
data[0].append(30)
print("\nTuple with Mutable List:", data)

# 9. List as dictionary key
try:
    sample = {[1, 2]: "Value"}
except TypeError as e:
    print("\nList Key Error:", e)

# 10. Sparse dictionary alternative
grid = {
    (0, 0): 9,
    (2, 1): 5
}
print("\nSparse Grid:", grid)
