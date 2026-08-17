# 23. Memory Efficiency
import sys

data = range(1_000_000)
list_data = list(data)
tuple_data = tuple(data)

list_size = sys.getsizeof(list_data)
tuple_size = sys.getsizeof(tuple_data)

print("List size:", list_size)
print("Tuple size:", tuple_size)
print("Difference:", list_size - tuple_size)
