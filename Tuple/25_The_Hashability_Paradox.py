# 25. The Hashability Paradox
my_dict = {}

my_dict[(1, 2)] = "immutable tuple"
print("(1, 2) as key: success, value =", my_dict[(1, 2)])

try:
    my_dict[(1, [2])] = "mutable tuple"
except TypeError as e:
    print("(1, [2]) as key: TypeError -", e)
