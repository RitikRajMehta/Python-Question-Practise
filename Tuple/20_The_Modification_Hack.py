# 20. The "Modification" Hack
colours = ("red", "green", "blue")
print("Original:", colours)
temp = list(colours)
temp[1] = "yellow"
colours = tuple(temp)
print("Modified:", colours)
