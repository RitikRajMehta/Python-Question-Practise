data = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

print("Original Dictionary:", data)

# 1. pop() - remove specific key
data.pop("B")
print("After pop('B'):", data)

# 2. popitem() - remove last key-value pair
data.popitem()
print("After popitem():", data)

# 3. del - remove specific key
del data["A"]
print("After del['A']:", data)

# 4. clear() - remove all elements
data.clear()
print("After clear():", data)