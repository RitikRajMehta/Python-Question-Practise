# 15. Sort Tuple of Tuples
students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))
result = tuple(sorted(students, key=lambda x: x[1]))
print("Sorted:", result)
