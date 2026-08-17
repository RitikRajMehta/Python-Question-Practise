# 22. Nested Tuple Flattening
def flatten(t):
    result = []
    for item in t:
        if isinstance(item, tuple):
            result.extend(flatten(item))
        else:
            result.append(item)
    return tuple(result)

nested = (1, (2, 3), (4, (5, (6, 7))))
print("Flattened:", flatten(nested))
