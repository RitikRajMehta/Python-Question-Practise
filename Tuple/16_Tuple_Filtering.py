# 16. Tuple Filtering
numbers = (3, 14, 7, 22, 9, 41, 18, 5)
result = tuple(filter(lambda x: x > 10, numbers))
print("Filtered:", result)
