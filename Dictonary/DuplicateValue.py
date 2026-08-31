data = {
    "A101": "CSE",
    "A102": "ECE",
    "A103": "CSE",
    "A104": "ME",
    "A105": "ECE",
    "A106": "CSE"
}
result = {}
for key, value in data.items():
    result.setdefault(value, []).append(key)
for key in result:
    result[key].sort()
print("Inverted Dictionary:", result)

group = None
count = 0

for key, ids in result.items():
    if len(ids) > count:
        count = len(ids)
        group = key
print("Maximum Group:", group, result[group])