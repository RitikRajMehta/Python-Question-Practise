data = {
    "name": "Ritik",
    "age": 22,
    "course": "MCA",
    "city": "Delhi"
}

print("Original Dictionary:", data)

# 1. Using [] - access value using key
print("Using []:", data["name"])

# 2. Using get() - access value safely
print("Using get():", data.get("age"))

# 3. Using keys() - access keys and their values
print("Using keys():")
for key in data.keys():
    print(key, "=", data[key])

# 4. Using values() - access all values
print("Using values():")
for value in data.values():
    print(value)

# 5. Using items() - access key and value together
print("Using items():")
for key, value in data.items():
    print(key, "=", value)