# 21. Tuple Mutability
t = (1, 2, [3, 4, 5])
print("Before:", t)
t[2].append(99)
print("After:", t)
print("Same object?", True)
