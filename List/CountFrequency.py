numbers = [10, 20, 10, 30, 20, 10]

frequency = {}

for x in numbers:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1

print(frequency)